# pylint: disable=missing-function-docstring, missing-class-docstring, missing-module-docstring

from typing import Any, Dict

from fixpoint_sdk.types import openai


def test_to_dict() -> None:
    request = openai.CreateChatCompletionRequest(
        messages=[{"role": "user", "content": "Hello!"}], model="gpt-3.5-turbo"
    )
    expected: Dict[str, Any] = {
        "messages": [{"role": "user", "content": "Hello!"}],
        "model": "gpt-3.5-turbo",
        "extra_body": None,
        "extra_query": None,
        "extra_headers": None,
    }
    assert request.to_dict() == expected

    request = openai.CreateChatCompletionRequest(
        messages=[{"role": "user", "content": "Hello!"}],
        model="gpt-3.5-turbo",
        frequency_penalty=0.5,
    )
    expected = {
        "messages": [{"role": "user", "content": "Hello!"}],
        "model": "gpt-3.5-turbo",
        "frequency_penalty": 0.5,
        "extra_body": None,
        "extra_query": None,
        "extra_headers": None,
    }
    assert request.to_dict() == expected

    request = openai.CreateChatCompletionRequest(
        messages=[{"role": "user", "content": "Hello!"}],
        model="gpt-3.5-turbo",
        frequency_penalty=None,
    )
    expected = {
        "messages": [{"role": "user", "content": "Hello!"}],
        "model": "gpt-3.5-turbo",
        "frequency_penalty": None,
        "extra_body": None,
        "extra_query": None,
        "extra_headers": None,
    }
    assert request.to_dict() == expected
