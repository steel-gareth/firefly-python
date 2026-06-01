# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from .limits import (
    LimitsResource,
    AsyncLimitsResource,
    LimitsResourceWithRawResponse,
    AsyncLimitsResourceWithRawResponse,
    LimitsResourceWithStreamingResponse,
    AsyncLimitsResourceWithStreamingResponse,
)
from ...types import (
    AutoBudgetType,
    AutoBudgetPeriod,
    TransactionTypeFilter,
    budget_list_params,
    budget_create_params,
    budget_update_params,
    budget_retrieve_params,
    budget_list_attachments_params,
    budget_list_transactions_params,
    budget_list_transactions_without_budget_params,
)
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
from ...types.budget_single import BudgetSingle
from ...types.attachment_array import AttachmentArray
from ...types.auto_budget_type import AutoBudgetType
from ...types.transaction_array import TransactionArray
from ...types.auto_budget_period import AutoBudgetPeriod
from ...types.budget_list_response import BudgetListResponse
from ...types.transaction_type_filter import TransactionTypeFilter

__all__ = ["BudgetsResource", "AsyncBudgetsResource"]


class BudgetsResource(SyncAPIResource):
    """
    Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
    """

    @cached_property
    def limits(self) -> LimitsResource:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        return LimitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BudgetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return BudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BudgetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return BudgetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        active: bool | Omit = omit,
        auto_budget_amount: Optional[str] | Omit = omit,
        auto_budget_currency_code: Optional[str] | Omit = omit,
        auto_budget_currency_id: Optional[str] | Omit = omit,
        auto_budget_period: Optional[AutoBudgetPeriod] | Omit = omit,
        auto_budget_type: Optional[AutoBudgetType] | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetSingle:
        """Creates a new budget.

        The data required can be submitted as a JSON body or as a
        list of parameters.

        Args:
          auto_budget_currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_period: Period for the auto budget

          auto_budget_type: The type of auto-budget that Firefly III must create.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/budgets",
            body=maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "auto_budget_amount": auto_budget_amount,
                    "auto_budget_currency_code": auto_budget_currency_code,
                    "auto_budget_currency_id": auto_budget_currency_id,
                    "auto_budget_period": auto_budget_period,
                    "auto_budget_type": auto_budget_type,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetSingle,
        )

    def retrieve(
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
    ) -> BudgetSingle:
        """Get a single budget.

        If the start date and end date are submitted as well, the
        "spent" array will be updated accordingly.

        Args:
          end: A date formatted YYYY-MM-DD, to get info on how much the user has spent.

          start: A date formatted YYYY-MM-DD, to get info on how much the user has spent.

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
            path_template("/v1/budgets/{id}", id=id),
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
                    budget_retrieve_params.BudgetRetrieveParams,
                ),
            ),
            cast_to=BudgetSingle,
        )

    def update(
        self,
        id: str,
        *,
        name: str,
        active: bool | Omit = omit,
        auto_budget_amount: Optional[str] | Omit = omit,
        auto_budget_currency_code: Optional[str] | Omit = omit,
        auto_budget_currency_id: Optional[str] | Omit = omit,
        auto_budget_period: Optional[AutoBudgetPeriod] | Omit = omit,
        auto_budget_type: Optional[AutoBudgetType] | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetSingle:
        """Update existing budget.

        This endpoint cannot be used to set budget amount
        limits.

        Args:
          auto_budget_currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_period: Period for the auto budget

          auto_budget_type: The type of auto-budget that Firefly III must create.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._put(
            path_template("/v1/budgets/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "auto_budget_amount": auto_budget_amount,
                    "auto_budget_currency_code": auto_budget_currency_code,
                    "auto_budget_currency_id": auto_budget_currency_id,
                    "auto_budget_period": auto_budget_period,
                    "auto_budget_type": auto_budget_type,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                    "order": order,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetSingle,
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
    ) -> BudgetListResponse:
        """List all the budgets the user has made.

        If the start date and end date are
        submitted as well, the "spent" array will be updated accordingly.

        Args:
          end: A date formatted YYYY-MM-DD, to get info on how much the user has spent. You
              must submit both start and end.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD, to get info on how much the user has spent. You
              must submit both start and end.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/budgets",
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
                    budget_list_params.BudgetListParams,
                ),
            ),
            cast_to=BudgetListResponse,
        )

    def delete(
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
    ) -> None:
        """Delete a budget.

        Transactions will not be deleted.

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
            path_template("/v1/budgets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_attachments(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentArray:
        """Lists all attachments.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

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
            path_template("/v1/budgets/{id}/attachments", id=id),
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
                    budget_list_attachments_params.BudgetListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    def list_transactions(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        Get all transactions linked to a budget, possibly limited by start and end

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/budgets/{id}/transactions", id=id),
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
                        "type": type,
                    },
                    budget_list_transactions_params.BudgetListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    def list_transactions_without_budget(
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
    ) -> TransactionArray:
        """
        Get all transactions NOT linked to a budget, possibly limited by start and end

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
            "/v1/budgets/transactions-without-budget",
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
                    budget_list_transactions_without_budget_params.BudgetListTransactionsWithoutBudgetParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncBudgetsResource(AsyncAPIResource):
    """
    Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
    """

    @cached_property
    def limits(self) -> AsyncLimitsResource:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        return AsyncLimitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBudgetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBudgetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncBudgetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        active: bool | Omit = omit,
        auto_budget_amount: Optional[str] | Omit = omit,
        auto_budget_currency_code: Optional[str] | Omit = omit,
        auto_budget_currency_id: Optional[str] | Omit = omit,
        auto_budget_period: Optional[AutoBudgetPeriod] | Omit = omit,
        auto_budget_type: Optional[AutoBudgetType] | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetSingle:
        """Creates a new budget.

        The data required can be submitted as a JSON body or as a
        list of parameters.

        Args:
          auto_budget_currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_period: Period for the auto budget

          auto_budget_type: The type of auto-budget that Firefly III must create.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/budgets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "auto_budget_amount": auto_budget_amount,
                    "auto_budget_currency_code": auto_budget_currency_code,
                    "auto_budget_currency_id": auto_budget_currency_id,
                    "auto_budget_period": auto_budget_period,
                    "auto_budget_type": auto_budget_type,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetSingle,
        )

    async def retrieve(
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
    ) -> BudgetSingle:
        """Get a single budget.

        If the start date and end date are submitted as well, the
        "spent" array will be updated accordingly.

        Args:
          end: A date formatted YYYY-MM-DD, to get info on how much the user has spent.

          start: A date formatted YYYY-MM-DD, to get info on how much the user has spent.

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
            path_template("/v1/budgets/{id}", id=id),
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
                    budget_retrieve_params.BudgetRetrieveParams,
                ),
            ),
            cast_to=BudgetSingle,
        )

    async def update(
        self,
        id: str,
        *,
        name: str,
        active: bool | Omit = omit,
        auto_budget_amount: Optional[str] | Omit = omit,
        auto_budget_currency_code: Optional[str] | Omit = omit,
        auto_budget_currency_id: Optional[str] | Omit = omit,
        auto_budget_period: Optional[AutoBudgetPeriod] | Omit = omit,
        auto_budget_type: Optional[AutoBudgetType] | Omit = omit,
        fire_webhooks: bool | Omit = omit,
        notes: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BudgetSingle:
        """Update existing budget.

        This endpoint cannot be used to set budget amount
        limits.

        Args:
          auto_budget_currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          auto_budget_period: Period for the auto budget

          auto_budget_type: The type of auto-budget that Firefly III must create.

          fire_webhooks: Whether or not to fire the webhooks that are related to this event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._put(
            path_template("/v1/budgets/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "auto_budget_amount": auto_budget_amount,
                    "auto_budget_currency_code": auto_budget_currency_code,
                    "auto_budget_currency_id": auto_budget_currency_id,
                    "auto_budget_period": auto_budget_period,
                    "auto_budget_type": auto_budget_type,
                    "fire_webhooks": fire_webhooks,
                    "notes": notes,
                    "order": order,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetSingle,
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
    ) -> BudgetListResponse:
        """List all the budgets the user has made.

        If the start date and end date are
        submitted as well, the "spent" array will be updated accordingly.

        Args:
          end: A date formatted YYYY-MM-DD, to get info on how much the user has spent. You
              must submit both start and end.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD, to get info on how much the user has spent. You
              must submit both start and end.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/budgets",
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
                    budget_list_params.BudgetListParams,
                ),
            ),
            cast_to=BudgetListResponse,
        )

    async def delete(
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
    ) -> None:
        """Delete a budget.

        Transactions will not be deleted.

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
            path_template("/v1/budgets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_attachments(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentArray:
        """Lists all attachments.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

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
            path_template("/v1/budgets/{id}/attachments", id=id),
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
                    budget_list_attachments_params.BudgetListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    async def list_transactions(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        Get all transactions linked to a budget, possibly limited by start and end

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/budgets/{id}/transactions", id=id),
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
                        "type": type,
                    },
                    budget_list_transactions_params.BudgetListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    async def list_transactions_without_budget(
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
    ) -> TransactionArray:
        """
        Get all transactions NOT linked to a budget, possibly limited by start and end

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
            "/v1/budgets/transactions-without-budget",
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
                    budget_list_transactions_without_budget_params.BudgetListTransactionsWithoutBudgetParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class BudgetsResourceWithRawResponse:
    def __init__(self, budgets: BudgetsResource) -> None:
        self._budgets = budgets

        self.create = to_raw_response_wrapper(
            budgets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            budgets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            budgets.update,
        )
        self.list = to_raw_response_wrapper(
            budgets.list,
        )
        self.delete = to_raw_response_wrapper(
            budgets.delete,
        )
        self.list_attachments = to_raw_response_wrapper(
            budgets.list_attachments,
        )
        self.list_transactions = to_raw_response_wrapper(
            budgets.list_transactions,
        )
        self.list_transactions_without_budget = to_raw_response_wrapper(
            budgets.list_transactions_without_budget,
        )

    @cached_property
    def limits(self) -> LimitsResourceWithRawResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        return LimitsResourceWithRawResponse(self._budgets.limits)


class AsyncBudgetsResourceWithRawResponse:
    def __init__(self, budgets: AsyncBudgetsResource) -> None:
        self._budgets = budgets

        self.create = async_to_raw_response_wrapper(
            budgets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            budgets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            budgets.update,
        )
        self.list = async_to_raw_response_wrapper(
            budgets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            budgets.delete,
        )
        self.list_attachments = async_to_raw_response_wrapper(
            budgets.list_attachments,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            budgets.list_transactions,
        )
        self.list_transactions_without_budget = async_to_raw_response_wrapper(
            budgets.list_transactions_without_budget,
        )

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithRawResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        return AsyncLimitsResourceWithRawResponse(self._budgets.limits)


class BudgetsResourceWithStreamingResponse:
    def __init__(self, budgets: BudgetsResource) -> None:
        self._budgets = budgets

        self.create = to_streamed_response_wrapper(
            budgets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            budgets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            budgets.update,
        )
        self.list = to_streamed_response_wrapper(
            budgets.list,
        )
        self.delete = to_streamed_response_wrapper(
            budgets.delete,
        )
        self.list_attachments = to_streamed_response_wrapper(
            budgets.list_attachments,
        )
        self.list_transactions = to_streamed_response_wrapper(
            budgets.list_transactions,
        )
        self.list_transactions_without_budget = to_streamed_response_wrapper(
            budgets.list_transactions_without_budget,
        )

    @cached_property
    def limits(self) -> LimitsResourceWithStreamingResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        return LimitsResourceWithStreamingResponse(self._budgets.limits)


class AsyncBudgetsResourceWithStreamingResponse:
    def __init__(self, budgets: AsyncBudgetsResource) -> None:
        self._budgets = budgets

        self.create = async_to_streamed_response_wrapper(
            budgets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            budgets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            budgets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            budgets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            budgets.delete,
        )
        self.list_attachments = async_to_streamed_response_wrapper(
            budgets.list_attachments,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            budgets.list_transactions,
        )
        self.list_transactions_without_budget = async_to_streamed_response_wrapper(
            budgets.list_transactions_without_budget,
        )

    @cached_property
    def limits(self) -> AsyncLimitsResourceWithStreamingResponse:
        """
        Endpoints to manage a user&#039;s budgets and get info on the related objects, like limits.
        """
        return AsyncLimitsResourceWithStreamingResponse(self._budgets.limits)
