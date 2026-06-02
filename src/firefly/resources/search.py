# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import AccountTypeFilter, search_accounts_params, search_transactions_params
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
from ..types.account_array import AccountArray
from ..types.transaction_array import TransactionArray
from ..types.account_type_filter import AccountTypeFilter

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    """Endpoints that allow you to search through the user&#039;s financial data.

    Different from the autocomplete endpoints, the search accepts more advanced arguments.
    """

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def accounts(
        self,
        *,
        field: Literal["all", "iban", "name", "number", "id"],
        query: str,
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
        """
        Search for accounts

        Args:
          field: The account field(s) you want to search in.

          query: The query you wish to search for.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/search/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "field": field,
                        "query": query,
                        "limit": limit,
                        "page": page,
                        "type": type,
                    },
                    search_accounts_params.SearchAccountsParams,
                ),
            ),
            cast_to=AccountArray,
        )

    def transactions(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        Searches through the users transactions.

        Args:
          query: The query you wish to search for.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/search/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "page": page,
                    },
                    search_transactions_params.SearchTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncSearchResource(AsyncAPIResource):
    """Endpoints that allow you to search through the user&#039;s financial data.

    Different from the autocomplete endpoints, the search accepts more advanced arguments.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def accounts(
        self,
        *,
        field: Literal["all", "iban", "name", "number", "id"],
        query: str,
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
        """
        Search for accounts

        Args:
          field: The account field(s) you want to search in.

          query: The query you wish to search for.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/search/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "field": field,
                        "query": query,
                        "limit": limit,
                        "page": page,
                        "type": type,
                    },
                    search_accounts_params.SearchAccountsParams,
                ),
            ),
            cast_to=AccountArray,
        )

    async def transactions(
        self,
        *,
        query: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        Searches through the users transactions.

        Args:
          query: The query you wish to search for.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/search/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "page": page,
                    },
                    search_transactions_params.SearchTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.accounts = to_raw_response_wrapper(
            search.accounts,
        )
        self.transactions = to_raw_response_wrapper(
            search.transactions,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.accounts = async_to_raw_response_wrapper(
            search.accounts,
        )
        self.transactions = async_to_raw_response_wrapper(
            search.transactions,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.accounts = to_streamed_response_wrapper(
            search.accounts,
        )
        self.transactions = to_streamed_response_wrapper(
            search.transactions,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.accounts = async_to_streamed_response_wrapper(
            search.accounts,
        )
        self.transactions = async_to_streamed_response_wrapper(
            search.transactions,
        )
