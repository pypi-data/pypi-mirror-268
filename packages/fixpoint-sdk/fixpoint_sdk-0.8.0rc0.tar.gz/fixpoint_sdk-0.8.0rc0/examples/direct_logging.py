"""An example calling OpenAI directly

This example demonstrates how to call OpenAI directly and then to log the LLM
input and output to Fixpoint.
"""

from typing import List

from openai import OpenAI
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

import fixpoint_sdk
from fixpoint_sdk import FixpointClient


def main() -> None:
    """An example calling OpenAI directly"""
    openaiclient = OpenAI()
    client = FixpointClient()

    messages: List[ChatCompletionMessageParam] = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are you?"},
    ]
    user_id = "some-user-id"
    model: fixpoint_sdk.types.openai.Model = "gpt-3.5-turbo-0125"

    completion = openaiclient.chat.completions.create(
        messages=messages, model=model, user=user_id
    )

    input_log, output_log = client.fixpoint.logging.llm.log_input_and_output(
        messages,
        model,
        completion,
        mode="test",
        trace_id="some-trace-id",
        user=user_id,
    )
    print(f"Logged LLM input: {input_log['name']}")
    print(f"Logged LLM output: {output_log['name']}")


if __name__ == "__main__":
    main()
