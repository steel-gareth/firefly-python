# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chart import budget_retrieve_overview_params
from ..._base_client import make_request_options
from ...types.chart.budget_retrieve_overview_response import BudgetRetrieveOverviewResponse

__all__ = ["BudgetResource", "AsyncBudgetResource"]


class BudgetResource(SyncAPIResource):
    """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""

    @cached_property
    def with_raw_response(self) -> BudgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return BudgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BudgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return BudgetResourceWithStreamingResponse(self)

    def retrieve_overview(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetRetrieveOverviewResponse:
        """
        This endpoint returns the data required to generate a chart with basic budget
        information.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/chart/budget/overview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    budget_retrieve_overview_params.BudgetRetrieveOverviewParams,
                ),
            ),
            cast_to=BudgetRetrieveOverviewResponse,
        )


class AsyncBudgetResource(AsyncAPIResource):
    """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""

    @cached_property
    def with_raw_response(self) -> AsyncBudgetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBudgetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBudgetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncBudgetResourceWithStreamingResponse(self)

    async def retrieve_overview(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetRetrieveOverviewResponse:
        """
        This endpoint returns the data required to generate a chart with basic budget
        information.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/chart/budget/overview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    budget_retrieve_overview_params.BudgetRetrieveOverviewParams,
                ),
            ),
            cast_to=BudgetRetrieveOverviewResponse,
        )


class BudgetResourceWithRawResponse:
    def __init__(self, budget: BudgetResource) -> None:
        self._budget = budget

        self.retrieve_overview = to_raw_response_wrapper(
            budget.retrieve_overview,
        )


class AsyncBudgetResourceWithRawResponse:
    def __init__(self, budget: AsyncBudgetResource) -> None:
        self._budget = budget

        self.retrieve_overview = async_to_raw_response_wrapper(
            budget.retrieve_overview,
        )


class BudgetResourceWithStreamingResponse:
    def __init__(self, budget: BudgetResource) -> None:
        self._budget = budget

        self.retrieve_overview = to_streamed_response_wrapper(
            budget.retrieve_overview,
        )


class AsyncBudgetResourceWithStreamingResponse:
    def __init__(self, budget: AsyncBudgetResource) -> None:
        self._budget = budget

        self.retrieve_overview = async_to_streamed_response_wrapper(
            budget.retrieve_overview,
        )
