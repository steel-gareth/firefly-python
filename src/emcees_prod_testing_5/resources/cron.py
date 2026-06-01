# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import cron_run_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.cron_run_response import CronRunResponse

__all__ = ["CronResource", "AsyncCronResource"]


class CronResource(SyncAPIResource):
    """
    These endpoints deliver general system information, version- and meta information.
    """

    @cached_property
    def with_raw_response(self) -> CronResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return CronResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CronResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return CronResourceWithStreamingResponse(self)

    def run(
        self,
        cli_token: str,
        *,
        date: Union[str, date] | Omit = omit,
        force: bool | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CronRunResponse:
        """Firefly III has one endpoint for its various cron related tasks.

        Send a GET to
        this endpoint to run the cron. The cron requires the CLI token to be present.
        The cron job will fire for all users.

        Args:
          date: A date formatted YYYY-MM-DD. This can be used to make the cron job pretend it's
              running on another day.

          force: Forces the cron job to fire, regardless of whether it has fired before. This may
              result in double transactions or weird budgets, so be careful.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not cli_token:
            raise ValueError(f"Expected a non-empty value for `cli_token` but received {cli_token!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/cron/{cli_token}", cli_token=cli_token),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "force": force,
                    },
                    cron_run_params.CronRunParams,
                ),
            ),
            cast_to=CronRunResponse,
        )


class AsyncCronResource(AsyncAPIResource):
    """
    These endpoints deliver general system information, version- and meta information.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCronResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCronResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCronResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncCronResourceWithStreamingResponse(self)

    async def run(
        self,
        cli_token: str,
        *,
        date: Union[str, date] | Omit = omit,
        force: bool | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CronRunResponse:
        """Firefly III has one endpoint for its various cron related tasks.

        Send a GET to
        this endpoint to run the cron. The cron requires the CLI token to be present.
        The cron job will fire for all users.

        Args:
          date: A date formatted YYYY-MM-DD. This can be used to make the cron job pretend it's
              running on another day.

          force: Forces the cron job to fire, regardless of whether it has fired before. This may
              result in double transactions or weird budgets, so be careful.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not cli_token:
            raise ValueError(f"Expected a non-empty value for `cli_token` but received {cli_token!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/cron/{cli_token}", cli_token=cli_token),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "force": force,
                    },
                    cron_run_params.CronRunParams,
                ),
            ),
            cast_to=CronRunResponse,
        )


class CronResourceWithRawResponse:
    def __init__(self, cron: CronResource) -> None:
        self._cron = cron

        self.run = to_raw_response_wrapper(
            cron.run,
        )


class AsyncCronResourceWithRawResponse:
    def __init__(self, cron: AsyncCronResource) -> None:
        self._cron = cron

        self.run = async_to_raw_response_wrapper(
            cron.run,
        )


class CronResourceWithStreamingResponse:
    def __init__(self, cron: CronResource) -> None:
        self._cron = cron

        self.run = to_streamed_response_wrapper(
            cron.run,
        )


class AsyncCronResourceWithStreamingResponse:
    def __init__(self, cron: AsyncCronResource) -> None:
        self._cron = cron

        self.run = async_to_streamed_response_wrapper(
            cron.run,
        )
