# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    autocomplete_list_tags_params,
    autocomplete_list_bills_params,
    autocomplete_list_rules_params,
    autocomplete_list_budgets_params,
    autocomplete_list_accounts_params,
    autocomplete_list_categories_params,
    autocomplete_list_currencies_params,
    autocomplete_list_piggy_banks_params,
    autocomplete_list_rule_groups_params,
    autocomplete_list_transactions_params,
    autocomplete_list_object_groups_params,
    autocomplete_list_subscriptions_params,
    autocomplete_list_transaction_types_params,
    autocomplete_list_currencies_with_code_params,
    autocomplete_list_transactions_with_id_params,
    autocomplete_list_recurring_transactions_params,
    autocomplete_list_piggy_banks_with_balance_params,
)
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
from ..types.account_type_filter import AccountTypeFilter
from ..types.autocomplete_list_tags_response import AutocompleteListTagsResponse
from ..types.autocomplete_list_bills_response import AutocompleteListBillsResponse
from ..types.autocomplete_list_rules_response import AutocompleteListRulesResponse
from ..types.autocomplete_list_budgets_response import AutocompleteListBudgetsResponse
from ..types.autocomplete_list_accounts_response import AutocompleteListAccountsResponse
from ..types.autocomplete_list_categories_response import AutocompleteListCategoriesResponse
from ..types.autocomplete_list_currencies_response import AutocompleteListCurrenciesResponse
from ..types.autocomplete_list_piggy_banks_response import AutocompleteListPiggyBanksResponse
from ..types.autocomplete_list_rule_groups_response import AutocompleteListRuleGroupsResponse
from ..types.autocomplete_list_transactions_response import AutocompleteListTransactionsResponse
from ..types.autocomplete_list_object_groups_response import AutocompleteListObjectGroupsResponse
from ..types.autocomplete_list_subscriptions_response import AutocompleteListSubscriptionsResponse
from ..types.autocomplete_list_transaction_types_response import AutocompleteListTransactionTypesResponse
from ..types.autocomplete_list_currencies_with_code_response import AutocompleteListCurrenciesWithCodeResponse
from ..types.autocomplete_list_transactions_with_id_response import AutocompleteListTransactionsWithIDResponse
from ..types.autocomplete_list_recurring_transactions_response import AutocompleteListRecurringTransactionsResponse
from ..types.autocomplete_list_piggy_banks_with_balance_response import AutocompleteListPiggyBanksWithBalanceResponse

__all__ = ["AutocompleteResource", "AsyncAutocompleteResource"]


