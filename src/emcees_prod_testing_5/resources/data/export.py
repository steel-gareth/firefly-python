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
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.data import (
    ExportFileFilter,
    export_export_tags_params,
    export_export_bills_params,
    export_export_rules_params,
    export_export_budgets_params,
    export_export_accounts_params,
    export_export_recurring_params,
    export_export_categories_params,
    export_export_piggy_banks_params,
    export_export_transactions_params,
)
from ..._base_client import make_request_options
from ...types.data.export_file_filter import ExportFileFilter

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    """
    The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
    """

    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)

    def export_accounts(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export your accounts from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_accounts_params.ExportExportAccountsParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_bills(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export your bills from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/bills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_bills_params.ExportExportBillsParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_budgets(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export your budgets and associated budget data from
        Firefly III into a file. Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_budgets_params.ExportExportBudgetsParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_categories(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export your categories from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_categories_params.ExportExportCategoriesParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_piggy_banks(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """This endpoint allows you to export your piggy banks from Firefly III into a
        file.

        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/piggy-banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_piggy_banks_params.ExportExportPiggyBanksParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_recurring(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export your recurring transactions from Firefly III
        into a file. Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/recurring",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_recurring_params.ExportExportRecurringParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_rules(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export your rules and rule groups from Firefly III
        into a file. Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_rules_params.ExportExportRulesParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_tags(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export your tags from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, export_export_tags_params.ExportExportTagsParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_transactions(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: str | Omit = omit,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        This endpoint allows you to export transactions from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: Limit the export of transactions to these accounts only. Only asset accounts
              will be accepted. Other types will be silently dropped.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/data/export/transactions",
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
                        "type": type,
                    },
                    export_export_transactions_params.ExportExportTransactionsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncExportResource(AsyncAPIResource):
    """
    The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
    """

    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)

    async def export_accounts(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export your accounts from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, export_export_accounts_params.ExportExportAccountsParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_bills(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export your bills from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/bills",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, export_export_bills_params.ExportExportBillsParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_budgets(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export your budgets and associated budget data from
        Firefly III into a file. Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/budgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, export_export_budgets_params.ExportExportBudgetsParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_categories(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export your categories from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/categories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, export_export_categories_params.ExportExportCategoriesParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_piggy_banks(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """This endpoint allows you to export your piggy banks from Firefly III into a
        file.

        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/piggy-banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, export_export_piggy_banks_params.ExportExportPiggyBanksParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_recurring(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export your recurring transactions from Firefly III
        into a file. Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/recurring",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, export_export_recurring_params.ExportExportRecurringParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_rules(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export your rules and rule groups from Firefly III
        into a file. Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, export_export_rules_params.ExportExportRulesParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_tags(
        self,
        *,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export your tags from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, export_export_tags_params.ExportExportTagsParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_transactions(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: str | Omit = omit,
        type: ExportFileFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        This endpoint allows you to export transactions from Firefly III into a file.
        Currently supports CSV exports only.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: Limit the export of transactions to these accounts only. Only asset accounts
              will be accepted. Other types will be silently dropped.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/data/export/transactions",
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
                        "type": type,
                    },
                    export_export_transactions_params.ExportExportTransactionsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.export_accounts = to_custom_raw_response_wrapper(
            export.export_accounts,
            BinaryAPIResponse,
        )
        self.export_bills = to_custom_raw_response_wrapper(
            export.export_bills,
            BinaryAPIResponse,
        )
        self.export_budgets = to_custom_raw_response_wrapper(
            export.export_budgets,
            BinaryAPIResponse,
        )
        self.export_categories = to_custom_raw_response_wrapper(
            export.export_categories,
            BinaryAPIResponse,
        )
        self.export_piggy_banks = to_custom_raw_response_wrapper(
            export.export_piggy_banks,
            BinaryAPIResponse,
        )
        self.export_recurring = to_custom_raw_response_wrapper(
            export.export_recurring,
            BinaryAPIResponse,
        )
        self.export_rules = to_custom_raw_response_wrapper(
            export.export_rules,
            BinaryAPIResponse,
        )
        self.export_tags = to_custom_raw_response_wrapper(
            export.export_tags,
            BinaryAPIResponse,
        )
        self.export_transactions = to_custom_raw_response_wrapper(
            export.export_transactions,
            BinaryAPIResponse,
        )


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.export_accounts = async_to_custom_raw_response_wrapper(
            export.export_accounts,
            AsyncBinaryAPIResponse,
        )
        self.export_bills = async_to_custom_raw_response_wrapper(
            export.export_bills,
            AsyncBinaryAPIResponse,
        )
        self.export_budgets = async_to_custom_raw_response_wrapper(
            export.export_budgets,
            AsyncBinaryAPIResponse,
        )
        self.export_categories = async_to_custom_raw_response_wrapper(
            export.export_categories,
            AsyncBinaryAPIResponse,
        )
        self.export_piggy_banks = async_to_custom_raw_response_wrapper(
            export.export_piggy_banks,
            AsyncBinaryAPIResponse,
        )
        self.export_recurring = async_to_custom_raw_response_wrapper(
            export.export_recurring,
            AsyncBinaryAPIResponse,
        )
        self.export_rules = async_to_custom_raw_response_wrapper(
            export.export_rules,
            AsyncBinaryAPIResponse,
        )
        self.export_tags = async_to_custom_raw_response_wrapper(
            export.export_tags,
            AsyncBinaryAPIResponse,
        )
        self.export_transactions = async_to_custom_raw_response_wrapper(
            export.export_transactions,
            AsyncBinaryAPIResponse,
        )


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.export_accounts = to_custom_streamed_response_wrapper(
            export.export_accounts,
            StreamedBinaryAPIResponse,
        )
        self.export_bills = to_custom_streamed_response_wrapper(
            export.export_bills,
            StreamedBinaryAPIResponse,
        )
        self.export_budgets = to_custom_streamed_response_wrapper(
            export.export_budgets,
            StreamedBinaryAPIResponse,
        )
        self.export_categories = to_custom_streamed_response_wrapper(
            export.export_categories,
            StreamedBinaryAPIResponse,
        )
        self.export_piggy_banks = to_custom_streamed_response_wrapper(
            export.export_piggy_banks,
            StreamedBinaryAPIResponse,
        )
        self.export_recurring = to_custom_streamed_response_wrapper(
            export.export_recurring,
            StreamedBinaryAPIResponse,
        )
        self.export_rules = to_custom_streamed_response_wrapper(
            export.export_rules,
            StreamedBinaryAPIResponse,
        )
        self.export_tags = to_custom_streamed_response_wrapper(
            export.export_tags,
            StreamedBinaryAPIResponse,
        )
        self.export_transactions = to_custom_streamed_response_wrapper(
            export.export_transactions,
            StreamedBinaryAPIResponse,
        )


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.export_accounts = async_to_custom_streamed_response_wrapper(
            export.export_accounts,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_bills = async_to_custom_streamed_response_wrapper(
            export.export_bills,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_budgets = async_to_custom_streamed_response_wrapper(
            export.export_budgets,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_categories = async_to_custom_streamed_response_wrapper(
            export.export_categories,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_piggy_banks = async_to_custom_streamed_response_wrapper(
            export.export_piggy_banks,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_recurring = async_to_custom_streamed_response_wrapper(
            export.export_recurring,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_rules = async_to_custom_streamed_response_wrapper(
            export.export_rules,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_tags = async_to_custom_streamed_response_wrapper(
            export.export_tags,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_transactions = async_to_custom_streamed_response_wrapper(
            export.export_transactions,
            AsyncStreamedBinaryAPIResponse,
        )
