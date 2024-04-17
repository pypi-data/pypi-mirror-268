"""Example of multi-LLM routing"""

from dataclasses import dataclass
import os

from fixpoint_sdk import openapi_client, FixpointClient


@dataclass
class ApiKeys:
    """Various API keys"""

    fixpoint: str
    anthropic: str
    openai: str


def main(apikeys: ApiKeys) -> None:
    """Example of multi-LLM routing"""
    client = FixpointClient(
        fixpoint_api_key=apikeys.fixpoint,
        openai_api_key=apikeys.openai,
    )

    print("\nWaiting for inference...\n\n")

    multi_completion = client.fixpoint.api.fixpoint_create_multi_llm_chat_completion(
        openapi_client.V1CreateMultiLLMChatCompletionRequest(
            mode=openapi_client.V1Mode.MODE_TEST,
            models=[
                openapi_client.V1CreateMultiLLMChatCompletionRequestModel(
                    name="anthropic/claude-3-sonnet-20240229",
                    temperature=1.0,
                    api_key=apikeys.anthropic,
                    max_tokens=1024,
                ),
                openapi_client.V1CreateMultiLLMChatCompletionRequestModel(
                    name="openai/gpt-3.5-turbo-1106",
                    temperature=1.8,
                    api_key=apikeys.openai,
                ),
                openapi_client.V1CreateMultiLLMChatCompletionRequestModel(
                    name="openai/gpt-3.5-turbo-1106",
                    temperature=0.9,
                    api_key=apikeys.openai,
                ),
            ],
            tracing=openapi_client.V1Tracing(
                session_id="27eea3a1-e16e-4643-aa0c-4b0cdb4e826b",
                trace_id="trace_id",
                span_id="46425bf0-6e48-4018-9e34-7539627a09ea",
                parent_span_id="parent_span",
            ),
            user_id="dylan",
            messages=[
                openapi_client.V1InputMessage(
                    role="system",
                    content="You are an old curmudgeonly AI. You are helpful, but you don't like being helpful. You are concise.",  # pylint: disable=line-too-long
                ),
                openapi_client.V1InputMessage(
                    role="user", content="How does ChatGPT work?"
                ),
            ],
        )
    )

    completion_id = multi_completion.id
    external_id = multi_completion.primary_external_id
    print(
        f"Made MultiLLMCompletion with ID: {completion_id}, External ID: {external_id}\n"
    )
    choice = multi_completion.completion.choices[0]
    role = choice.message.role
    content = choice.message.content
    print(f"{role}: {content}")


if __name__ == "__main__":
    main(
        ApiKeys(
            fixpoint=os.environ["FIXPOINT_API_KEY"],
            anthropic=os.environ["ANTHROPIC_API_KEY"],
            openai=os.environ["OPENAI_API_KEY"],
        )
    )
