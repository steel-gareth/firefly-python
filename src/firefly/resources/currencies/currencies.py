# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import (
    AccountTypeFilter,
    TransactionTypeFilter,
    currency_list_params,
    currency_create_params,
    currency_update_params,
    currency_list_bills_params,
    currency_list_rules_params,
    currency_list_accounts_params,
    currency_list_recurrences_params,
    currency_list_transactions_params,
    currency_list_budget_limits_params,
    currency_list_available_budgets_params,
)
from .primary import (
    PrimaryResource,
    AsyncPrimaryResource,
    PrimaryResourceWithRawResponse,
    AsyncPrimaryResourceWithRawResponse,
    PrimaryResourceWithStreamingResponse,
    AsyncPrimaryResourceWithStreamingResponse,
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
from ...types.bill_array import BillArray
from ...types.rule_array import RuleArray
from ...types.account_array import AccountArray
from ...types.currency_single import CurrencySingle
from ...types.recurrence_array import RecurrenceArray
from ...types.transaction_array import TransactionArray
from ...types.account_type_filter import AccountTypeFilter
from ...types.available_budget_array import AvailableBudgetArray
from ...types.currency_list_response import CurrencyListResponse
from ...types.transaction_type_filter import TransactionTypeFilter
from ...types.budgets.budget_limit_array import BudgetLimitArray

__all__ = ["CurrenciesResource", "AsyncCurrenciesResource"]


class CurrenciesResource(SyncAPIResource):
    """Endpoints to manage the currencies in Firefly III.

    Depending on the user&#039;s role you can also disable and enable them, or add new ones.
    """

    @cached_property
    def primary(self) -> PrimaryResource:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        return PrimaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> CurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return CurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return CurrenciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        code: str,
        name: str,
        symbol: str,
        decimal_places: int | Omit = omit,
        enabled: bool | Omit = omit,
        primary: bool | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """Creates a new currency.

        The data required can be submitted as a JSON body or as
        a list of parameters.

        Args:
          decimal_places: Supports 0-16 decimals.

          enabled: Defaults to true

          primary: Make this currency the primary currency for the current administration. You can
              set this value to FALSE, in which case nothing will change to the primary
              currency. If you set it to TRUE, the current primary currency will no longer be
              the primary currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/currencies",
            body=maybe_transform(
                {
                    "code": code,
                    "name": name,
                    "symbol": symbol,
                    "decimal_places": decimal_places,
                    "enabled": enabled,
                    "primary": primary,
                },
                currency_create_params.CurrencyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    def retrieve(
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
        """
        Get a single currency.

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
        return self._get(
            path_template("/v1/currencies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    def update(
        self,
        path_code: str,
        *,
        body_code: str | Omit = omit,
        decimal_places: int | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        primary: Literal[True] | Omit = omit,
        symbol: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """
        Update existing currency.

        Args:
          body_code: The currency code

          decimal_places: How many decimals to use when displaying this currency. Between 0 and 16.

          enabled: If the currency is enabled

          name: The currency name

          primary: If the currency must be the primary for the user. You can only submit TRUE.
              Submitting FALSE will not drop this currency as the primary currency, because
              then the system would be without one.

          symbol: The currency symbol

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_code:
            raise ValueError(f"Expected a non-empty value for `path_code` but received {path_code!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._put(
            path_template("/v1/currencies/{path_code}", path_code=path_code),
            body=maybe_transform(
                {
                    "body_code": body_code,
                    "decimal_places": decimal_places,
                    "enabled": enabled,
                    "name": name,
                    "primary": primary,
                    "symbol": symbol,
                },
                currency_update_params.CurrencyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    def list(
        self,
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
    ) -> CurrencyListResponse:
        """List all currencies.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/currencies",
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
                    currency_list_params.CurrencyListParams,
                ),
            ),
            cast_to=CurrencyListResponse,
        )

    def delete(
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
    ) -> None:
        """
        Delete a currency.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/currencies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def disable(
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
        """
        Disable a currency.

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
            path_template("/v1/currencies/{code}/disable", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    def enable(
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
        """
        Enable a single currency.

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
            path_template("/v1/currencies/{code}/enable", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    def list_accounts(
        self,
        code: str,
        *,
        date: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        type: AccountTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountArray:
        """List all accounts with this currency.

        Args:
          date: A date formatted YYYY-MM-DD.

        When added to the request, Firefly III will show
              the account's balance on that day.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/currencies/{code}/accounts", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                        "type": type,
                    },
                    currency_list_accounts_params.CurrencyListAccountsParams,
                ),
            ),
            cast_to=AccountArray,
        )

    def list_available_budgets(
        self,
        code: str,
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
    ) -> AvailableBudgetArray:
        """
        List all available budgets with this currency.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/currencies/{code}/available-budgets", code=code),
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
                    currency_list_available_budgets_params.CurrencyListAvailableBudgetsParams,
                ),
            ),
            cast_to=AvailableBudgetArray,
        )

    def list_bills(
        self,
        code: str,
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
    ) -> BillArray:
        """List all bills with this currency.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/currencies/{code}/bills", code=code),
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
                    currency_list_bills_params.CurrencyListBillsParams,
                ),
            ),
            cast_to=BillArray,
        )

    def list_budget_limits(
        self,
        code: str,
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
    ) -> BudgetLimitArray:
        """
        List all budget limits with this currency

        Args:
          end: End date for the budget limit list.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: Start date for the budget limit list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/currencies/{code}/budget-limits", code=code),
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
                    currency_list_budget_limits_params.CurrencyListBudgetLimitsParams,
                ),
            ),
            cast_to=BudgetLimitArray,
        )

    def list_recurrences(
        self,
        code: str,
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
    ) -> RecurrenceArray:
        """
        List all recurring transactions with this currency.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/currencies/{code}/recurrences", code=code),
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
                    currency_list_recurrences_params.CurrencyListRecurrencesParams,
                ),
            ),
            cast_to=RecurrenceArray,
        )

    def list_rules(
        self,
        code: str,
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
    ) -> RuleArray:
        """List all rules with this currency.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/currencies/{code}/rules", code=code),
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
                    currency_list_rules_params.CurrencyListRulesParams,
                ),
            ),
            cast_to=RuleArray,
        )

    def list_transactions(
        self,
        code: str,
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
        List all transactions with this currency.

        Args:
          end: A date formatted YYYY-MM-DD, to limit the list of transactions.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD, to limit the list of transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/currencies/{code}/transactions", code=code),
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
                    currency_list_transactions_params.CurrencyListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncCurrenciesResource(AsyncAPIResource):
    """Endpoints to manage the currencies in Firefly III.

    Depending on the user&#039;s role you can also disable and enable them, or add new ones.
    """

    @cached_property
    def primary(self) -> AsyncPrimaryResource:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        return AsyncPrimaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncCurrenciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        code: str,
        name: str,
        symbol: str,
        decimal_places: int | Omit = omit,
        enabled: bool | Omit = omit,
        primary: bool | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """Creates a new currency.

        The data required can be submitted as a JSON body or as
        a list of parameters.

        Args:
          decimal_places: Supports 0-16 decimals.

          enabled: Defaults to true

          primary: Make this currency the primary currency for the current administration. You can
              set this value to FALSE, in which case nothing will change to the primary
              currency. If you set it to TRUE, the current primary currency will no longer be
              the primary currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/currencies",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "name": name,
                    "symbol": symbol,
                    "decimal_places": decimal_places,
                    "enabled": enabled,
                    "primary": primary,
                },
                currency_create_params.CurrencyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    async def retrieve(
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
        """
        Get a single currency.

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
        return await self._get(
            path_template("/v1/currencies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    async def update(
        self,
        path_code: str,
        *,
        body_code: str | Omit = omit,
        decimal_places: int | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        primary: Literal[True] | Omit = omit,
        symbol: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencySingle:
        """
        Update existing currency.

        Args:
          body_code: The currency code

          decimal_places: How many decimals to use when displaying this currency. Between 0 and 16.

          enabled: If the currency is enabled

          name: The currency name

          primary: If the currency must be the primary for the user. You can only submit TRUE.
              Submitting FALSE will not drop this currency as the primary currency, because
              then the system would be without one.

          symbol: The currency symbol

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_code:
            raise ValueError(f"Expected a non-empty value for `path_code` but received {path_code!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._put(
            path_template("/v1/currencies/{path_code}", path_code=path_code),
            body=await async_maybe_transform(
                {
                    "body_code": body_code,
                    "decimal_places": decimal_places,
                    "enabled": enabled,
                    "name": name,
                    "primary": primary,
                    "symbol": symbol,
                },
                currency_update_params.CurrencyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    async def list(
        self,
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
    ) -> CurrencyListResponse:
        """List all currencies.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/currencies",
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
                    currency_list_params.CurrencyListParams,
                ),
            ),
            cast_to=CurrencyListResponse,
        )

    async def delete(
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
    ) -> None:
        """
        Delete a currency.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/currencies/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def disable(
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
        """
        Disable a currency.

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
            path_template("/v1/currencies/{code}/disable", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    async def enable(
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
        """
        Enable a single currency.

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
            path_template("/v1/currencies/{code}/enable", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencySingle,
        )

    async def list_accounts(
        self,
        code: str,
        *,
        date: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        type: AccountTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountArray:
        """List all accounts with this currency.

        Args:
          date: A date formatted YYYY-MM-DD.

        When added to the request, Firefly III will show
              the account's balance on that day.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/currencies/{code}/accounts", code=code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                        "type": type,
                    },
                    currency_list_accounts_params.CurrencyListAccountsParams,
                ),
            ),
            cast_to=AccountArray,
        )

    async def list_available_budgets(
        self,
        code: str,
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
    ) -> AvailableBudgetArray:
        """
        List all available budgets with this currency.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/currencies/{code}/available-budgets", code=code),
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
                    currency_list_available_budgets_params.CurrencyListAvailableBudgetsParams,
                ),
            ),
            cast_to=AvailableBudgetArray,
        )

    async def list_bills(
        self,
        code: str,
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
    ) -> BillArray:
        """List all bills with this currency.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/currencies/{code}/bills", code=code),
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
                    currency_list_bills_params.CurrencyListBillsParams,
                ),
            ),
            cast_to=BillArray,
        )

    async def list_budget_limits(
        self,
        code: str,
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
    ) -> BudgetLimitArray:
        """
        List all budget limits with this currency

        Args:
          end: End date for the budget limit list.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: Start date for the budget limit list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/currencies/{code}/budget-limits", code=code),
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
                    currency_list_budget_limits_params.CurrencyListBudgetLimitsParams,
                ),
            ),
            cast_to=BudgetLimitArray,
        )

    async def list_recurrences(
        self,
        code: str,
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
    ) -> RecurrenceArray:
        """
        List all recurring transactions with this currency.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/currencies/{code}/recurrences", code=code),
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
                    currency_list_recurrences_params.CurrencyListRecurrencesParams,
                ),
            ),
            cast_to=RecurrenceArray,
        )

    async def list_rules(
        self,
        code: str,
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
    ) -> RuleArray:
        """List all rules with this currency.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/currencies/{code}/rules", code=code),
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
                    currency_list_rules_params.CurrencyListRulesParams,
                ),
            ),
            cast_to=RuleArray,
        )

    async def list_transactions(
        self,
        code: str,
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
        List all transactions with this currency.

        Args:
          end: A date formatted YYYY-MM-DD, to limit the list of transactions.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD, to limit the list of transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/currencies/{code}/transactions", code=code),
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
                    currency_list_transactions_params.CurrencyListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class CurrenciesResourceWithRawResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.create = to_raw_response_wrapper(
            currencies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            currencies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            currencies.update,
        )
        self.list = to_raw_response_wrapper(
            currencies.list,
        )
        self.delete = to_raw_response_wrapper(
            currencies.delete,
        )
        self.disable = to_raw_response_wrapper(
            currencies.disable,
        )
        self.enable = to_raw_response_wrapper(
            currencies.enable,
        )
        self.list_accounts = to_raw_response_wrapper(
            currencies.list_accounts,
        )
        self.list_available_budgets = to_raw_response_wrapper(
            currencies.list_available_budgets,
        )
        self.list_bills = to_raw_response_wrapper(
            currencies.list_bills,
        )
        self.list_budget_limits = to_raw_response_wrapper(
            currencies.list_budget_limits,
        )
        self.list_recurrences = to_raw_response_wrapper(
            currencies.list_recurrences,
        )
        self.list_rules = to_raw_response_wrapper(
            currencies.list_rules,
        )
        self.list_transactions = to_raw_response_wrapper(
            currencies.list_transactions,
        )

    @cached_property
    def primary(self) -> PrimaryResourceWithRawResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        return PrimaryResourceWithRawResponse(self._currencies.primary)


class AsyncCurrenciesResourceWithRawResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.create = async_to_raw_response_wrapper(
            currencies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            currencies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            currencies.update,
        )
        self.list = async_to_raw_response_wrapper(
            currencies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            currencies.delete,
        )
        self.disable = async_to_raw_response_wrapper(
            currencies.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            currencies.enable,
        )
        self.list_accounts = async_to_raw_response_wrapper(
            currencies.list_accounts,
        )
        self.list_available_budgets = async_to_raw_response_wrapper(
            currencies.list_available_budgets,
        )
        self.list_bills = async_to_raw_response_wrapper(
            currencies.list_bills,
        )
        self.list_budget_limits = async_to_raw_response_wrapper(
            currencies.list_budget_limits,
        )
        self.list_recurrences = async_to_raw_response_wrapper(
            currencies.list_recurrences,
        )
        self.list_rules = async_to_raw_response_wrapper(
            currencies.list_rules,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            currencies.list_transactions,
        )

    @cached_property
    def primary(self) -> AsyncPrimaryResourceWithRawResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        return AsyncPrimaryResourceWithRawResponse(self._currencies.primary)


class CurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: CurrenciesResource) -> None:
        self._currencies = currencies

        self.create = to_streamed_response_wrapper(
            currencies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            currencies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            currencies.update,
        )
        self.list = to_streamed_response_wrapper(
            currencies.list,
        )
        self.delete = to_streamed_response_wrapper(
            currencies.delete,
        )
        self.disable = to_streamed_response_wrapper(
            currencies.disable,
        )
        self.enable = to_streamed_response_wrapper(
            currencies.enable,
        )
        self.list_accounts = to_streamed_response_wrapper(
            currencies.list_accounts,
        )
        self.list_available_budgets = to_streamed_response_wrapper(
            currencies.list_available_budgets,
        )
        self.list_bills = to_streamed_response_wrapper(
            currencies.list_bills,
        )
        self.list_budget_limits = to_streamed_response_wrapper(
            currencies.list_budget_limits,
        )
        self.list_recurrences = to_streamed_response_wrapper(
            currencies.list_recurrences,
        )
        self.list_rules = to_streamed_response_wrapper(
            currencies.list_rules,
        )
        self.list_transactions = to_streamed_response_wrapper(
            currencies.list_transactions,
        )

    @cached_property
    def primary(self) -> PrimaryResourceWithStreamingResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        return PrimaryResourceWithStreamingResponse(self._currencies.primary)


