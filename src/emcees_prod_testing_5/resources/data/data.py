# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from .export import (
    ExportResource,
    AsyncExportResource,
    ExportResourceWithRawResponse,
    AsyncExportResourceWithRawResponse,
    ExportResourceWithStreamingResponse,
    AsyncExportResourceWithStreamingResponse,
)
from ...types import data_destroy_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    """
    The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
    """

    @cached_property
    def bulk(self) -> BulkResource:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return BulkResource(self._client)

    @cached_property
    def export(self) -> ExportResource:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return ExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return DataResourceWithStreamingResponse(self)

    def destroy(
        self,
        *,
        objects: Literal[
            "not_assets_liabilities",
            "budgets",
            "bills",
            "piggy_banks",
            "rules",
            "recurring",
            "categories",
            "tags",
            "object_groups",
            "accounts",
            "asset_accounts",
            "expense_accounts",
            "revenue_accounts",
            "liabilities",
            "transactions",
            "withdrawals",
            "deposits",
            "transfers",
        ],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """A call to this endpoint deletes the requested data type.

        Use it with care and
        always with user permission. The demo user is incapable of using this endpoint.

        Args:
          objects: The type of data that you wish to destroy. You can only use one at a time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            "/v1/data/destroy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"objects": objects}, data_destroy_params.DataDestroyParams),
            ),
            cast_to=NoneType,
        )

    def purge(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """A call to this endpoint purges all previously deleted data.

        Use it with care and
        always with user permission. The demo user is incapable of using this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            "/v1/data/purge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDataResource(AsyncAPIResource):
    """
    The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
    """

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return AsyncBulkResource(self._client)

    @cached_property
    def export(self) -> AsyncExportResource:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return AsyncExportResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncDataResourceWithStreamingResponse(self)

    async def destroy(
        self,
        *,
        objects: Literal[
            "not_assets_liabilities",
            "budgets",
            "bills",
            "piggy_banks",
            "rules",
            "recurring",
            "categories",
            "tags",
            "object_groups",
            "accounts",
            "asset_accounts",
            "expense_accounts",
            "revenue_accounts",
            "liabilities",
            "transactions",
            "withdrawals",
            "deposits",
            "transfers",
        ],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """A call to this endpoint deletes the requested data type.

        Use it with care and
        always with user permission. The demo user is incapable of using this endpoint.

        Args:
          objects: The type of data that you wish to destroy. You can only use one at a time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            "/v1/data/destroy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"objects": objects}, data_destroy_params.DataDestroyParams),
            ),
            cast_to=NoneType,
        )

    async def purge(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """A call to this endpoint purges all previously deleted data.

        Use it with care and
        always with user permission. The demo user is incapable of using this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            "/v1/data/purge",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.destroy = to_raw_response_wrapper(
            data.destroy,
        )
        self.purge = to_raw_response_wrapper(
            data.purge,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return BulkResourceWithRawResponse(self._data.bulk)

    @cached_property
    def export(self) -> ExportResourceWithRawResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return ExportResourceWithRawResponse(self._data.export)


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.destroy = async_to_raw_response_wrapper(
            data.destroy,
        )
        self.purge = async_to_raw_response_wrapper(
            data.purge,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return AsyncBulkResourceWithRawResponse(self._data.bulk)

    @cached_property
    def export(self) -> AsyncExportResourceWithRawResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return AsyncExportResourceWithRawResponse(self._data.export)


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.destroy = to_streamed_response_wrapper(
            data.destroy,
        )
        self.purge = to_streamed_response_wrapper(
            data.purge,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return BulkResourceWithStreamingResponse(self._data.bulk)

    @cached_property
    def export(self) -> ExportResourceWithStreamingResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return ExportResourceWithStreamingResponse(self._data.export)


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.destroy = async_to_streamed_response_wrapper(
            data.destroy,
        )
        self.purge = async_to_streamed_response_wrapper(
            data.purge,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return AsyncBulkResourceWithStreamingResponse(self._data.bulk)

    @cached_property
    def export(self) -> AsyncExportResourceWithStreamingResponse:
        """
        The &quot;data&quot;-endpoints manage generic Firefly III and user-specific data.
        """
        return AsyncExportResourceWithStreamingResponse(self._data.export)
