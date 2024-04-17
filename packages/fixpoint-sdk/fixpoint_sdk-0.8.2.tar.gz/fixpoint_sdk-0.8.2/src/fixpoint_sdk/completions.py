"""Code for chat completions."""

import typing
from typing import Callable, Optional, Literal, List, Generator
from dataclasses import dataclass

from openai import OpenAI
from openai._streaming import Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

from .lib.requests import Requester
from .lib.debugging import dprint
from .lib.iterwrapper import IterWrapper
from .lib.logging import logger
from . import types
from ._logging_api import log_llm_input, log_llm_output


@dataclass
class FixpointChatRoutedCompletion:
    """Wraps the OpenAI chat completion with logging data."""

    completion: types.ChatCompletion


@dataclass
class FixpointChatCompletion:
    """Wraps the OpenAI chat completion with logging data."""

    completion: ChatCompletion
    input_log: types.InputLog
    output_log: types.OutputLog


class FixpointChatCompletionStream:
    """Wraps the OpenAI chat completion stream with logging data."""

    _stream: Stream[ChatCompletionChunk]
    input_log: types.InputLog
    _output_log: typing.Optional[types.OutputLog]
    _outputs: typing.List[ChatCompletionChunk]
    _mode_type: types.ModeType
    _requester: Requester
    _trace_id: typing.Optional[str]
    _model_name: str
    _all_streamed: bool = False

    def __init__(
        self,
        *,
        stream: Stream[ChatCompletionChunk],
        input_log: types.InputLog,
        mode_type: types.ModeType,
        requester: Requester,
        trace_id: typing.Optional[str] = None,
        model_name: str,
    ):
        self.input_log = input_log
        self._output_log = None
        self._mode_type = mode_type
        self._requester = requester
        self._trace_id = trace_id
        self._model_name = model_name

        self._stream = stream
        self._outputs = []
        self._all_streamed = False

        def on_finish() -> None:
            self._all_streamed = True
            # Send HTTP request after calling create
            try:
                output_log = log_llm_output(
                    self._requester,
                    self._model_name,
                    self.input_log,
                    combine_chunks(self._outputs),
                    trace_id=self._trace_id,
                    mode=self._mode_type,
                )
                self._output_log = output_log
            # pylint: disable=broad-exception-caught
            except Exception:
                logger.exception("error logging LLM output")

        def on_error(exc: Exception) -> None:
            raise exc

        self._iter_wrapper = IterWrapper(
            stream, on_iter=self._outputs.append, on_finish=on_finish, on_error=on_error
        )

    def __next__(self) -> ChatCompletionChunk:
        return self._iter_wrapper.__next__()

    # pylint: disable=use-yield-from
    def __iter__(self) -> typing.Iterator[ChatCompletionChunk]:
        """Yield the chat completion chunks."""
        return self

    @property
    def completion(self) -> Generator[ChatCompletionChunk, None, None]:
        """Yield the chat completion chunks."""
        for chunk in self:
            yield chunk

    # This function is deprecated, because `completion` exists on all inference
    # response types while `completions` only exists on streaming response.
    @property
    def completions(self) -> Generator[ChatCompletionChunk, None, None]:
        """Yield the chat completion chunks."""
        return self.completion

    @property
    def output_log(self) -> typing.Optional[types.OutputLog]:
        """Returns the output log if we have streamed all output chunks."""
        if not self._all_streamed:
            logger.warning(
                "\n".join(
                    [
                        "FixpointChatCompletionStream.output_log error: stream all output chunks before accessing output_log.",  # pylint: disable=line-too-long
                        "\tStream by either iterating over the FixpointChatCompletionStream object, or its FixpointChatCompletionStream.completions property.",  # pylint: disable=line-too-long
                    ]
                )
            )
        return self._output_log


FinishReason = typing.Literal[
    "stop", "length", "tool_calls", "content_filter", "function_call"
]


def combine_chunks(chunks: typing.List[ChatCompletionChunk]) -> ChatCompletion:
    """Combine chunks from a stream into one full completion object."""
    if len(chunks) == 0:
        raise ValueError("Must have at least one chunk")

    num_choices = 0
    for chunk in chunks:
        if num_choices == 0:
            num_choices = len(chunk.choices)
        elif num_choices != len(chunk.choices):
            raise ValueError("All chunks must have the same number of choices")

    chatid = ""
    created = 0
    model = ""
    choice_contents: typing.List[typing.List[str]] = [[] for _ in range(num_choices)]
    # default to "assistant" for typing reasons
    # default to "stop" for typing reasons
    finish_reasons: typing.List[FinishReason] = ["stop" for _ in range(num_choices)]
    for chunk in chunks:
        # all `id` and `created` values are the same.
        chatid = chunk.id
        created = chunk.created
        model = chunk.model
        for choice in chunk.choices:
            if choice.delta.content is not None:
                choice_contents[choice.index].append(choice.delta.content)
            # default to "stop" for typing reasons
            finish_reasons[choice.index] = choice.finish_reason or "stop"

    final_choices = []
    for i, choice_content in enumerate(choice_contents):
        final_choices.append(
            Choice(
                index=i,
                finish_reason=finish_reasons[i],
                logprobs=None,
                message=ChatCompletionMessage(
                    # all output roles are assistants
                    role="assistant",
                    content="".join(choice_content),
                ),
            )
        )

    return ChatCompletion(
        id=chatid,
        created=created,
        model=model,
        object="chat.completion",
        # The server will compute this when logging
        usage=None,
        choices=final_choices,
    )


