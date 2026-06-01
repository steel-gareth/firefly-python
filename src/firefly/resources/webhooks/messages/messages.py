# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .attempts import (
    AttemptsResource,
    AsyncAttemptsResource,
    AttemptsResourceWithRawResponse,
    AsyncAttemptsResourceWithRawResponse,
    AttemptsResourceWithStreamingResponse,
    AsyncAttemptsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.webhooks.message_list_response import MessageListResponse
from ....types.webhooks.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    """
    These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
    """

    @cached_property
    def attempts(self) -> AttemptsResource:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        return AttemptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: int,
        *,
        id: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        When a webhook is triggered it will store the actual content of the webhook in a
        webhook message. You can view and analyse a single one using this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/webhooks/{id}/messages/{message_id}", id=id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def list(
        self,
        id: str,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        When a webhook is triggered the actual message that will be send is stored in a
        "message". You can view and analyse these messages.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/webhooks/{id}/messages", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageListResponse,
        )

    def delete(
        self,
        message_id: int,
        *,
        id: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a webhook message.

        Any time a webhook is triggered the message is stored
        before it's sent. You can delete them before or after sending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/webhooks/{id}/messages/{message_id}", id=id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMessagesResource(AsyncAPIResource):
    """
    These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
    """

    @cached_property
    def attempts(self) -> AsyncAttemptsResource:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        return AsyncAttemptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: int,
        *,
        id: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        When a webhook is triggered it will store the actual content of the webhook in a
        webhook message. You can view and analyse a single one using this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/webhooks/{id}/messages/{message_id}", id=id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def list(
        self,
        id: str,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        When a webhook is triggered the actual message that will be send is stored in a
        "message". You can view and analyse these messages.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/webhooks/{id}/messages", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageListResponse,
        )

    async def delete(
        self,
        message_id: int,
        *,
        id: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a webhook message.

        Any time a webhook is triggered the message is stored
        before it's sent. You can delete them before or after sending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/webhooks/{id}/messages/{message_id}", id=id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )

    @cached_property
    def attempts(self) -> AttemptsResourceWithRawResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        return AttemptsResourceWithRawResponse(self._messages.attempts)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )

    @cached_property
    def attempts(self) -> AsyncAttemptsResourceWithRawResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        return AsyncAttemptsResourceWithRawResponse(self._messages.attempts)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )

    @cached_property
    def attempts(self) -> AttemptsResourceWithStreamingResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        return AttemptsResourceWithStreamingResponse(self._messages.attempts)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )

    @cached_property
    def attempts(self) -> AsyncAttemptsResourceWithStreamingResponse:
        """
        These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
        """
        return AsyncAttemptsResourceWithStreamingResponse(self._messages.attempts)
