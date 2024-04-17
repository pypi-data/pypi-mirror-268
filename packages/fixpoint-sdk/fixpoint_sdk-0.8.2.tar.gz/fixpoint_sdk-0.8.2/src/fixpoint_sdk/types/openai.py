"""Types for interfacing with the OpenAI API and SDK"""

from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass

import httpx

from openai._types import NOT_GIVEN, NotGiven, Body, Query, Headers
from openai.types.chat import (
    completion_create_params,
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam,
)
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

from ._utils import to_dict_without_not_given


Model = Union[
    str,
    Literal[
        "gpt-4-1106-preview",
        "gpt-4-vision-preview",
        "gpt-4",
        "gpt-4-0314",
        "gpt-4-0613",
        "gpt-4-32k",
        "gpt-4-32k-0314",
        "gpt-4-32k-0613",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo-0301",
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-1106",
        "gpt-3.5-turbo-16k-0613",
    ],
]


@dataclass
class CreateChatCompletionRequest:
    """A normal chat completion create request"""

    messages: List[ChatCompletionMessageParam]
    model: Model
    frequency_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN
    function_call: Union[completion_create_params.FunctionCall, NotGiven] = NOT_GIVEN
    functions: Union[List[completion_create_params.Function], NotGiven] = NOT_GIVEN
    logit_bias: Union[Optional[Dict[str, int]], NotGiven] = NOT_GIVEN
    logprobs: Union[Optional[bool], NotGiven] = NOT_GIVEN
    max_tokens: Union[Optional[int], NotGiven] = NOT_GIVEN
    n: Union[Optional[int], NotGiven] = NOT_GIVEN
    presence_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN
    response_format: Union[completion_create_params.ResponseFormat, NotGiven] = (
        NOT_GIVEN
    )
    seed: Union[Optional[int], NotGiven] = NOT_GIVEN
    stop: Union[Union[Optional[str], List[str]], NotGiven] = NOT_GIVEN
    stream: Union[Optional[Literal[False]], Literal[True], NotGiven] = NOT_GIVEN
    temperature: Union[Optional[float], NotGiven] = NOT_GIVEN
    tool_choice: Union[ChatCompletionToolChoiceOptionParam, NotGiven] = NOT_GIVEN
    tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN
    top_logprobs: Union[Optional[int], NotGiven] = NOT_GIVEN
    top_p: Union[Optional[float], NotGiven] = NOT_GIVEN
    user: Union[str, NotGiven] = NOT_GIVEN

    # Use the following arguments if you need to pass additional parameters
    # to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the
    # client or passed to this method.
    extra_headers: Union[Headers, None] = None
    extra_query: Union[Query, None] = None
    extra_body: Union[Body, None] = None
    timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN

    def to_dict(self) -> Dict[str, Any]:
        """Convert to a dict, removing fields that were never set."""
        return to_dict_without_not_given(self)


@dataclass
class RoutedCreateChatCompletionRequest:
    """A chat completion create request for a model-router completion"""

    messages: List[ChatCompletionMessageParam]
    frequency_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN
    function_call: Union[completion_create_params.FunctionCall, NotGiven] = NOT_GIVEN
    functions: Union[List[completion_create_params.Function], NotGiven] = NOT_GIVEN
    logit_bias: Union[Optional[Dict[str, int]], NotGiven] = NOT_GIVEN
    logprobs: Union[Optional[bool], NotGiven] = NOT_GIVEN
    max_tokens: Union[Optional[int], NotGiven] = NOT_GIVEN
    n: Union[Optional[int], NotGiven] = NOT_GIVEN
    presence_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN
    response_format: Union[completion_create_params.ResponseFormat, NotGiven] = (
        NOT_GIVEN
    )
    seed: Union[Optional[int], NotGiven] = NOT_GIVEN
    stop: Union[Union[Optional[str], List[str]], NotGiven] = NOT_GIVEN
    stream: Union[Optional[Literal[False]], Literal[True], NotGiven] = NOT_GIVEN
    temperature: Union[Optional[float], NotGiven] = NOT_GIVEN
    tool_choice: Union[ChatCompletionToolChoiceOptionParam, NotGiven] = NOT_GIVEN
    tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN
    top_logprobs: Union[Optional[int], NotGiven] = NOT_GIVEN
    top_p: Union[Optional[float], NotGiven] = NOT_GIVEN
    user: Union[str, NotGiven] = NOT_GIVEN

    # Use the following arguments if you need to pass additional parameters
    # to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the
    # client or passed to this method.
    extra_headers: Union[Headers, None] = None
    extra_query: Union[Query, None] = None
    extra_body: Union[Body, None] = None
    timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN

    def to_dict(self) -> Dict[str, Any]:
        """Convert to a dict, removing fields that were never set."""
        return to_dict_without_not_given(self)
