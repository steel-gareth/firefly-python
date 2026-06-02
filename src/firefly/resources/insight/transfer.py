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
    transfer_get_total_params,
    transfer_list_by_tag_params,
    transfer_list_by_category_params,
    transfer_list_without_tag_params,
    transfer_list_by_asset_account_params,
    transfer_list_without_category_params,
)
from ...types.insight.transfer_get_total_response import TransferGetTotalResponse
from ...types.insight.transfer_list_by_tag_response import TransferListByTagResponse
from ...types.insight.transfer_list_by_category_response import TransferListByCategoryResponse
from ...types.insight.transfer_list_without_tag_response import TransferListWithoutTagResponse
from ...types.insight.transfer_list_by_asset_account_response import TransferListByAssetAccountResponse
from ...types.insight.transfer_list_without_category_response import TransferListWithoutCategoryResponse

__all__ = ["TransferResource", "AsyncTransferResource"]


class TransferResource(SyncAPIResource):
    """
    The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
    """

    @cached_property
    def with_raw_response(self) -> TransferResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return TransferResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransferResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return TransferResourceWithStreamingResponse(self)

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
    ) -> TransferGetTotalResponse:
        """
        This endpoint gives a sum of the total amount transfers made by the user.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/transfer/total",
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
                    transfer_get_total_params.TransferGetTotalParams,
                ),
            ),
            cast_to=TransferGetTotalResponse,
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
    ) -> TransferListByAssetAccountResponse:
        """
        This endpoint gives a summary of the transfers made by the user, grouped by
        asset account or lability.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/transfer/asset",
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
                    transfer_list_by_asset_account_params.TransferListByAssetAccountParams,
                ),
            ),
            cast_to=TransferListByAssetAccountResponse,
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
    ) -> TransferListByCategoryResponse:
        """
        This endpoint gives a summary of the transfers made by the user, grouped by
        (any) category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          categories: The categories to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/transfer/category",
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
                    transfer_list_by_category_params.TransferListByCategoryParams,
                ),
            ),
            cast_to=TransferListByCategoryResponse,
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
    ) -> TransferListByTagResponse:
        """
        This endpoint gives a summary of the transfers created by the user, grouped by
        (any) tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          tags: The tags to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/transfer/tag",
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
                    transfer_list_by_tag_params.TransferListByTagParams,
                ),
            ),
            cast_to=TransferListByTagResponse,
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
    ) -> TransferListWithoutCategoryResponse:
        """
        This endpoint gives a summary of the transfers made by the user, including only
        transfers with no category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/transfer/no-category",
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
                    transfer_list_without_category_params.TransferListWithoutCategoryParams,
                ),
            ),
            cast_to=TransferListWithoutCategoryResponse,
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
    ) -> TransferListWithoutTagResponse:
        """
        This endpoint gives a summary of the transfers made by the user, including only
        transfers with no tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers from those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/insight/transfer/no-tag",
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
                    transfer_list_without_tag_params.TransferListWithoutTagParams,
                ),
            ),
            cast_to=TransferListWithoutTagResponse,
        )


