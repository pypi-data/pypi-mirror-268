"""Module for mocking the requests module"""

from unittest.mock import Mock

from . import requests
from .. import types


class MockRequester:
    """A mocked Requester class"""

    requester: requests.Requester

    def __init__(
        self,
        base_url: str,
        api_key: str,
        input_log_retval: types.InputLog,
        output_log_retval: types.OutputLog,
    ) -> None:
        self.requester = Mock(spec=requests.Requester)
        self.requester.base_url.return_value = base_url
        self.requester.api_key.return_value = api_key
        self.requester.create_openai_input_log.return_value = input_log_retval
        self.requester.create_openai_output_log.return_value = output_log_retval
