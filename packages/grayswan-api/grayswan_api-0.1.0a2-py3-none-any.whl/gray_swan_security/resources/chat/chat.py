# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .completion import (
    Completion,
    AsyncCompletion,
    CompletionWithRawResponse,
    AsyncCompletionWithRawResponse,
    CompletionWithStreamingResponse,
    AsyncCompletionWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Chat", "AsyncChat"]


class Chat(SyncAPIResource):
    @cached_property
    def completion(self) -> Completion:
        return Completion(self._client)

    @cached_property
    def with_raw_response(self) -> ChatWithRawResponse:
        return ChatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatWithStreamingResponse:
        return ChatWithStreamingResponse(self)


class AsyncChat(AsyncAPIResource):
    @cached_property
    def completion(self) -> AsyncCompletion:
        return AsyncCompletion(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatWithRawResponse:
        return AsyncChatWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatWithStreamingResponse:
        return AsyncChatWithStreamingResponse(self)


class ChatWithRawResponse:
    def __init__(self, chat: Chat) -> None:
        self._chat = chat

    @cached_property
    def completion(self) -> CompletionWithRawResponse:
        return CompletionWithRawResponse(self._chat.completion)


class AsyncChatWithRawResponse:
    def __init__(self, chat: AsyncChat) -> None:
        self._chat = chat

    @cached_property
    def completion(self) -> AsyncCompletionWithRawResponse:
        return AsyncCompletionWithRawResponse(self._chat.completion)


class ChatWithStreamingResponse:
    def __init__(self, chat: Chat) -> None:
        self._chat = chat

    @cached_property
    def completion(self) -> CompletionWithStreamingResponse:
        return CompletionWithStreamingResponse(self._chat.completion)


class AsyncChatWithStreamingResponse:
    def __init__(self, chat: AsyncChat) -> None:
        self._chat = chat

    @cached_property
    def completion(self) -> AsyncCompletionWithStreamingResponse:
        return AsyncCompletionWithStreamingResponse(self._chat.completion)
