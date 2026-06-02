# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_single import UserSingle
from ..types.about_retrieve_info_response import AboutRetrieveInfoResponse

__all__ = ["AboutResource", "AsyncAboutResource"]


class AboutResource(SyncAPIResource):
    """
    These endpoints deliver general system information, version- and meta information.
    """

    @cached_property
    def with_raw_response(self) -> AboutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AboutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AboutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AboutResourceWithStreamingResponse(self)

    def retrieve_info(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AboutRetrieveInfoResponse:
        """
        Returns general system information and versions of the (supporting) software.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/about",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AboutRetrieveInfoResponse,
        )

    def retrieve_user(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserSingle:
        """
        Returns the currently authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/about/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSingle,
        )


class AsyncAboutResource(AsyncAPIResource):
    """
    These endpoints deliver general system information, version- and meta information.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAboutResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAboutResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAboutResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncAboutResourceWithStreamingResponse(self)

    async def retrieve_info(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AboutRetrieveInfoResponse:
        """
        Returns general system information and versions of the (supporting) software.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/about",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AboutRetrieveInfoResponse,
        )

    async def retrieve_user(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserSingle:
        """
        Returns the currently authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/about/user",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSingle,
        )


class AboutResourceWithRawResponse:
    def __init__(self, about: AboutResource) -> None:
        self._about = about

        self.retrieve_info = to_raw_response_wrapper(
            about.retrieve_info,
        )
        self.retrieve_user = to_raw_response_wrapper(
            about.retrieve_user,
        )


class AsyncAboutResourceWithRawResponse:
    def __init__(self, about: AsyncAboutResource) -> None:
        self._about = about

        self.retrieve_info = async_to_raw_response_wrapper(
            about.retrieve_info,
        )
        self.retrieve_user = async_to_raw_response_wrapper(
            about.retrieve_user,
        )


class AboutResourceWithStreamingResponse:
    def __init__(self, about: AboutResource) -> None:
        self._about = about

        self.retrieve_info = to_streamed_response_wrapper(
            about.retrieve_info,
        )
        self.retrieve_user = to_streamed_response_wrapper(
            about.retrieve_user,
        )


class AsyncAboutResourceWithStreamingResponse:
    def __init__(self, about: AsyncAboutResource) -> None:
        self._about = about

        self.retrieve_info = async_to_streamed_response_wrapper(
            about.retrieve_info,
        )
        self.retrieve_user = async_to_streamed_response_wrapper(
            about.retrieve_user,
        )
