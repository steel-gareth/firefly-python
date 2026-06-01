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
    income_get_total_params,
    income_list_by_tag_params,
    income_list_by_category_params,
    income_list_without_tag_params,
    income_list_by_asset_account_params,
    income_list_without_category_params,
    income_list_by_revenue_account_params,
)
from ...types.insight.income_get_total_response import IncomeGetTotalResponse
from ...types.insight.income_list_by_tag_response import IncomeListByTagResponse
from ...types.insight.income_list_by_category_response import IncomeListByCategoryResponse
from ...types.insight.income_list_without_tag_response import IncomeListWithoutTagResponse
from ...types.insight.income_list_by_asset_account_response import IncomeListByAssetAccountResponse
from ...types.insight.income_list_without_category_response import IncomeListWithoutCategoryResponse
from ...types.insight.income_list_by_revenue_account_response import IncomeListByRevenueAccountResponse

__all__ = ["IncomeResource", "AsyncIncomeResource"]


class IncomeResource(SyncAPIResource):
    """
    The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
    """

    @cached_property
    def with_raw_response(self) -> IncomeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return IncomeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncomeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return IncomeResourceWithStreamingResponse(self)

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
    ) -> IncomeGetTotalResponse:
        """
        This endpoint gives a sum of the total income received by the user.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/income/total",
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
                    income_get_total_params.IncomeGetTotalParams,
                ),
            ),
            cast_to=IncomeGetTotalResponse,
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
    ) -> IncomeListByAssetAccountResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        asset account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/income/asset",
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
                    income_list_by_asset_account_params.IncomeListByAssetAccountParams,
                ),
            ),
            cast_to=IncomeListByAssetAccountResponse,
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
    ) -> IncomeListByCategoryResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        (any) category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          categories: The categories to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/income/category",
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
                    income_list_by_category_params.IncomeListByCategoryParams,
                ),
            ),
            cast_to=IncomeListByCategoryResponse,
        )

    def list_by_revenue_account(
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
    ) -> IncomeListByRevenueAccountResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        revenue account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you add the accounts ID's of
              revenue accounts, only those accounts are included in the results. If you
              include ID's of asset accounts or liabilities, only deposits to those asset
              accounts / liabilities will be included. You can combine both asset / liability
              and deposit account ID's. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/income/revenue",
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
                    income_list_by_revenue_account_params.IncomeListByRevenueAccountParams,
                ),
            ),
            cast_to=IncomeListByRevenueAccountResponse,
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
    ) -> IncomeListByTagResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        (any) tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          tags: The tags to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/income/tag",
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
                    income_list_by_tag_params.IncomeListByTagParams,
                ),
            ),
            cast_to=IncomeListByTagResponse,
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
    ) -> IncomeListWithoutCategoryResponse:
        """
        This endpoint gives a summary of the income received by the user, including only
        income with no category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/income/no-category",
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
                    income_list_without_category_params.IncomeListWithoutCategoryParams,
                ),
            ),
            cast_to=IncomeListWithoutCategoryResponse,
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
    ) -> IncomeListWithoutTagResponse:
        """
        This endpoint gives a summary of the income received by the user, including only
        income with no tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/income/no-tag",
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
                    income_list_without_tag_params.IncomeListWithoutTagParams,
                ),
            ),
            cast_to=IncomeListWithoutTagResponse,
        )


class AsyncIncomeResource(AsyncAPIResource):
    """
    The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
    """

    @cached_property
    def with_raw_response(self) -> AsyncIncomeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIncomeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncomeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncIncomeResourceWithStreamingResponse(self)

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
    ) -> IncomeGetTotalResponse:
        """
        This endpoint gives a sum of the total income received by the user.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/income/total",
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
                    income_get_total_params.IncomeGetTotalParams,
                ),
            ),
            cast_to=IncomeGetTotalResponse,
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
    ) -> IncomeListByAssetAccountResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        asset account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/income/asset",
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
                    income_list_by_asset_account_params.IncomeListByAssetAccountParams,
                ),
            ),
            cast_to=IncomeListByAssetAccountResponse,
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
    ) -> IncomeListByCategoryResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        (any) category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          categories: The categories to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/income/category",
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
                    income_list_by_category_params.IncomeListByCategoryParams,
                ),
            ),
            cast_to=IncomeListByCategoryResponse,
        )

    async def list_by_revenue_account(
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
    ) -> IncomeListByRevenueAccountResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        revenue account.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you add the accounts ID's of
              revenue accounts, only those accounts are included in the results. If you
              include ID's of asset accounts or liabilities, only deposits to those asset
              accounts / liabilities will be included. You can combine both asset / liability
              and deposit account ID's. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/income/revenue",
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
                    income_list_by_revenue_account_params.IncomeListByRevenueAccountParams,
                ),
            ),
            cast_to=IncomeListByRevenueAccountResponse,
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
    ) -> IncomeListByTagResponse:
        """
        This endpoint gives a summary of the income received by the user, grouped by
        (any) tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          tags: The tags to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/income/tag",
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
                    income_list_by_tag_params.IncomeListByTagParams,
                ),
            ),
            cast_to=IncomeListByTagResponse,
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
    ) -> IncomeListWithoutCategoryResponse:
        """
        This endpoint gives a summary of the income received by the user, including only
        income with no category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/income/no-category",
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
                    income_list_without_category_params.IncomeListWithoutCategoryParams,
                ),
            ),
            cast_to=IncomeListWithoutCategoryResponse,
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
    ) -> IncomeListWithoutTagResponse:
        """
        This endpoint gives a summary of the income received by the user, including only
        income with no tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only deposits to those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/income/no-tag",
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
                    income_list_without_tag_params.IncomeListWithoutTagParams,
                ),
            ),
            cast_to=IncomeListWithoutTagResponse,
        )


class IncomeResourceWithRawResponse:
    def __init__(self, income: IncomeResource) -> None:
        self._income = income

        self.get_total = to_raw_response_wrapper(
            income.get_total,
        )
        self.list_by_asset_account = to_raw_response_wrapper(
            income.list_by_asset_account,
        )
        self.list_by_category = to_raw_response_wrapper(
            income.list_by_category,
        )
        self.list_by_revenue_account = to_raw_response_wrapper(
            income.list_by_revenue_account,
        )
        self.list_by_tag = to_raw_response_wrapper(
            income.list_by_tag,
        )
        self.list_without_category = to_raw_response_wrapper(
            income.list_without_category,
        )
        self.list_without_tag = to_raw_response_wrapper(
            income.list_without_tag,
        )


class AsyncIncomeResourceWithRawResponse:
    def __init__(self, income: AsyncIncomeResource) -> None:
        self._income = income

        self.get_total = async_to_raw_response_wrapper(
            income.get_total,
        )
        self.list_by_asset_account = async_to_raw_response_wrapper(
            income.list_by_asset_account,
        )
        self.list_by_category = async_to_raw_response_wrapper(
            income.list_by_category,
        )
        self.list_by_revenue_account = async_to_raw_response_wrapper(
            income.list_by_revenue_account,
        )
        self.list_by_tag = async_to_raw_response_wrapper(
            income.list_by_tag,
        )
        self.list_without_category = async_to_raw_response_wrapper(
            income.list_without_category,
        )
        self.list_without_tag = async_to_raw_response_wrapper(
            income.list_without_tag,
        )


class IncomeResourceWithStreamingResponse:
    def __init__(self, income: IncomeResource) -> None:
        self._income = income

        self.get_total = to_streamed_response_wrapper(
            income.get_total,
        )
        self.list_by_asset_account = to_streamed_response_wrapper(
            income.list_by_asset_account,
        )
        self.list_by_category = to_streamed_response_wrapper(
            income.list_by_category,
        )
        self.list_by_revenue_account = to_streamed_response_wrapper(
            income.list_by_revenue_account,
        )
        self.list_by_tag = to_streamed_response_wrapper(
            income.list_by_tag,
        )
        self.list_without_category = to_streamed_response_wrapper(
            income.list_without_category,
        )
        self.list_without_tag = to_streamed_response_wrapper(
            income.list_without_tag,
        )


class AsyncIncomeResourceWithStreamingResponse:
    def __init__(self, income: AsyncIncomeResource) -> None:
        self._income = income

        self.get_total = async_to_streamed_response_wrapper(
            income.get_total,
        )
        self.list_by_asset_account = async_to_streamed_response_wrapper(
            income.list_by_asset_account,
        )
        self.list_by_category = async_to_streamed_response_wrapper(
            income.list_by_category,
        )
        self.list_by_revenue_account = async_to_streamed_response_wrapper(
            income.list_by_revenue_account,
        )
        self.list_by_tag = async_to_streamed_response_wrapper(
            income.list_by_tag,
        )
        self.list_without_category = async_to_streamed_response_wrapper(
            income.list_without_category,
        )
        self.list_without_tag = async_to_streamed_response_wrapper(
            income.list_without_tag,
        )