class AutocompleteResource(SyncAPIResource):
    """
    Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
    """

    @cached_property
    def with_raw_response(self) -> AutocompleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AutocompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutocompleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AutocompleteResourceWithStreamingResponse(self)

    def list_accounts(
        self,
        *,
        date: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        types: List[AccountTypeFilter] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListAccountsResponse:
        """
        Returns all accounts of the user returned in a basic auto-complete array.

        Args:
          date: If the account is an asset account or a liability, the autocomplete will also
              return the balance of the account on this date.

          limit: The number of items returned.

          query: The autocomplete search query.

          types: Optional filter on the account type(s) used in the autocomplete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "query": query,
                        "types": types,
                    },
                    autocomplete_list_accounts_params.AutocompleteListAccountsParams,
                ),
            ),
            cast_to=AutocompleteListAccountsResponse,
        )

    def list_bills(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListBillsResponse:
        """
        Returns all bills of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/bills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_bills_params.AutocompleteListBillsParams,
                ),
            ),
            cast_to=AutocompleteListBillsResponse,
        )

    def list_budgets(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListBudgetsResponse:
        """
        Returns all budgets of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_budgets_params.AutocompleteListBudgetsParams,
                ),
            ),
            cast_to=AutocompleteListBudgetsResponse,
        )

    def list_categories(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListCategoriesResponse:
        """
        Returns all categories of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_categories_params.AutocompleteListCategoriesParams,
                ),
            ),
            cast_to=AutocompleteListCategoriesResponse,
        )

    def list_currencies(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListCurrenciesResponse:
        """
        Returns all currencies of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/currencies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_currencies_params.AutocompleteListCurrenciesParams,
                ),
            ),
            cast_to=AutocompleteListCurrenciesResponse,
        )

    def list_currencies_with_code(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListCurrenciesWithCodeResponse:
        """Returns all currencies of the user returned in a basic auto-complete array.

        This
        endpoint is DEPRECATED and I suggest you DO NOT use it.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/currencies-with-code",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_currencies_with_code_params.AutocompleteListCurrenciesWithCodeParams,
                ),
            ),
            cast_to=AutocompleteListCurrenciesWithCodeResponse,
        )

    def list_object_groups(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListObjectGroupsResponse:
        """
        Returns all object groups of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/object-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_object_groups_params.AutocompleteListObjectGroupsParams,
                ),
            ),
            cast_to=AutocompleteListObjectGroupsResponse,
        )

    def list_piggy_banks(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListPiggyBanksResponse:
        """
        Returns all piggy banks of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/piggy-banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_piggy_banks_params.AutocompleteListPiggyBanksParams,
                ),
            ),
            cast_to=AutocompleteListPiggyBanksResponse,
        )

    def list_piggy_banks_with_balance(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListPiggyBanksWithBalanceResponse:
        """
        Returns all piggy banks of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/piggy-banks-with-balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_piggy_banks_with_balance_params.AutocompleteListPiggyBanksWithBalanceParams,
                ),
            ),
            cast_to=AutocompleteListPiggyBanksWithBalanceResponse,
        )

    def list_recurring_transactions(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListRecurringTransactionsResponse:
        """
        Returns all recurring transactions of the user returned in a basic auto-complete
        array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/recurring",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_recurring_transactions_params.AutocompleteListRecurringTransactionsParams,
                ),
            ),
            cast_to=AutocompleteListRecurringTransactionsResponse,
        )

    def list_rule_groups(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListRuleGroupsResponse:
        """
        Returns all rule groups of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/rule-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_rule_groups_params.AutocompleteListRuleGroupsParams,
                ),
            ),
            cast_to=AutocompleteListRuleGroupsResponse,
        )

    def list_rules(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListRulesResponse:
        """
        Returns all rules of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_rules_params.AutocompleteListRulesParams,
                ),
            ),
            cast_to=AutocompleteListRulesResponse,
        )

    def list_subscriptions(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListSubscriptionsResponse:
        """
        Returns all subscriptions of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_subscriptions_params.AutocompleteListSubscriptionsParams,
                ),
            ),
            cast_to=AutocompleteListSubscriptionsResponse,
        )

    def list_tags(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTagsResponse:
        """
        Returns all tags of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_tags_params.AutocompleteListTagsParams,
                ),
            ),
            cast_to=AutocompleteListTagsResponse,
        )

    def list_transaction_types(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTransactionTypesResponse:
        """Returns all transaction types returned in a basic auto-complete array.

        English
        only.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/transaction-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_transaction_types_params.AutocompleteListTransactionTypesParams,
                ),
            ),
            cast_to=AutocompleteListTransactionTypesResponse,
        )

    def list_transactions(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTransactionsResponse:
        """
        Returns all transaction descriptions of the user returned in a basic
        auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_transactions_params.AutocompleteListTransactionsParams,
                ),
            ),
            cast_to=AutocompleteListTransactionsResponse,
        )

    def list_transactions_with_id(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTransactionsWithIDResponse:
        """
        Returns all transactions, complemented with their ID, of the user returned in a
        basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT
        use it.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/autocomplete/transactions-with-id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_transactions_with_id_params.AutocompleteListTransactionsWithIDParams,
                ),
            ),
            cast_to=AutocompleteListTransactionsWithIDResponse,
        )


class AsyncAutocompleteResource(AsyncAPIResource):
    """
    Auto-complete endpoints show basic information about Firefly III models, like the name and maybe some amounts. They all support a search query and can be used to autocomplete data in forms. Autocomplete return values always have a &quot;name&quot;-field.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAutocompleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutocompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutocompleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncAutocompleteResourceWithStreamingResponse(self)

    async def list_accounts(
        self,
        *,
        date: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        types: List[AccountTypeFilter] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListAccountsResponse:
        """
        Returns all accounts of the user returned in a basic auto-complete array.

        Args:
          date: If the account is an asset account or a liability, the autocomplete will also
              return the balance of the account on this date.

          limit: The number of items returned.

          query: The autocomplete search query.

          types: Optional filter on the account type(s) used in the autocomplete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "query": query,
                        "types": types,
                    },
                    autocomplete_list_accounts_params.AutocompleteListAccountsParams,
                ),
            ),
            cast_to=AutocompleteListAccountsResponse,
        )

    async def list_bills(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListBillsResponse:
        """
        Returns all bills of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/bills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_bills_params.AutocompleteListBillsParams,
                ),
            ),
            cast_to=AutocompleteListBillsResponse,
        )

    async def list_budgets(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListBudgetsResponse:
        """
        Returns all budgets of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_budgets_params.AutocompleteListBudgetsParams,
                ),
            ),
            cast_to=AutocompleteListBudgetsResponse,
        )

    async def list_categories(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListCategoriesResponse:
        """
        Returns all categories of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_categories_params.AutocompleteListCategoriesParams,
                ),
            ),
            cast_to=AutocompleteListCategoriesResponse,
        )

    async def list_currencies(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListCurrenciesResponse:
        """
        Returns all currencies of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/currencies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_currencies_params.AutocompleteListCurrenciesParams,
                ),
            ),
            cast_to=AutocompleteListCurrenciesResponse,
        )

    async def list_currencies_with_code(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListCurrenciesWithCodeResponse:
        """Returns all currencies of the user returned in a basic auto-complete array.

        This
        endpoint is DEPRECATED and I suggest you DO NOT use it.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/currencies-with-code",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_currencies_with_code_params.AutocompleteListCurrenciesWithCodeParams,
                ),
            ),
            cast_to=AutocompleteListCurrenciesWithCodeResponse,
        )

    async def list_object_groups(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListObjectGroupsResponse:
        """
        Returns all object groups of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/object-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_object_groups_params.AutocompleteListObjectGroupsParams,
                ),
            ),
            cast_to=AutocompleteListObjectGroupsResponse,
        )

    async def list_piggy_banks(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListPiggyBanksResponse:
        """
        Returns all piggy banks of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/piggy-banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_piggy_banks_params.AutocompleteListPiggyBanksParams,
                ),
            ),
            cast_to=AutocompleteListPiggyBanksResponse,
        )

    async def list_piggy_banks_with_balance(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListPiggyBanksWithBalanceResponse:
        """
        Returns all piggy banks of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/piggy-banks-with-balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_piggy_banks_with_balance_params.AutocompleteListPiggyBanksWithBalanceParams,
                ),
            ),
            cast_to=AutocompleteListPiggyBanksWithBalanceResponse,
        )

    async def list_recurring_transactions(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListRecurringTransactionsResponse:
        """
        Returns all recurring transactions of the user returned in a basic auto-complete
        array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/recurring",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_recurring_transactions_params.AutocompleteListRecurringTransactionsParams,
                ),
            ),
            cast_to=AutocompleteListRecurringTransactionsResponse,
        )

    async def list_rule_groups(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListRuleGroupsResponse:
        """
        Returns all rule groups of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/rule-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_rule_groups_params.AutocompleteListRuleGroupsParams,
                ),
            ),
            cast_to=AutocompleteListRuleGroupsResponse,
        )

    async def list_rules(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListRulesResponse:
        """
        Returns all rules of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_rules_params.AutocompleteListRulesParams,
                ),
            ),
            cast_to=AutocompleteListRulesResponse,
        )

    async def list_subscriptions(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListSubscriptionsResponse:
        """
        Returns all subscriptions of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_subscriptions_params.AutocompleteListSubscriptionsParams,
                ),
            ),
            cast_to=AutocompleteListSubscriptionsResponse,
        )

    async def list_tags(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTagsResponse:
        """
        Returns all tags of the user returned in a basic auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_tags_params.AutocompleteListTagsParams,
                ),
            ),
            cast_to=AutocompleteListTagsResponse,
        )

    async def list_transaction_types(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTransactionTypesResponse:
        """Returns all transaction types returned in a basic auto-complete array.

        English
        only.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/transaction-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_transaction_types_params.AutocompleteListTransactionTypesParams,
                ),
            ),
            cast_to=AutocompleteListTransactionTypesResponse,
        )

    async def list_transactions(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTransactionsResponse:
        """
        Returns all transaction descriptions of the user returned in a basic
        auto-complete array.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_transactions_params.AutocompleteListTransactionsParams,
                ),
            ),
            cast_to=AutocompleteListTransactionsResponse,
        )

    async def list_transactions_with_id(
        self,
        *,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutocompleteListTransactionsWithIDResponse:
        """
        Returns all transactions, complemented with their ID, of the user returned in a
        basic auto-complete array. This endpoint is DEPRECATED and I suggest you DO NOT
        use it.

        Args:
          limit: The number of items returned.

          query: The autocomplete search query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/autocomplete/transactions-with-id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "query": query,
                    },
                    autocomplete_list_transactions_with_id_params.AutocompleteListTransactionsWithIDParams,
                ),
            ),
            cast_to=AutocompleteListTransactionsWithIDResponse,
        )


class AutocompleteResourceWithRawResponse:
    def __init__(self, autocomplete: AutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.list_accounts = to_raw_response_wrapper(
            autocomplete.list_accounts,
        )
        self.list_bills = to_raw_response_wrapper(
            autocomplete.list_bills,
        )
        self.list_budgets = to_raw_response_wrapper(
            autocomplete.list_budgets,
        )
        self.list_categories = to_raw_response_wrapper(
            autocomplete.list_categories,
        )
        self.list_currencies = to_raw_response_wrapper(
            autocomplete.list_currencies,
        )
        self.list_currencies_with_code = to_raw_response_wrapper(
            autocomplete.list_currencies_with_code,
        )
        self.list_object_groups = to_raw_response_wrapper(
            autocomplete.list_object_groups,
        )
        self.list_piggy_banks = to_raw_response_wrapper(
            autocomplete.list_piggy_banks,
        )
        self.list_piggy_banks_with_balance = to_raw_response_wrapper(
            autocomplete.list_piggy_banks_with_balance,
        )
        self.list_recurring_transactions = to_raw_response_wrapper(
            autocomplete.list_recurring_transactions,
        )
        self.list_rule_groups = to_raw_response_wrapper(
            autocomplete.list_rule_groups,
        )
        self.list_rules = to_raw_response_wrapper(
            autocomplete.list_rules,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            autocomplete.list_subscriptions,
        )
        self.list_tags = to_raw_response_wrapper(
            autocomplete.list_tags,
        )
        self.list_transaction_types = to_raw_response_wrapper(
            autocomplete.list_transaction_types,
        )
        self.list_transactions = to_raw_response_wrapper(
            autocomplete.list_transactions,
        )
        self.list_transactions_with_id = to_raw_response_wrapper(
            autocomplete.list_transactions_with_id,
        )


class AsyncAutocompleteResourceWithRawResponse:
    def __init__(self, autocomplete: AsyncAutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.list_accounts = async_to_raw_response_wrapper(
            autocomplete.list_accounts,
        )
        self.list_bills = async_to_raw_response_wrapper(
            autocomplete.list_bills,
        )
        self.list_budgets = async_to_raw_response_wrapper(
            autocomplete.list_budgets,
        )
        self.list_categories = async_to_raw_response_wrapper(
            autocomplete.list_categories,
        )
        self.list_currencies = async_to_raw_response_wrapper(
            autocomplete.list_currencies,
        )
        self.list_currencies_with_code = async_to_raw_response_wrapper(
            autocomplete.list_currencies_with_code,
        )
        self.list_object_groups = async_to_raw_response_wrapper(
            autocomplete.list_object_groups,
        )
        self.list_piggy_banks = async_to_raw_response_wrapper(
            autocomplete.list_piggy_banks,
        )
        self.list_piggy_banks_with_balance = async_to_raw_response_wrapper(
            autocomplete.list_piggy_banks_with_balance,
        )
        self.list_recurring_transactions = async_to_raw_response_wrapper(
            autocomplete.list_recurring_transactions,
        )
        self.list_rule_groups = async_to_raw_response_wrapper(
            autocomplete.list_rule_groups,
        )
        self.list_rules = async_to_raw_response_wrapper(
            autocomplete.list_rules,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            autocomplete.list_subscriptions,
        )
        self.list_tags = async_to_raw_response_wrapper(
            autocomplete.list_tags,
        )
        self.list_transaction_types = async_to_raw_response_wrapper(
            autocomplete.list_transaction_types,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            autocomplete.list_transactions,
        )
        self.list_transactions_with_id = async_to_raw_response_wrapper(
            autocomplete.list_transactions_with_id,
        )


class AutocompleteResourceWithStreamingResponse:
    def __init__(self, autocomplete: AutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.list_accounts = to_streamed_response_wrapper(
            autocomplete.list_accounts,
        )
        self.list_bills = to_streamed_response_wrapper(
            autocomplete.list_bills,
        )
        self.list_budgets = to_streamed_response_wrapper(
            autocomplete.list_budgets,
        )
        self.list_categories = to_streamed_response_wrapper(
            autocomplete.list_categories,
        )
        self.list_currencies = to_streamed_response_wrapper(
            autocomplete.list_currencies,
        )
        self.list_currencies_with_code = to_streamed_response_wrapper(
            autocomplete.list_currencies_with_code,
        )
        self.list_object_groups = to_streamed_response_wrapper(
            autocomplete.list_object_groups,
        )
        self.list_piggy_banks = to_streamed_response_wrapper(
            autocomplete.list_piggy_banks,
        )
        self.list_piggy_banks_with_balance = to_streamed_response_wrapper(
            autocomplete.list_piggy_banks_with_balance,
        )
        self.list_recurring_transactions = to_streamed_response_wrapper(
            autocomplete.list_recurring_transactions,
        )
        self.list_rule_groups = to_streamed_response_wrapper(
            autocomplete.list_rule_groups,
        )
        self.list_rules = to_streamed_response_wrapper(
            autocomplete.list_rules,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            autocomplete.list_subscriptions,
        )
        self.list_tags = to_streamed_response_wrapper(
            autocomplete.list_tags,
        )
        self.list_transaction_types = to_streamed_response_wrapper(
            autocomplete.list_transaction_types,
        )
        self.list_transactions = to_streamed_response_wrapper(
            autocomplete.list_transactions,
        )
        self.list_transactions_with_id = to_streamed_response_wrapper(
            autocomplete.list_transactions_with_id,
        )


class AsyncAutocompleteResourceWithStreamingResponse:
    def __init__(self, autocomplete: AsyncAutocompleteResource) -> None:
        self._autocomplete = autocomplete

        self.list_accounts = async_to_streamed_response_wrapper(
            autocomplete.list_accounts,
        )
        self.list_bills = async_to_streamed_response_wrapper(
            autocomplete.list_bills,
        )
        self.list_budgets = async_to_streamed_response_wrapper(
            autocomplete.list_budgets,
        )
        self.list_categories = async_to_streamed_response_wrapper(
            autocomplete.list_categories,
        )
        self.list_currencies = async_to_streamed_response_wrapper(
            autocomplete.list_currencies,
        )
        self.list_currencies_with_code = async_to_streamed_response_wrapper(
            autocomplete.list_currencies_with_code,
        )
        self.list_object_groups = async_to_streamed_response_wrapper(
            autocomplete.list_object_groups,
        )
        self.list_piggy_banks = async_to_streamed_response_wrapper(
            autocomplete.list_piggy_banks,
        )
        self.list_piggy_banks_with_balance = async_to_streamed_response_wrapper(
            autocomplete.list_piggy_banks_with_balance,
        )
        self.list_recurring_transactions = async_to_streamed_response_wrapper(
            autocomplete.list_recurring_transactions,
        )
        self.list_rule_groups = async_to_streamed_response_wrapper(
            autocomplete.list_rule_groups,
        )
        self.list_rules = async_to_streamed_response_wrapper(
            autocomplete.list_rules,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            autocomplete.list_subscriptions,
        )
        self.list_tags = async_to_streamed_response_wrapper(
            autocomplete.list_tags,
        )
        self.list_transaction_types = async_to_streamed_response_wrapper(
            autocomplete.list_transaction_types,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            autocomplete.list_transactions,
        )
        self.list_transactions_with_id = async_to_streamed_response_wrapper(
            autocomplete.list_transactions_with_id,
        )
