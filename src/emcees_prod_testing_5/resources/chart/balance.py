# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
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
from ...types.chart import balance_retrieve_balance_params
from ..._base_client import make_request_options
from ...types.chart.balance_retrieve_balance_response import BalanceRetrieveBalanceResponse

__all__ = ["BalanceResource", "AsyncBalanceResource"]


class BalanceResource(SyncAPIResource):
    """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""

    @cached_property
    def with_raw_response(self) -> BalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return BalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return BalanceResourceWithStreamingResponse(self)

    def retrieve_balance(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        period: Literal["1D", "1W", "1M", "3M", "6M", "1Y"] | Omit = omit,
        preselected: Literal["empty", "all", "assets", "liabilities"] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceRetrieveBalanceResponse:
        """
        This endpoint returns the data required to generate a chart with balance
        information.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: Limit the chart to these asset accounts or liabilities. Only asset accounts and
              liabilities will be accepted. Other types will be silently dropped.

              This list of accounts will be OVERRULED by the `preselected` parameter.

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
            "/v1/chart/balance/balance",
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
                        "period": period,
                        "preselected": preselected,
                    },
                    balance_retrieve_balance_params.BalanceRetrieveBalanceParams,
                ),
            ),
            cast_to=BalanceRetrieveBalanceResponse,
        )


class AsyncBalanceResource(AsyncAPIResource):
    """The &quot;charts&quot; endpoints deliver optimised data for charts and graphs."""

    @cached_property
    def with_raw_response(self) -> AsyncBalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncBalanceResourceWithStreamingResponse(self)

    async def retrieve_balance(
        self,
        *,
        end: Union[str, date],
        start: Union[str, date],
        accounts: Iterable[int] | Omit = omit,
        period: Literal["1D", "1W", "1M", "3M", "6M", "1Y"] | Omit = omit,
        preselected: Literal["empty", "all", "assets", "liabilities"] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceRetrieveBalanceResponse:
        """
        This endpoint returns the data required to generate a chart with balance
        information.

        Args:
          end: A date formatted YYYY-MM-DD.

          start: A date formatted YYYY-MM-DD.

          accounts: Limit the chart to these asset accounts or liabilities. Only asset accounts and
              liabilities will be accepted. Other types will be silently dropped.

              This list of accounts will be OVERRULED by the `preselected` parameter.

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
            "/v1/chart/balance/balance",
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
                        "period": period,
                        "preselected": preselected,
                    },
                    balance_retrieve_balance_params.BalanceRetrieveBalanceParams,
                ),
            ),
            cast_to=BalanceRetrieveBalanceResponse,
        )


class BalanceResourceWithRawResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.retrieve_balance = to_raw_response_wrapper(
            balance.retrieve_balance,
        )


class AsyncBalanceResourceWithRawResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.retrieve_balance = async_to_raw_response_wrapper(
            balance.retrieve_balance,
        )


class BalanceResourceWithStreamingResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.retrieve_balance = to_streamed_response_wrapper(
            balance.retrieve_balance,
        )


class AsyncBalanceResourceWithStreamingResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.retrieve_balance = async_to_streamed_response_wrapper(
            balance.retrieve_balance,
        )
