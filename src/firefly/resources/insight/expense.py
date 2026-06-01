# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
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
from ..._base_client import make_request_options
from ...types.insight import (
    expense_get_total_params,
    expense_list_by_tag_params,
    expense_list_by_bill_params,
    expense_list_by_budget_params,
    expense_list_by_category_params,
    expense_list_without_tag_params,
    expense_list_without_bill_params,
    expense_list_without_budget_params,
    expense_list_by_asset_account_params,
    expense_list_without_category_params,
    expense_list_by_expense_account_params,
)
from ...types.insight.expense_get_total_response import ExpenseGetTotalResponse
from ...types.insight.expense_list_by_tag_response import ExpenseListByTagResponse
from ...types.insight.expense_list_by_bill_response import ExpenseListByBillResponse
from ...types.insight.expense_list_by_budget_response import ExpenseListByBudgetResponse
from ...types.insight.expense_list_by_category_response import ExpenseListByCategoryResponse
from ...types.insight.expense_list_without_tag_response import ExpenseListWithoutTagResponse
from ...types.insight.expense_list_without_bill_response import ExpenseListWithoutBillResponse
from ...types.insight.expense_list_without_budget_response import ExpenseListWithoutBudgetResponse
from ...types.insight.expense_list_by_asset_account_response import ExpenseListByAssetAccountResponse
from ...types.insight.expense_list_without_category_response import ExpenseListWithoutCategoryResponse
from ...types.insight.expense_list_by_expense_account_response import ExpenseListByExpenseAccountResponse

__all__ = ["ExpenseResource", "AsyncExpenseResource"]


