# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date, datetime

import httpx

from ...types import TransactionTypeFilter
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.budgets import (
    limit_create_params,
    limit_list_0_params,
    limit_list_1_params,
    limit_update_params,
    limit_list_transactions_params,
)
from ...types.transaction_array import TransactionArray
from ...types.transaction_type_filter import TransactionTypeFilter
from ...types.budgets.budget_limit_array import BudgetLimitArray
from ...types.budgets.budget_limit_single import BudgetLimitSingle

__all__ = ["LimitsResource", "AsyncLimitsResource"]


class LimitsResource(SyncAPIResource):
    """
    Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
    """

    @cached_property
    def with_raw_response(self) -> LimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return LimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return LimitsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        amount: str,
        end: Union[str, date],
        start: Union[str, date],
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitSingle:
        """
        Store a new budget limit under this budget.

        Args:
          end: End date of the budget limit.

          start: Start date of the budget limit.

          currency_code: Use either currency_id or currency_code. Defaults to the user's primary
              currency.

          currency_id: Use either currency_id or currency_code. Defaults to the user's primary
              currency.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          notes: Some notes for this specific budget limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/budgets/{id}/limits", id=id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "end": end,
                    "start": start,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                },
                limit_create_params.LimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetLimitSingle,
        )

    def retrieve(
        self,
        limit_id: int,
        *,
        id: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitSingle:
        """
        Get single budget limit.

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
            path_template("/v1/budgets/{id}/limits/{limit_id}", id=id, limit_id=limit_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetLimitSingle,
        )

    def update(
        self,
        limit_id: str,
        *,
        id: str,
        amount: str | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        currency_name: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitSingle:
        """
        Update existing budget limit.

        Args:
          currency_code: The currency code of the currency associated with this object.

          currency_id: The currency ID of the currency associated with this object.

          currency_name: The currency name of the currency associated with this object.

          end: End date of the budget limit.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          notes: Some notes for this specific budget limit.

          start: Start date of the budget limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not limit_id:
            raise ValueError(f"Expected a non-empty value for `limit_id` but received {limit_id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._put(
            path_template("/v1/budgets/{id}/limits/{limit_id}", id=id, limit_id=limit_id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "currency_name": currency_name,
                    "end": end,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                    "start": start,
                },
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetLimitSingle,
        )

    def delete(
        self,
        limit_id: str,
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
        """
        Delete a budget limit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not limit_id:
            raise ValueError(f"Expected a non-empty value for `limit_id` but received {limit_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/budgets/{id}/limits/{limit_id}", id=id, limit_id=limit_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_0(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitArray:
        """Get all budget limits for this budget and the money spent, and money left.

        You
        can limit the list by submitting a date range as well. The "spent" array for
        each budget limit is NOT influenced by the start and end date of your query, but
        by the start and end date of the budget limit itself.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

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
            path_template("/v1/budgets/{id}/limits", id=id),
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
                    limit_list_0_params.LimitList0Params,
                ),
            ),
            cast_to=BudgetLimitArray,
        )

    def list_1(
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
    ) -> BudgetLimitArray:
        """
        Get all budget limits for for this date range.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/budget-limits",
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
                    limit_list_1_params.LimitList1Params,
                ),
            ),
            cast_to=BudgetLimitArray,
        )

    def list_transactions(
        self,
        limit_id: str,
        *,
        id: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """List all the transactions within one budget limit.

        The start and end date are
        dictated by the budget limit.

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
        if not limit_id:
            raise ValueError(f"Expected a non-empty value for `limit_id` but received {limit_id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/budgets/{id}/limits/{limit_id}/transactions", id=id, limit_id=limit_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "type": type,
                    },
                    limit_list_transactions_params.LimitListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncLimitsResource(AsyncAPIResource):
    """
    Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
    """

    @cached_property
    def with_raw_response(self) -> AsyncLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncLimitsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        amount: str,
        end: Union[str, date],
        start: Union[str, date],
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitSingle:
        """
        Store a new budget limit under this budget.

        Args:
          end: End date of the budget limit.

          start: Start date of the budget limit.

          currency_code: Use either currency_id or currency_code. Defaults to the user's primary
              currency.

          currency_id: Use either currency_id or currency_code. Defaults to the user's primary
              currency.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          notes: Some notes for this specific budget limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/budgets/{id}/limits", id=id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "end": end,
                    "start": start,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                },
                limit_create_params.LimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetLimitSingle,
        )

    async def retrieve(
        self,
        limit_id: int,
        *,
        id: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitSingle:
        """
        Get single budget limit.

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
            path_template("/v1/budgets/{id}/limits/{limit_id}", id=id, limit_id=limit_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetLimitSingle,
        )

    async def update(
        self,
        limit_id: str,
        *,
        id: str,
        amount: str | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        currency_name: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitSingle:
        """
        Update existing budget limit.

        Args:
          currency_code: The currency code of the currency associated with this object.

          currency_id: The currency ID of the currency associated with this object.

          currency_name: The currency name of the currency associated with this object.

          end: End date of the budget limit.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          notes: Some notes for this specific budget limit.

          start: Start date of the budget limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not limit_id:
            raise ValueError(f"Expected a non-empty value for `limit_id` but received {limit_id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._put(
            path_template("/v1/budgets/{id}/limits/{limit_id}", id=id, limit_id=limit_id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "currency_name": currency_name,
                    "end": end,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                    "start": start,
                },
                limit_update_params.LimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetLimitSingle,
        )

    async def delete(
        self,
        limit_id: str,
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
        """
        Delete a budget limit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not limit_id:
            raise ValueError(f"Expected a non-empty value for `limit_id` but received {limit_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/budgets/{id}/limits/{limit_id}", id=id, limit_id=limit_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_0(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetLimitArray:
        """Get all budget limits for this budget and the money spent, and money left.

        You
        can limit the list by submitting a date range as well. The "spent" array for
        each budget limit is NOT influenced by the start and end date of your query, but
        by the start and end date of the budget limit itself.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

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
            path_template("/v1/budgets/{id}/limits", id=id),
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
                    limit_list_0_params.LimitList0Params,
                ),
            ),
            cast_to=BudgetLimitArray,
        )

    async def list_1(
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
    ) -> BudgetLimitArray:
        """
        Get all budget limits for for this date range.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/budget-limits",
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
                    limit_list_1_params.LimitList1Params,
                ),
            ),
            cast_to=BudgetLimitArray,
        )

    async def list_transactions(
        self,
        limit_id: str,
        *,
        id: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """List all the transactions within one budget limit.

        The start and end date are
        dictated by the budget limit.

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
        if not limit_id:
            raise ValueError(f"Expected a non-empty value for `limit_id` but received {limit_id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/budgets/{id}/limits/{limit_id}/transactions", id=id, limit_id=limit_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "type": type,
                    },
                    limit_list_transactions_params.LimitListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class LimitsResourceWithRawResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.create = to_raw_response_wrapper(
            limits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            limits.retrieve,
        )
        self.update = to_raw_response_wrapper(
            limits.update,
        )
        self.delete = to_raw_response_wrapper(
            limits.delete,
        )
        self.list_0 = to_raw_response_wrapper(
            limits.list_0,
        )
        self.list_1 = to_raw_response_wrapper(
            limits.list_1,
        )
        self.list_transactions = to_raw_response_wrapper(
            limits.list_transactions,
        )


class AsyncLimitsResourceWithRawResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.create = async_to_raw_response_wrapper(
            limits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            limits.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            limits.update,
        )
        self.delete = async_to_raw_response_wrapper(
            limits.delete,
        )
        self.list_0 = async_to_raw_response_wrapper(
            limits.list_0,
        )
        self.list_1 = async_to_raw_response_wrapper(
            limits.list_1,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            limits.list_transactions,
        )


class LimitsResourceWithStreamingResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.create = to_streamed_response_wrapper(
            limits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            limits.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            limits.update,
        )
        self.delete = to_streamed_response_wrapper(
            limits.delete,
        )
        self.list_0 = to_streamed_response_wrapper(
            limits.list_0,
        )
        self.list_1 = to_streamed_response_wrapper(
            limits.list_1,
        )
        self.list_transactions = to_streamed_response_wrapper(
            limits.list_transactions,
        )


class AsyncLimitsResourceWithStreamingResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.create = async_to_streamed_response_wrapper(
            limits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            limits.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            limits.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            limits.delete,
        )
        self.list_0 = async_to_streamed_response_wrapper(
            limits.list_0,
        )
        self.list_1 = async_to_streamed_response_wrapper(
            limits.list_1,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            limits.list_transactions,
        )
