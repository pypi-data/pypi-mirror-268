# pylint: disable=unused-variable

"""Examples using function calling"""

import json
from typing import cast, Any, Dict, List, Tuple

from openai.types.chat import ChatCompletion
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

import fixpoint_sdk


COT_CLASSIFY_FN = "cot_classify"


class COTResult:
    """A class to help parse the chain-of-thought classification result from an eval."""

    def __init__(self, completion: ChatCompletion) -> None:
        self.completion = completion
        tcs = completion.choices[0].message.tool_calls
        if tcs is None:
            raise ValueError("No tool calls in completion")
        self.eval_json = json.loads(tcs[0].function.arguments)

    def get_cot(self) -> str:
        """Get the chain of thought reasoning for the eval"""
        return cast(str, self.eval_json["chain_of_thought"])

    def get_classification(self) -> str:
        """Get the classification result for the eval"""
        return cast(str, self.eval_json["classification"])


def main() -> Tuple[fixpoint_sdk.FixpointChatCompletion, COTResult]:
    """An example of using FixpointClient to make LLM tool calls"""
    # Make sure that the enviroment variables set:
    # - `FIXPOINT_API_KEY` is set to your Fixpoint API key
    # - `OPENAI_API_KEY` is set to your normal OpenAI API key
    # Create a FixpointClient instance (uses the FIXPOINT_API_KEY env var)
    client = fixpoint_sdk.FixpointClient()

    input_ = "Who played Dumbledore in the Harry Potter movies?"
    ideal = """Dumbledore was portrayed by Richard Harris in the film adaptations of Harry Potter and the Philosopher's Stone (2001) and Harry Potter and the Chamber of Secrets (2002). Following Harris' death in October 2002, Michael Gambon portrayed Dumbledore in the six remaining Harry Potter films from 2004 to 2011. Jude Law portrayed Dumbledore as a middle-aged man in the prequel films Fantastic Beasts: The Crimes of Grindelwald (2018) and Fantastic Beasts: The Secrets of Dumbledore (2022)."""  # pylint: disable=line-too-long
    submission = "Michael Gambon"
    messages: List[ChatCompletionMessageParam] = [
        {"role": "user", "content": make_expert_eval(input_, ideal, submission)}
    ]

    # Normally, Python should infer the return type because the `stream` arg is
    # absent, but it is not doing so here, so force cast it.
    resp = cast(
        fixpoint_sdk.FixpointChatCompletion,
        client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
            tools=make_cot_classify_tool(list("ABCDE")),
            tool_choice={"type": "function", "function": {"name": COT_CLASSIFY_FN}},
            logprobs=True,
        ),
    )

    cot_result = COTResult(resp.completion)
    return resp, cot_result


def make_cot_classify_tool(choices: List[str]) -> List[Dict[str, Any]]:
    """Make the chain-of-thought classification tool"""
    tools = [
        {
            "type": "function",
            "function": {
                "name": COT_CLASSIFY_FN,
                "description": "Classify the eval and do chain of thought",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "chain_of_thought": {
                            "type": "string",
                            "description": f"First, write out in a step by step manner your reasoning to be sure that your conclusion is correct. Avoid simply stating the correct answer at the outset. Then print only a single choice from {choices} (without quotes or punctuation) on its own line corresponding to the correct answer",  # pylint: disable=line-too-long
                        },
                        "classification": {"type": "string", "enum": choices},
                    },
                    "required": ["classification", "chain_of_thought"],
                },
            },
        }
    ]
    return tools


def make_expert_eval(input_: str, ideal: str, submission: str) -> str:
    """Make the expert eval prompt."""
    # pylint: disable=line-too-long
    eval_prompt = f"""You are comparing a submitted answer to an expert answer on a given question. Here is the data:
[BEGIN DATA]
************
[Question]: {input_}
************
[Expert]: {ideal}
************
[Submission]: {submission}
************
[END DATA]

Compare the factual content of the submitted answer with the expert answer. Ignore any differences in style, grammar, or punctuation.
The submitted answer may either be a subset or superset of the expert answer, or it may conflict with it. Determine which case applies. Answer the question by selecting one of the following options:
(A) The submitted answer is a subset of the expert answer and is fully consistent with it.
(B) The submitted answer is a superset of the expert answer and is fully consistent with it.
(C) The submitted answer contains all the same details as the expert answer.
(D) There is a disagreement between the submitted answer and the expert answer.
(E) The answers differ, but these differences don't matter from the perspective of factuality."""
    return eval_prompt


if __name__ == "__main__":
    main()
