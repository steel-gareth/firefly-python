# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.webhooks.messages import attempt_list_params
from ....types.webhooks.messages.attempt_list_response import AttemptListResponse
from ....types.webhooks.messages.attempt_retrieve_response import AttemptRetrieveResponse

__all__ = ["AttemptsResource", "AsyncAttemptsResource"]


class AttemptsResource(SyncAPIResource):
    """
    These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
    """

    @cached_property
    def with_raw_response(self) -> AttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AttemptsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        attempt_id: int,
        *,
        id: str,
        message_id: int,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttemptRetrieveResponse:
        """
        When a webhook message fails to send it will store the failure in an "attempt".
        You can view and analyse these. Webhooks messages that receive too many attempts
        (failures) will not be fired. You must first clear out old attempts and try
        again. This endpoint shows you the details of a single attempt. The ID of the
        attempt must match the corresponding webhook and webhook message.

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
            path_template(
                "/v1/webhooks/{id}/messages/{message_id}/attempts/{attempt_id}",
                id=id,
                message_id=message_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttemptRetrieveResponse,
        )

    def list(
        self,
        message_id: int,
        *,
        id: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttemptListResponse:
        """
        When a webhook message fails to send it will store the failure in an "attempt".
        You can view and analyse these. Webhook messages that receive too many attempts
        (failures) will not be sent again. You must first clear out old attempts before
        the message can go out again.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

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
            path_template("/v1/webhooks/{id}/messages/{message_id}/attempts", id=id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    attempt_list_params.AttemptListParams,
                ),
            ),
            cast_to=AttemptListResponse,
        )

    def delete(
        self,
        attempt_id: int,
        *,
        id: str,
        message_id: int,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a webhook message attempt.

        If you delete all attempts for a webhook
        message, Firefly III will (once again) assume all is well with the webhook
        message and will try to send it again.

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
            path_template(
                "/v1/webhooks/{id}/messages/{message_id}/attempts/{attempt_id}",
                id=id,
                message_id=message_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAttemptsResource(AsyncAPIResource):
    """
    These endpoints can be used to manage the user&#039;s webhooks and triggers them if necessary.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncAttemptsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        attempt_id: int,
        *,
        id: str,
        message_id: int,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttemptRetrieveResponse:
        """
        When a webhook message fails to send it will store the failure in an "attempt".
        You can view and analyse these. Webhooks messages that receive too many attempts
        (failures) will not be fired. You must first clear out old attempts and try
        again. This endpoint shows you the details of a single attempt. The ID of the
        attempt must match the corresponding webhook and webhook message.

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
            path_template(
                "/v1/webhooks/{id}/messages/{message_id}/attempts/{attempt_id}",
                id=id,
                message_id=message_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttemptRetrieveResponse,
        )

    async def list(
        self,
        message_id: int,
        *,
        id: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttemptListResponse:
        """
        When a webhook message fails to send it will store the failure in an "attempt".
        You can view and analyse these. Webhook messages that receive too many attempts
        (failures) will not be sent again. You must first clear out old attempts before
        the message can go out again.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

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
            path_template("/v1/webhooks/{id}/messages/{message_id}/attempts", id=id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    attempt_list_params.AttemptListParams,
                ),
            ),
            cast_to=AttemptListResponse,
        )

    async def delete(
        self,
        attempt_id: int,
        *,
        id: str,
        message_id: int,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a webhook message attempt.

        If you delete all attempts for a webhook
        message, Firefly III will (once again) assume all is well with the webhook
        message and will try to send it again.

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
            path_template(
                "/v1/webhooks/{id}/messages/{message_id}/attempts/{attempt_id}",
                id=id,
                message_id=message_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AttemptsResourceWithRawResponse:
    def __init__(self, attempts: AttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = to_raw_response_wrapper(
            attempts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            attempts.list,
        )
        self.delete = to_raw_response_wrapper(
            attempts.delete,
        )


class AsyncAttemptsResourceWithRawResponse:
    def __init__(self, attempts: AsyncAttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = async_to_raw_response_wrapper(
            attempts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            attempts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            attempts.delete,
        )


class AttemptsResourceWithStreamingResponse:
    def __init__(self, attempts: AttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = to_streamed_response_wrapper(
            attempts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            attempts.list,
        )
        self.delete = to_streamed_response_wrapper(
            attempts.delete,
        )


class AsyncAttemptsResourceWithStreamingResponse:
    def __init__(self, attempts: AsyncAttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = async_to_streamed_response_wrapper(
            attempts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            attempts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            attempts.delete,
        )
