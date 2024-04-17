"""Defines the Fixpoint client, which is the main interface for the SDK."""

from dataclasses import dataclass
import typing

from openai import OpenAI

from fixpoint_openapi.configuration import Configuration
from fixpoint_openapi.api_client import ApiClient
from fixpoint_openapi.api.fixpoint_api import FixpointApi

from .lib.env import get_fixpoint_api_key, get_api_base_url
from .lib.requests import Requester
from . import types
from .completions import Chat, ChatWithRouter, _ChatDeps
from ._logging_api import LLMLogging


@dataclass
class _FixpointClientDeps:
    chat: typing.Optional[_ChatDeps] = None
    requester: typing.Optional[Requester] = None


class _FixpointClientBase:
    def __init__(
        self,
        *,
        fixpoint_api_key: typing.Optional[str] = None,
        openai_api_key: typing.Optional[str] = None,
        api_base_url: typing.Optional[str] = None,
        _deps: typing.Optional[_FixpointClientDeps] = None,
        **kwargs: typing.Any,
    ):
        # Check that the environment variable FIXPOINT_API_KEY is set
        _api_key = get_fixpoint_api_key(fixpoint_api_key)

        self._api_key = _api_key
        if _deps and _deps.requester:
            self._requester = _deps.requester
        else:
            self._requester = Requester(self._api_key, get_api_base_url(api_base_url))
        if openai_api_key:
            kwargs = dict(kwargs, api_key=openai_api_key)
        self.fixpoint = _Fixpoint(self._requester)


class ChatRouterClient(_FixpointClientBase):
    """The ChatRouterClient lets you interact with the Fixpoint API and the OpenAI API."""

    def __init__(
        self,
        *,
        fixpoint_api_key: typing.Optional[str] = None,
        openai_api_key: typing.Optional[str] = None,
        api_base_url: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(
            fixpoint_api_key=fixpoint_api_key,
            openai_api_key=openai_api_key,
            api_base_url=api_base_url,
            **kwargs,
        )
        client = OpenAI(api_key=openai_api_key, **kwargs)
        self.chat = ChatWithRouter(self._requester, client)


class FixpointClient(_FixpointClientBase):
    """The FixpointClient lets you interact with the Fixpoint API."""

    def __init__(
        self,
        *,
        fixpoint_api_key: typing.Optional[str] = None,
        openai_api_key: typing.Optional[str] = None,
        api_base_url: typing.Optional[str] = None,
        _deps: typing.Optional[_FixpointClientDeps] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(
            fixpoint_api_key=fixpoint_api_key,
            openai_api_key=openai_api_key,
            api_base_url=api_base_url,
            _deps=_deps,
            **kwargs,
        )
        client = OpenAI(api_key=openai_api_key, **kwargs)
        chat_deps = None
        if _deps:
            chat_deps = _deps.chat
        self.chat = Chat(self._requester, client, _deps=chat_deps)


class _Fixpoint:
    api: FixpointApi

    def __init__(self, requester: Requester):
        self.user_feedback = self._UserFeedback(requester)
        self.attributes = self._Attributes(requester)
        self.logging = self._Logging(LLMLogging(requester))

        configuration = Configuration(
            host=get_api_base_url(requester.base_url()),
        )

        api_client = ApiClient(
            configuration,
            header_name="Authorization",
            header_value=f"Bearer {requester.api_key()}",
        )
        self.api = FixpointApi(api_client)
        self.proxy_client = self.api

    class _Logging:
        def __init__(self, llm: LLMLogging):
            self.llm = llm

    class _UserFeedback:
        def __init__(self, requester: Requester):
            self._requester = requester

        def create(
            self, request: types.CreateUserFeedbackRequest
        ) -> types.CreateUserFeedbackResponse:
            """Attach user feedback to an LLM log."""
            return self._requester.create_user_feedback(request)

    class _Attributes:
        def __init__(self, requester: Requester):
            self._requester = requester

        def create(
            self, request: types.CreateLogAttributeRequest
        ) -> types.LogAttribute:
            """Attach a log attribute to an LLM log."""
            return self._requester.create_attribute(request)
