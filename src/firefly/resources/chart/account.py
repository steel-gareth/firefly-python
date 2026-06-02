# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

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
from ...types.chart import account_retrieve_overview_params
from ..._base_client import make_request_options
from ...types.chart.account_retrieve_overview_response import AccountRetrieveOverviewResponse

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""

    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)

    def retrieve_overview(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        period: Literal["1D", "1W", "1M", "3M", "6M", "1Y"] | Omit = omit,
        preselected: Literal["empty", "all", "assets", "liabilities"] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRetrieveOverviewResponse:
        """
        This endpoint returns the data required to generate a chart with basic asset
        account balance information. This is used on the dashboard.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          period: Optional period to group the data by. If not provided, it will default to '1M'
              or whatever is deemed relevant for the range provided.

              If you want to know which periods are available, see the enums or get the
              configuration value: `GET /api/v1/configuration/firefly.valid_view_ranges`

          preselected: Optional set of preselected accounts to limit the chart to. This may be easier
              than submitting all asset accounts manually, for example. If you want to know
              which selection are available, see the enums here or get the configuration
              value: `GET /api/v1/configuration/firefly.preselected_accounts`

              - `empty`: do not do a pre-selection
              - `all`: select all asset and all liability accounts
              - `assets`: select all asset accounts
              - `liabilities`: select all liability accounts

              If no accounts are found, the user's "frontpage accounts" preference will be
              used. If that is empty, all asset accounts will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/chart/account/overview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "period": period,
                        "preselected": preselected,
                    },
                    account_retrieve_overview_params.AccountRetrieveOverviewParams,
                ),
            ),
            cast_to=AccountRetrieveOverviewResponse,
        )


class AsyncAccountResource(AsyncAPIResource):
    """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""

    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)

    async def retrieve_overview(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        period: Literal["1D", "1W", "1M", "3M", "6M", "1Y"] | Omit = omit,
        preselected: Literal["empty", "all", "assets", "liabilities"] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRetrieveOverviewResponse:
        """
        This endpoint returns the data required to generate a chart with basic asset
        account balance information. This is used on the dashboard.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          period: Optional period to group the data by. If not provided, it will default to '1M'
              or whatever is deemed relevant for the range provided.

              If you want to know which periods are available, see the enums or get the
              configuration value: `GET /api/v1/configuration/firefly.valid_view_ranges`

          preselected: Optional set of preselected accounts to limit the chart to. This may be easier
              than submitting all asset accounts manually, for example. If you want to know
              which selection are available, see the enums here or get the configuration
              value: `GET /api/v1/configuration/firefly.preselected_accounts`

              - `empty`: do not do a pre-selection
              - `all`: select all asset and all liability accounts
              - `assets`: select all asset accounts
              - `liabilities`: select all liability accounts

              If no accounts are found, the user's "frontpage accounts" preference will be
              used. If that is empty, all asset accounts will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/chart/account/overview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                        "period": period,
                        "preselected": preselected,
                    },
                    account_retrieve_overview_params.AccountRetrieveOverviewParams,
                ),
            ),
            cast_to=AccountRetrieveOverviewResponse,
        )


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.retrieve_overview = to_raw_response_wrapper(
            account.retrieve_overview,
        )


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.retrieve_overview = async_to_raw_response_wrapper(
            account.retrieve_overview,
        )


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.retrieve_overview = to_streamed_response_wrapper(
            account.retrieve_overview,
        )


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.retrieve_overview = async_to_streamed_response_wrapper(
            account.retrieve_overview,
        )