class ExpenseResource(SyncAPIResource):
    """
    The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
    """

    @cached_property
    def with_raw_response(self) -> ExpenseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return ExpenseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpenseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return ExpenseResourceWithStreamingResponse(self)

    def get_total(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseGetTotalResponse:
        """
        This endpoint gives a sum of the total expenses made by the user.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/total",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_get_total_params.ExpenseGetTotalParams,
                ),
            ),
            cast_to=ExpenseGetTotalResponse,
        )

    def list_by_asset_account(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByAssetAccountResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by asset
        account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/asset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_by_asset_account_params.ExpenseListByAssetAccountParams,
                ),
            ),
            cast_to=ExpenseListByAssetAccountResponse,
        )

    def list_by_bill(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        bills: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByBillResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        bill.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          bills: The bills to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/bill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "bills": bills,
                    },
                    expense_list_by_bill_params.ExpenseListByBillParams,
                ),
            ),
            cast_to=ExpenseListByBillResponse,
        )

    def list_by_budget(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        budgets: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByBudgetResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        budget.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          budgets: The budgets to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/budget",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "budgets": budgets,
                    },
                    expense_list_by_budget_params.ExpenseListByBudgetParams,
                ),
            ),
            cast_to=ExpenseListByBudgetResponse,
        )

    def list_by_category(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        categories: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByCategoryResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          categories: The categories to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "categories": categories,
                    },
                    expense_list_by_category_params.ExpenseListByCategoryParams,
                ),
            ),
            cast_to=ExpenseListByCategoryResponse,
        )

    def list_by_expense_account(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByExpenseAccountResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by
        expense account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you add the accounts ID's of
              expense accounts, only those accounts are included in the results. If you
              include ID's of asset accounts or liabilities, only withdrawals from those asset
              accounts / liabilities will be included. You can combine both asset / liability
              and expense account ID's. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/expense",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_by_expense_account_params.ExpenseListByExpenseAccountParams,
                ),
            ),
            cast_to=ExpenseListByExpenseAccountResponse,
        )

    def list_by_tag(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        tags: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByTagResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          tags: The tags to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/tag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "tags": tags,
                    },
                    expense_list_by_tag_params.ExpenseListByTagParams,
                ),
            ),
            cast_to=ExpenseListByTagResponse,
        )

    def list_without_bill(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutBillResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no bill.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/no-bill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_bill_params.ExpenseListWithoutBillParams,
                ),
            ),
            cast_to=ExpenseListWithoutBillResponse,
        )

    def list_without_budget(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutBudgetResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no budget.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/no-budget",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_budget_params.ExpenseListWithoutBudgetParams,
                ),
            ),
            cast_to=ExpenseListWithoutBudgetResponse,
        )

    def list_without_category(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutCategoryResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/no-category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_category_params.ExpenseListWithoutCategoryParams,
                ),
            ),
            cast_to=ExpenseListWithoutCategoryResponse,
        )

    def list_without_tag(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutTagResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/expense/no-tag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_tag_params.ExpenseListWithoutTagParams,
                ),
            ),
            cast_to=ExpenseListWithoutTagResponse,
        )


class AsyncExpenseResource(AsyncAPIResource):
    """
    The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
    """

    @cached_property
    def with_raw_response(self) -> AsyncExpenseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpenseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpenseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncExpenseResourceWithStreamingResponse(self)

    async def get_total(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseGetTotalResponse:
        """
        This endpoint gives a sum of the total expenses made by the user.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/total",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_get_total_params.ExpenseGetTotalParams,
                ),
            ),
            cast_to=ExpenseGetTotalResponse,
        )

    async def list_by_asset_account(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByAssetAccountResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by asset
        account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/asset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_by_asset_account_params.ExpenseListByAssetAccountParams,
                ),
            ),
            cast_to=ExpenseListByAssetAccountResponse,
        )

    async def list_by_bill(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        bills: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByBillResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        bill.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          bills: The bills to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/bill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "bills": bills,
                    },
                    expense_list_by_bill_params.ExpenseListByBillParams,
                ),
            ),
            cast_to=ExpenseListByBillResponse,
        )

    async def list_by_budget(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        budgets: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByBudgetResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        budget.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          budgets: The budgets to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/budget",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "budgets": budgets,
                    },
                    expense_list_by_budget_params.ExpenseListByBudgetParams,
                ),
            ),
            cast_to=ExpenseListByBudgetResponse,
        )

    async def list_by_category(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        categories: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByCategoryResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          categories: The categories to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "categories": categories,
                    },
                    expense_list_by_category_params.ExpenseListByCategoryParams,
                ),
            ),
            cast_to=ExpenseListByCategoryResponse,
        )

    async def list_by_expense_account(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByExpenseAccountResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by
        expense account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you add the accounts ID's of
              expense accounts, only those accounts are included in the results. If you
              include ID's of asset accounts or liabilities, only withdrawals from those asset
              accounts / liabilities will be included. You can combine both asset / liability
              and expense account ID's. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/expense",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_by_expense_account_params.ExpenseListByExpenseAccountParams,
                ),
            ),
            cast_to=ExpenseListByExpenseAccountResponse,
        )

    async def list_by_tag(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        tags: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListByTagResponse:
        """
        This endpoint gives a summary of the expenses made by the user, grouped by (any)
        tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          tags: The tags to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/tag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                        "tags": tags,
                    },
                    expense_list_by_tag_params.ExpenseListByTagParams,
                ),
            ),
            cast_to=ExpenseListByTagResponse,
        )

    async def list_without_bill(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutBillResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no bill.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/no-bill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_bill_params.ExpenseListWithoutBillParams,
                ),
            ),
            cast_to=ExpenseListWithoutBillResponse,
        )

    async def list_without_budget(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutBudgetResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no budget.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/no-budget",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_budget_params.ExpenseListWithoutBudgetParams,
                ),
            ),
            cast_to=ExpenseListWithoutBudgetResponse,
        )

    async def list_without_category(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutCategoryResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/no-category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_category_params.ExpenseListWithoutCategoryParams,
                ),
            ),
            cast_to=ExpenseListWithoutCategoryResponse,
        )

    async def list_without_tag(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpenseListWithoutTagResponse:
        """
        This endpoint gives a summary of the expenses made by the user, including only
        expenses with no tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only withdrawals from those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/expense/no-tag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "accounts": accounts,
                    },
                    expense_list_without_tag_params.ExpenseListWithoutTagParams,
                ),
            ),
            cast_to=ExpenseListWithoutTagResponse,
        )


