"""Mocks for the completions module"""

from typing import Callable
from unittest.mock import Mock

from openai.types.chat import ChatCompletion

from . import types

ChatCompletionFn = Callable[[types.openai.CreateChatCompletionRequest], ChatCompletion]


class MockChatCompletion:
    """A mocked ChatCompletion class"""

    create_completion: ChatCompletionFn

    def __init__(self) -> None:
        self.create_completion = Mock()

    def set_return_value(self, retval: ChatCompletion) -> None:
        """Set the return value of the create_completion function."""
        self.create_completion.return_value = retval  # type: ignore