class AsyncTransferResource(AsyncAPIResource):
    """
    The &quot;insight&quot; endpoints try to deliver sums, balances and insightful information in the broadest sense of the word.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTransferResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransferResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransferResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncTransferResourceWithStreamingResponse(self)

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
    ) -> TransferGetTotalResponse:
        """
        This endpoint gives a sum of the total amount transfers made by the user.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/transfer/total",
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
                    transfer_get_total_params.TransferGetTotalParams,
                ),
            ),
            cast_to=TransferGetTotalResponse,
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
    ) -> TransferListByAssetAccountResponse:
        """
        This endpoint gives a summary of the transfers made by the user, grouped by
        asset account or lability.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/transfer/asset",
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
                    transfer_list_by_asset_account_params.TransferListByAssetAccountParams,
                ),
            ),
            cast_to=TransferListByAssetAccountResponse,
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
    ) -> TransferListByCategoryResponse:
        """
        This endpoint gives a summary of the transfers made by the user, grouped by
        (any) category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          categories: The categories to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/transfer/category",
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
                    transfer_list_by_category_params.TransferListByCategoryParams,
                ),
            ),
            cast_to=TransferListByCategoryResponse,
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
    ) -> TransferListByTagResponse:
        """
        This endpoint gives a summary of the transfers created by the user, grouped by
        (any) tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          tags: The tags to be included in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/transfer/tag",
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
                    transfer_list_by_tag_params.TransferListByTagParams,
                ),
            ),
            cast_to=TransferListByTagResponse,
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
    ) -> TransferListWithoutCategoryResponse:
        """
        This endpoint gives a summary of the transfers made by the user, including only
        transfers with no category.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers between those asset accounts /
              liabilities will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/transfer/no-category",
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
                    transfer_list_without_category_params.TransferListWithoutCategoryParams,
                ),
            ),
            cast_to=TransferListWithoutCategoryResponse,
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
    ) -> TransferListWithoutTagResponse:
        """
        This endpoint gives a summary of the transfers made by the user, including only
        transfers with no tag.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: The accounts to be included in the results. If you include ID's of asset
              accounts or liabilities, only transfers from those asset accounts / liabilities
              will be included. Other account ID's will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/insight/transfer/no-tag",
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
                    transfer_list_without_tag_params.TransferListWithoutTagParams,
                ),
            ),
            cast_to=TransferListWithoutTagResponse,
        )


class TransferResourceWithRawResponse:
    def __init__(self, transfer: TransferResource) -> None:
        self._transfer = transfer

        self.get_total = to_raw_response_wrapper(
            transfer.get_total,
        )
        self.list_by_asset_account = to_raw_response_wrapper(
            transfer.list_by_asset_account,
        )
        self.list_by_category = to_raw_response_wrapper(
            transfer.list_by_category,
        )
        self.list_by_tag = to_raw_response_wrapper(
            transfer.list_by_tag,
        )
        self.list_without_category = to_raw_response_wrapper(
            transfer.list_without_category,
        )
        self.list_without_tag = to_raw_response_wrapper(
            transfer.list_without_tag,
        )


class AsyncTransferResourceWithRawResponse:
    def __init__(self, transfer: AsyncTransferResource) -> None:
        self._transfer = transfer

        self.get_total = async_to_raw_response_wrapper(
            transfer.get_total,
        )
        self.list_by_asset_account = async_to_raw_response_wrapper(
            transfer.list_by_asset_account,
        )
        self.list_by_category = async_to_raw_response_wrapper(
            transfer.list_by_category,
        )
        self.list_by_tag = async_to_raw_response_wrapper(
            transfer.list_by_tag,
        )
        self.list_without_category = async_to_raw_response_wrapper(
            transfer.list_without_category,
        )
        self.list_without_tag = async_to_raw_response_wrapper(
            transfer.list_without_tag,
        )


class TransferResourceWithStreamingResponse:
    def __init__(self, transfer: TransferResource) -> None:
        self._transfer = transfer

        self.get_total = to_streamed_response_wrapper(
            transfer.get_total,
        )
        self.list_by_asset_account = to_streamed_response_wrapper(
            transfer.list_by_asset_account,
        )
        self.list_by_category = to_streamed_response_wrapper(
            transfer.list_by_category,
        )
        self.list_by_tag = to_streamed_response_wrapper(
            transfer.list_by_tag,
        )
        self.list_without_category = to_streamed_response_wrapper(
            transfer.list_without_category,
        )
        self.list_without_tag = to_streamed_response_wrapper(
            transfer.list_without_tag,
        )


class AsyncTransferResourceWithStreamingResponse:
    def __init__(self, transfer: AsyncTransferResource) -> None:
        self._transfer = transfer

        self.get_total = async_to_streamed_response_wrapper(
            transfer.get_total,
        )
        self.list_by_asset_account = async_to_streamed_response_wrapper(
            transfer.list_by_asset_account,
        )
        self.list_by_category = async_to_streamed_response_wrapper(
            transfer.list_by_category,
        )
        self.list_by_tag = async_to_streamed_response_wrapper(
            transfer.list_by_tag,
        )
        self.list_without_category = async_to_streamed_response_wrapper(
            transfer.list_without_category,
        )
        self.list_without_tag = async_to_streamed_response_wrapper(
            transfer.list_without_tag,
        )
