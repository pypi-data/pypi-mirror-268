"""A module for logging LLM inferences and application logs to Fixpoint"""

from typing import cast, Any, List, Optional, Tuple, Union

from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

from .lib.requests import Requester
from .lib.debugging import dprint
from . import types


class LLMLogging:
    """A class for logging LLM input and output to Fixpoint"""

    def __init__(self, requester: Requester):
        self._requester = requester

    def log_input(
        self,
        messages: List[ChatCompletionMessageParam],
        model: types.openai.Model,
        temperature: Optional[float] = None,
        user: Optional[str] = None,
        trace_id: Optional[str] = None,
        mode: Optional[Union[types.ModeArg, types.ModeType]] = "unspecified",
        **kwargs: Any,
    ) -> types.InputLog:
        """Log the LLM input to Fixpoint"""
        return log_llm_input(
            self._requester,
            messages=messages,
            model=model,
            temperature=temperature,
            user=user,
            trace_id=trace_id,
            mode=mode,
            **kwargs,
        )

    def log_output(
        self,
        model: types.openai.Model,
        input_log: types.InputLog,
        completion: ChatCompletion,
        trace_id: Optional[str] = None,
        mode: Optional[Union[types.ModeArg, types.ModeType]] = "unspecified",
    ) -> types.OutputLog:
        """Log the LLM output to Fixpoint"""
        return log_llm_output(
            self._requester, model, input_log, completion, trace_id, mode
        )

    def log_input_and_output(
        self,
        messages: List[ChatCompletionMessageParam],
        model: types.openai.Model,
        completion: ChatCompletion,
        temperature: Optional[float] = None,
        user: Optional[str] = None,
        trace_id: Optional[str] = None,
        mode: Optional[Union[types.ModeArg, types.ModeType]] = "unspecified",
        **kwargs: Any,
    ) -> Tuple[types.InputLog, types.OutputLog]:
        """Log the LLM input and output to Fixpoint"""
        input_log = self.log_input(
            messages=messages,
            model=model,
            temperature=temperature,
            user=user,
            trace_id=trace_id,
            mode=mode,
            **kwargs,
        )
        output_log = self.log_output(model, input_log, completion, trace_id, mode)
        return input_log, output_log


def log_llm_input(
    requester: Requester,
    messages: List[ChatCompletionMessageParam],
    model: types.openai.Model,
    temperature: Optional[float] = None,
    user: Optional[str] = None,
    trace_id: Optional[str] = None,
    mode: Optional[Union[types.ModeArg, types.ModeType]] = "unspecified",
    **kwargs: Any,
) -> types.InputLog:
    """Log the LLM input to Fixpoint"""
    # Deep copy the kwargs to avoid modifying the original
    req_copy = cast(types.OpenAILLMInputLog, kwargs.copy())
    req_copy["model"] = model
    req_copy["messages"] = messages
    req_copy["user"] = user
    req_copy["temperature"] = temperature
    mode_type = types.parse_mode_type(mode)

    # Send HTTP request before calling create
    input_resp = requester.create_openai_input_log(
        req_copy["model"],
        req_copy,
        trace_id=trace_id,
        mode=mode_type,
    )
    dprint(f'Created an input log: {input_resp["name"]}')
    return input_resp


def log_llm_output(
    requester: Requester,
    model: types.openai.Model,
    input_log: types.InputLog,
    completion: ChatCompletion,
    trace_id: Optional[str] = None,
    mode: Optional[Union[types.ModeArg, types.ModeType]] = "unspecified",
) -> types.OutputLog:
    """Log the LLM output to Fixpoint"""
    output_log = requester.create_openai_output_log(
        model,
        input_log,
        completion,
        trace_id=trace_id,
        mode=types.parse_mode_type(mode),
    )
    dprint(f"Created an output log: {output_log['name']}")
    return output_log
