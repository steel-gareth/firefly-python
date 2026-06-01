# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.currency_single import CurrencySingle

__all__ = ["PrimaryResource", "AsyncPrimaryResource"]


class PrimaryResource(SyncAPIResource):
    """Endpoints to manage the currencies in Firefly III.

    Depending on the user&#039;s role you can also disable and enable them, or add new ones.
    """

    @cached_property
    def with_raw_response(self) -> PrimaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return PrimaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrimaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return PrimaryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """Get the primary currency of the current administration.

        This replaces what was
        called "the user's default currency" although they are essentially the same.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/currencies/primary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    def make_primary(
        self,
        code: str,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """Make this currency the primary currency for the current financial
        administration.

        If the currency is not enabled, it will be enabled as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/currencies/{code}/primary", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )


class AsyncPrimaryResource(AsyncAPIResource):
    """Endpoints to manage the currencies in Firefly III.

    Depending on the user&#039;s role you can also disable and enable them, or add new ones.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPrimaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrimaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrimaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncPrimaryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """Get the primary currency of the current administration.

        This replaces what was
        called "the user's default currency" although they are essentially the same.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/currencies/primary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    async def make_primary(
        self,
        code: str,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """Make this currency the primary currency for the current financial
        administration.

        If the currency is not enabled, it will be enabled as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/currencies/{code}/primary", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )


class PrimaryResourceWithRawResponse:
    def __init__(self, primary: PrimaryResource) -> None:
        self._primary = primary

        self.retrieve = to_raw_response_wrapper(
            primary.retrieve,
        )
        self.make_primary = to_raw_response_wrapper(
            primary.make_primary,
        )


class AsyncPrimaryResourceWithRawResponse:
    def __init__(self, primary: AsyncPrimaryResource) -> None:
        self._primary = primary

        self.retrieve = async_to_raw_response_wrapper(
            primary.retrieve,
        )
        self.make_primary = async_to_raw_response_wrapper(
            primary.make_primary,
        )


class PrimaryResourceWithStreamingResponse:
    def __init__(self, primary: PrimaryResource) -> None:
        self._primary = primary

        self.retrieve = to_streamed_response_wrapper(
            primary.retrieve,
        )
        self.make_primary = to_streamed_response_wrapper(
            primary.make_primary,
        )


class AsyncPrimaryResourceWithStreamingResponse:
    def __init__(self, primary: AsyncPrimaryResource) -> None:
        self._primary = primary

        self.retrieve = async_to_streamed_response_wrapper(
            primary.retrieve,
        )
        self.make_primary = async_to_streamed_response_wrapper(
            primary.make_primary,
        )