class AsyncCurrenciesResourceWithStreamingResponse:
    def __init__(self, currencies: AsyncCurrenciesResource) -> None:
        self._currencies = currencies

        self.create = async_to_streamed_response_wrapper(
            currencies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            currencies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            currencies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            currencies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            currencies.delete,
        )
        self.disable = async_to_streamed_response_wrapper(
            currencies.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            currencies.enable,
        )
        self.list_accounts = async_to_streamed_response_wrapper(
            currencies.list_accounts,
        )
        self.list_available_budgets = async_to_streamed_response_wrapper(
            currencies.list_available_budgets,
        )
        self.list_bills = async_to_streamed_response_wrapper(
            currencies.list_bills,
        )
        self.list_budget_limits = async_to_streamed_response_wrapper(
            currencies.list_budget_limits,
        )
        self.list_recurrences = async_to_streamed_response_wrapper(
            currencies.list_recurrences,
        )
        self.list_rules = async_to_streamed_response_wrapper(
            currencies.list_rules,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            currencies.list_transactions,
        )

    @cached_property
    def primary(self) -> AsyncPrimaryResourceWithStreamingResponse:
        """Endpoints to manage the currencies in Firefly III.

        Depending on the user&#039;s role you can also disable and enable them, or add new ones.
        """
        return AsyncPrimaryResourceWithStreamingResponse(self._currencies.primary)