class ExpenseResourceWithRawResponse:
    def __init__(self, expense: ExpenseResource) -> None:
        self._expense = expense

        self.get_total = to_raw_response_wrapper(
            expense.get_total,
        )
        self.list_by_asset_account = to_raw_response_wrapper(
            expense.list_by_asset_account,
        )
        self.list_by_bill = to_raw_response_wrapper(
            expense.list_by_bill,
        )
        self.list_by_budget = to_raw_response_wrapper(
            expense.list_by_budget,
        )
        self.list_by_category = to_raw_response_wrapper(
            expense.list_by_category,
        )
        self.list_by_expense_account = to_raw_response_wrapper(
            expense.list_by_expense_account,
        )
        self.list_by_tag = to_raw_response_wrapper(
            expense.list_by_tag,
        )
        self.list_without_bill = to_raw_response_wrapper(
            expense.list_without_bill,
        )
        self.list_without_budget = to_raw_response_wrapper(
            expense.list_without_budget,
        )
        self.list_without_category = to_raw_response_wrapper(
            expense.list_without_category,
        )
        self.list_without_tag = to_raw_response_wrapper(
            expense.list_without_tag,
        )


class AsyncExpenseResourceWithRawResponse:
    def __init__(self, expense: AsyncExpenseResource) -> None:
        self._expense = expense

        self.get_total = async_to_raw_response_wrapper(
            expense.get_total,
        )
        self.list_by_asset_account = async_to_raw_response_wrapper(
            expense.list_by_asset_account,
        )
        self.list_by_bill = async_to_raw_response_wrapper(
            expense.list_by_bill,
        )
        self.list_by_budget = async_to_raw_response_wrapper(
            expense.list_by_budget,
        )
        self.list_by_category = async_to_raw_response_wrapper(
            expense.list_by_category,
        )
        self.list_by_expense_account = async_to_raw_response_wrapper(
            expense.list_by_expense_account,
        )
        self.list_by_tag = async_to_raw_response_wrapper(
            expense.list_by_tag,
        )
        self.list_without_bill = async_to_raw_response_wrapper(
            expense.list_without_bill,
        )
        self.list_without_budget = async_to_raw_response_wrapper(
            expense.list_without_budget,
        )
        self.list_without_category = async_to_raw_response_wrapper(
            expense.list_without_category,
        )
        self.list_without_tag = async_to_raw_response_wrapper(
            expense.list_without_tag,
        )


class ExpenseResourceWithStreamingResponse:
    def __init__(self, expense: ExpenseResource) -> None:
        self._expense = expense

        self.get_total = to_streamed_response_wrapper(
            expense.get_total,
        )
        self.list_by_asset_account = to_streamed_response_wrapper(
            expense.list_by_asset_account,
        )
        self.list_by_bill = to_streamed_response_wrapper(
            expense.list_by_bill,
        )
        self.list_by_budget = to_streamed_response_wrapper(
            expense.list_by_budget,
        )
        self.list_by_category = to_streamed_response_wrapper(
            expense.list_by_category,
        )
        self.list_by_expense_account = to_streamed_response_wrapper(
            expense.list_by_expense_account,
        )
        self.list_by_tag = to_streamed_response_wrapper(
            expense.list_by_tag,
        )
        self.list_without_bill = to_streamed_response_wrapper(
            expense.list_without_bill,
        )
        self.list_without_budget = to_streamed_response_wrapper(
            expense.list_without_budget,
        )
        self.list_without_category = to_streamed_response_wrapper(
            expense.list_without_category,
        )
        self.list_without_tag = to_streamed_response_wrapper(
            expense.list_without_tag,
        )


class AsyncExpenseResourceWithStreamingResponse:
    def __init__(self, expense: AsyncExpenseResource) -> None:
        self._expense = expense

        self.get_total = async_to_streamed_response_wrapper(
            expense.get_total,
        )
        self.list_by_asset_account = async_to_streamed_response_wrapper(
            expense.list_by_asset_account,
        )
        self.list_by_bill = async_to_streamed_response_wrapper(
            expense.list_by_bill,
        )
        self.list_by_budget = async_to_streamed_response_wrapper(
            expense.list_by_budget,
        )
        self.list_by_category = async_to_streamed_response_wrapper(
            expense.list_by_category,
        )
        self.list_by_expense_account = async_to_streamed_response_wrapper(
            expense.list_by_expense_account,
        )
        self.list_by_tag = async_to_streamed_response_wrapper(
            expense.list_by_tag,
        )
        self.list_without_bill = async_to_streamed_response_wrapper(
            expense.list_without_bill,
        )
        self.list_without_budget = async_to_streamed_response_wrapper(
            expense.list_without_budget,
        )
        self.list_without_category = async_to_streamed_response_wrapper(
            expense.list_without_category,
        )
        self.list_without_tag = async_to_streamed_response_wrapper(
            expense.list_without_tag,
        )
