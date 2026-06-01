# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import summary_retrieve_basic_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.summary_retrieve_basic_response import SummaryRetrieveBasicResponse

__all__ = ["SummaryResource", "AsyncSummaryResource"]


class SummaryResource(SyncAPIResource):
    """
    These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
    """

    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return SummaryResourceWithStreamingResponse(self)

    def retrieve_basic(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        currency_code: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryRetrieveBasicResponse:
        """
        Returns basic sums of the users data, like the net worth, spent and earned
        amounts. It is multi-currency, and is used in Firefly III to populate the
        dashboard.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          currency_code: A currency code like EUR or USD, to filter the result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/summary/basic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "currency_code": currency_code,
                    },
                    summary_retrieve_basic_params.SummaryRetrieveBasicParams,
                ),
            ),
            cast_to=SummaryRetrieveBasicResponse,
        )


class AsyncSummaryResource(AsyncAPIResource):
    """
    These endpoints deliver summaries, like sums, lists of numbers and other processed information. Mainly used for the main dashboard and pretty specific for Firefly III itself.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncSummaryResourceWithStreamingResponse(self)

    async def retrieve_basic(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        currency_code: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryRetrieveBasicResponse:
        """
        Returns basic sums of the users data, like the net worth, spent and earned
        amounts. It is multi-currency, and is used in Firefly III to populate the
        dashboard.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          currency_code: A currency code like EUR or USD, to filter the result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/summary/basic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "currency_code": currency_code,
                    },
                    summary_retrieve_basic_params.SummaryRetrieveBasicParams,
                ),
            ),
            cast_to=SummaryRetrieveBasicResponse,
        )


class SummaryResourceWithRawResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.retrieve_basic = to_raw_response_wrapper(
            summary.retrieve_basic,
        )


class AsyncSummaryResourceWithRawResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.retrieve_basic = async_to_raw_response_wrapper(
            summary.retrieve_basic,
        )


class SummaryResourceWithStreamingResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.retrieve_basic = to_streamed_response_wrapper(
            summary.retrieve_basic,
        )


class AsyncSummaryResourceWithStreamingResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.retrieve_basic = async_to_streamed_response_wrapper(
            summary.retrieve_basic,
        )