@dataclass
class _CompletionsDeps:
    create_completion: Optional[
        Callable[[types.openai.CreateChatCompletionRequest], ChatCompletion]
    ] = None


class Completions:
    """Create chat completion inferences and log them."""

    _deps: Optional[_CompletionsDeps] = None
    """For dependency injection. Useful for testing, etc."""

    def __init__(
        self,
        requester: Requester,
        client: OpenAI,
        _deps: Optional[_CompletionsDeps] = None,
    ):
        self.client = client
        self._requester = requester
        self._deps = _deps

    @typing.overload
    def create(
        self,
        *,
        messages: List[ChatCompletionMessageParam],
        model: types.openai.Model,
        stream: Optional[Literal[False]],
        **kwargs: typing.Any,
    ) -> FixpointChatCompletion: ...

    @typing.overload
    def create(
        self,
        *,
        messages: List[ChatCompletionMessageParam],
        model: types.openai.Model,
        stream: Literal[True],
        **kwargs: typing.Any,
    ) -> FixpointChatCompletionStream: ...

    @typing.overload
    def create(
        self,
        *,
        messages: List[ChatCompletionMessageParam],
        model: types.openai.Model,
        stream: bool,
        **kwargs: typing.Any,
    ) -> typing.Union[FixpointChatCompletion, FixpointChatCompletionStream]: ...

    @typing.overload
    def create(
        self,
        *,
        messages: List[ChatCompletionMessageParam],
        model: types.openai.Model,
        stream: typing.Union[Optional[Literal[False]], Literal[True]] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[FixpointChatCompletion, FixpointChatCompletionStream]: ...

    def create(
        self,
        *,
        messages: List[ChatCompletionMessageParam],
        model: types.openai.Model,
        stream: typing.Union[Optional[Literal[False]], Literal[True]] = None,
        mode: Optional[types.ModeArg] = "unspecified",
        **kwargs: typing.Any,
    ) -> typing.Union[FixpointChatCompletion, FixpointChatCompletionStream]:
        """Create an OpenAI completion and log the LLM input and output."""

        # Separate out the kwargs so that we can pass through all extra
        # arguments to OpenAI but also avoid having duplicate keyword arguments
        # when calling the Fixpoint APIs.

        # Do not mutate the input kwargs. That is an unexpected behavior for
        # our caller.
        openaikwargs = kwargs.copy()
        # Extract trace_id from kwargs, if it exists, otherwise set it to None
        trace_id = openaikwargs.pop("trace_id", None)
        mode_type = types.parse_mode_type(mode)

        fixpointkwargs = openaikwargs.copy()
        user = fixpointkwargs.pop("user", None)
        temperature = fixpointkwargs.pop("temperature", None)

        input_log = log_llm_input(
            self._requester,
            messages=messages,
            model=model,
            trace_id=trace_id,
            mode=mode,
            user=user,
            temperature=temperature,
            **fixpointkwargs,
        )

        if stream:
            completion = self.client.chat.completions.create(
                messages=messages, model=model, stream=stream, **openaikwargs
            )
            dprint("Received an openai response stream")
            return FixpointChatCompletionStream(
                stream=completion,
                input_log=input_log,
                mode_type=mode_type,
                requester=self._requester,
                trace_id=trace_id,
                model_name=model,
            )

        if self._deps and self._deps.create_completion:
            completion = self._deps.create_completion(
                types.openai.CreateChatCompletionRequest(
                    messages=messages, model=model, stream=stream, **openaikwargs
                )
            )
        else:
            completion = self.client.chat.completions.create(
                messages=messages, model=model, stream=stream, **openaikwargs
            )
        dprint(f"Received an openai response: {completion.id}")
        output_log = log_llm_output(
            self._requester,
            model,
            input_log,
            completion,
            trace_id=trace_id,
            mode=mode,
        )
        return FixpointChatCompletion(
            completion=completion,
            input_log=input_log,
            output_log=output_log,
        )


class RoutedCompletions:
    """Create chat completion inferences and log them."""

    def __init__(self, requester: Requester, client: OpenAI):
        self._requester = requester
        self._client = client

    def create(
        self,
        *,
        messages: List[ChatCompletionMessageParam],
        mode: Optional[types.ModeArg] = "unspecified",
        **kwargs: typing.Any,
    ) -> FixpointChatRoutedCompletion:
        """Create an OpenAI completion and log the LLM input and output."""

        if "model" in kwargs:
            raise ValueError('you cannot pass a "model" to the completions router')

        # Prepare the request
        req_copy = kwargs.copy()
        trace_id = req_copy.pop("trace_id", None)

        routed_log_resp = self._requester.create_openai_routed_log(
            types.openai.RoutedCreateChatCompletionRequest(
                messages=messages, **req_copy
            ),
            mode=types.parse_mode_type(mode),
            trace_id=trace_id,
        )
        dprint(f"Created a routed log: {routed_log_resp['id']}")

        return FixpointChatRoutedCompletion(
            completion=routed_log_resp,
        )


class ChatWithRouter:
    """The Chat class lets you interact with the underlying chat APIs."""

    def __init__(self, requester: Requester, client: OpenAI):
        self.completions = RoutedCompletions(requester, client)


@dataclass
class _ChatDeps:
    completions: Optional[_CompletionsDeps] = None


class Chat:
    """The Chat class lets you interact with the underlying chat APIs."""

    def __init__(
        self, requester: Requester, client: OpenAI, _deps: Optional[_ChatDeps] = None
    ):
        _completions_deps = None
        if _deps and _deps.completions:
            _completions_deps = _deps.completions
        self.completions = Completions(requester, client, _deps=_completions_deps)
