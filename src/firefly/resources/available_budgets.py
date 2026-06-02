# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import available_budget_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.available_budget_array import AvailableBudgetArray
from ..types.available_budget_retrieve_response import AvailableBudgetRetrieveResponse

__all__ = ["AvailableBudgetsResource", "AsyncAvailableBudgetsResource"]


class AvailableBudgetsResource(SyncAPIResource):
    """
    Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
    """

    @cached_property
    def with_raw_response(self) -> AvailableBudgetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AvailableBudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableBudgetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AvailableBudgetsResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> AvailableBudgetRetrieveResponse:
        """
        Get a single available budget, by ID.

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
            path_template("/v1/available-budgets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailableBudgetRetrieveResponse,
        )

    def list(
        self,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvailableBudgetArray:
        """
        Firefly III calculates the total amount of money budgeted in so-called
        "available budgets". This endpoint returns all of these amounts and the periods
        for which they are calculated.

        Args:
          end: A date formatted YYYY-MM-DD.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/available-budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                    },
                    available_budget_list_params.AvailableBudgetListParams,
                ),
            ),
            cast_to=AvailableBudgetArray,
        )


class AsyncAvailableBudgetsResource(AsyncAPIResource):
    """
    Endpoints to manage the total available amount that the user has made available to themselves. Used in periodic budgeting.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAvailableBudgetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailableBudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableBudgetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncAvailableBudgetsResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> AvailableBudgetRetrieveResponse:
        """
        Get a single available budget, by ID.

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
            path_template("/v1/available-budgets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvailableBudgetRetrieveResponse,
        )

    async def list(
        self,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvailableBudgetArray:
        """
        Firefly III calculates the total amount of money budgeted in so-called
        "available budgets". This endpoint returns all of these amounts and the periods
        for which they are calculated.

        Args:
          end: A date formatted YYYY-MM-DD.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/available-budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                    },
                    available_budget_list_params.AvailableBudgetListParams,
                ),
            ),
            cast_to=AvailableBudgetArray,
        )


class AvailableBudgetsResourceWithRawResponse:
    def __init__(self, available_budgets: AvailableBudgetsResource) -> None:
        self._available_budgets = available_budgets

        self.retrieve = to_raw_response_wrapper(
            available_budgets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            available_budgets.list,
        )


class AsyncAvailableBudgetsResourceWithRawResponse:
    def __init__(self, available_budgets: AsyncAvailableBudgetsResource) -> None:
        self._available_budgets = available_budgets

        self.retrieve = async_to_raw_response_wrapper(
            available_budgets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            available_budgets.list,
        )


class AvailableBudgetsResourceWithStreamingResponse:
    def __init__(self, available_budgets: AvailableBudgetsResource) -> None:
        self._available_budgets = available_budgets

        self.retrieve = to_streamed_response_wrapper(
            available_budgets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            available_budgets.list,
        )


class AsyncAvailableBudgetsResourceWithStreamingResponse:
    def __init__(self, available_budgets: AsyncAvailableBudgetsResource) -> None:
        self._available_budgets = available_budgets

        self.retrieve = async_to_streamed_response_wrapper(
            available_budgets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            available_budgets.list,
        )
