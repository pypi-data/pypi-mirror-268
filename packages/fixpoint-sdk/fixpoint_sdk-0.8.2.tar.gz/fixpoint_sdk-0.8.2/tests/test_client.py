# pylint: disable=missing-function-docstring, missing-class-docstring, missing-module-docstring

from dataclasses import dataclass
from typing import List

from openai.types.chat import ChatCompletion, chat_completion
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.completion_usage import CompletionUsage

from fixpoint_sdk import FixpointClient, types as fixtypes
from fixpoint_sdk.client import _FixpointClientDeps
from fixpoint_sdk.completions import _ChatDeps, _CompletionsDeps
from fixpoint_sdk.lib._mock_requests import MockRequester
from fixpoint_sdk._mock_completions import MockChatCompletion


def test_log_llm_input_output() -> None:
    messages: List[ChatCompletionMessageParam] = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are you?"},
    ]
    model = "gpt-3.5-turbo"
    temperature = 0.7
    user = "dylan-uid"
    trace_id = "some-trace-id"
    input_log_retval: fixtypes.InputLog = {
        "name": "input-log-name",
        "modelName": model,
        "sessionName": None,
        "messages": messages,
        "temperature": temperature,
        "createdAt": None,
        "traceId": "some-trace-id",
    }
    output_log_retval: fixtypes.OutputLog = {"name": "output-log-name"}
    mock_env = new_mock_chat_client(input_log_retval, output_log_retval)

    completion = ChatCompletion(
        id="chatcmpl-8y9PZoZGSd7SZDXRLqYCB0FbUD2R7",
        choices=[
            chat_completion.Choice(
                finish_reason="stop",
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content="I am a computer program designed to assist and provide information to users like yourself. How can I help you today?",  # pylint: disable=line-too-long
                    role="assistant",
                    function_call=None,
                    tool_calls=None,
                ),
            )
        ],
        created=1709346549,
        model=model,
        object="chat.completion",
        system_fingerprint="fp_2b778c6b35",
        usage=CompletionUsage(completion_tokens=23, prompt_tokens=21, total_tokens=44),
    )

    mock_env.mock_completions.set_return_value(completion)

    mock_env.client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        user=user,
        trace_id=trace_id,
        mode=fixtypes.ModeType.MODE_TEST.value,
    )

    mock_env.mock_completions.create_completion.assert_called_once()  # type: ignore

    # pylint: disable=line-too-long
    mock_env.mock_requester.requester.create_openai_input_log.assert_called_once_with(  # type: ignore
        model,
        {
            "temperature": temperature,
            "user": user,
            "model": model,
            "messages": messages,
        },
        trace_id=trace_id,
        mode=fixtypes.ModeType.MODE_TEST,
    )

    # pylint: disable=line-too-long
    mock_env.mock_requester.requester.create_openai_output_log.assert_called_once_with(  # type: ignore
        model,
        input_log_retval,
        completion,
        trace_id=trace_id,
        mode=fixtypes.ModeType.MODE_TEST,
    )


@dataclass
class MockEnv:
    client: FixpointClient
    mock_requester: MockRequester
    mock_completions: MockChatCompletion


def new_mock_chat_client(
    input_log_retval: fixtypes.InputLog, output_log_retval: fixtypes.OutputLog
) -> MockEnv:
    base_url = "http://localhost:8000"
    fixpoint_api_key = "fake-fixpoint-key"
    mock_requester = MockRequester(
        base_url=base_url,
        api_key=fixpoint_api_key,
        input_log_retval=input_log_retval,
        output_log_retval=output_log_retval,
    )
    mock_chat_completions = MockChatCompletion()

    client = FixpointClient(
        api_base_url=base_url,
        fixpoint_api_key=fixpoint_api_key,
        openai_api_key="fake-openai-key",
        _deps=_FixpointClientDeps(
            requester=mock_requester.requester,
            chat=_ChatDeps(
                completions=_CompletionsDeps(
                    create_completion=mock_chat_completions.create_completion,
                )
            ),
        ),
    )

    return MockEnv(
        client=client,
        mock_requester=mock_requester,
        mock_completions=mock_chat_completions,
    )
