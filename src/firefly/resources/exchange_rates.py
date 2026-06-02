# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date

import httpx

from ..types import (
    exchange_rate_list_params,
    exchange_rate_create_params,
    exchange_rate_update_params,
    exchange_rate_retrieve_params,
    exchange_rate_create_by_date_params,
    exchange_rate_update_by_date_params,
    exchange_rate_retrieve_by_date_params,
    exchange_rate_list_by_currencies_params,
    exchange_rate_create_by_currencies_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.currency_exchange_rate_array import CurrencyExchangeRateArray
from ..types.currency_exchange_rate_single import CurrencyExchangeRateSingle

__all__ = ["ExchangeRatesResource", "AsyncExchangeRatesResource"]


class ExchangeRatesResource(SyncAPIResource):
    """All currency exchange rates."""

    @cached_property
    def with_raw_response(self) -> ExchangeRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return ExchangeRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExchangeRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return ExchangeRatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        date: Union[str, date],
        from_: str,
        rates: object,
        to: str,
        rate: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateSingle:
        """Stores a new exchange rate.

        The data required can be submitted as a JSON body or
        as a list of parameters.

        Args:
          date: The date to which the exchange rate is applicable.

          from_: The base currency code.

          to: The destination currency code.

          rate: The exchange rate from the base currency to the destination currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/exchange-rates",
            body=maybe_transform(
                {
                    "date": date,
                    "from_": from_,
                    "rates": rates,
                    "to": to,
                    "rate": rate,
                },
                exchange_rate_create_params.ExchangeRateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateSingle,
        )

    def retrieve(
        self,
        id: str,
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
    ) -> CurrencyExchangeRateSingle:
        """
        List a single specific exchange rate by its ID.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/exchange-rates/{id}", id=id),
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
                    exchange_rate_retrieve_params.ExchangeRateRetrieveParams,
                ),
            ),
            cast_to=CurrencyExchangeRateSingle,
        )

    def update(
        self,
        id: str,
        *,
        date: Union[str, date],
        rate: str,
        from_: Optional[str] | Omit = omit,
        to: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateSingle:
        """Used to update a single currency exchange rate by its ID.

        Including the from/to
        currency is optional.

        Args:
          date: The date to which the exchange rate is applicable.

          rate: The exchange rate from the base currency to the destination currency.

          from_: The base currency code.

          to: The destination currency code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._put(
            path_template("/v1/exchange-rates/{id}", id=id),
            body=maybe_transform(
                {
                    "date": date,
                    "rate": rate,
                    "from_": from_,
                    "to": to,
                },
                exchange_rate_update_params.ExchangeRateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateSingle,
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
    ) -> CurrencyExchangeRateArray:
        """
        List exchange rates that Firefly III knows.

        Args:
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
            "/v1/exchange-rates",
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
                    exchange_rate_list_params.ExchangeRateListParams,
                ),
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    def delete(
        self,
        id: str,
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
        Delete a specific currency exchange rate by its internal ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/exchange-rates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_by_currencies(
        self,
        to: str,
        *,
        from_: str,
        body: Dict[str, str],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """Stores a new set of exchange rates for this pair.

        The date is variable, and the
        data required can be submitted as a JSON body.

        Args:
          body: The actual entries for this data set. They 'key' value is the date in
              YYYY-MM-DD. The value is the exchange rate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/exchange-rates/by-currencies/{from_}/{to}", from_=from_, to=to),
            body=maybe_transform(body, exchange_rate_create_by_currencies_params.ExchangeRateCreateByCurrenciesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    def create_by_date(
        self,
        path_date: str,
        *,
        body_date: object,
        from_: str,
        rates: Dict[str, str],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """Stores a new set of exchange rates.

        The date is fixed (in the URL parameter) and
        the data required can be submitted as a JSON body.

        Args:
          from_: The 'from'-currency

          rates: The actual entries for this data set. They 'key' value is 'to' currency. The
              value is the exchange rate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_date:
            raise ValueError(f"Expected a non-empty value for `path_date` but received {path_date!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/exchange-rates/by-date/{path_date}", path_date=path_date),
            body=maybe_transform(
                {
                    "body_date": body_date,
                    "from_": from_,
                    "rates": rates,
                },
                exchange_rate_create_by_date_params.ExchangeRateCreateByDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    def delete_all_by_currencies(
        self,
        to: str,
        *,
        from_: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes ALL currency exchange rates from 'from' to 'to'.

        It's important to know
        that the reverse exchange rates (from 'to' to 'from') will not be deleted and
        Firefly III will still be able to infer the correct exchange rate from the
        reverse one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/exchange-rates/{from_}/{to}", from_=from_, to=to),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_by_date(
        self,
        date: str,
        *,
        from_: str,
        to: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the currency exchange rate from 'from' to 'to' on the specified date.
        It's important to know that the reverse exchange rate (from 'to' to 'from') will
        not be deleted and Firefly III will still be able to infer the correct exchange
        rate from the reverse one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/exchange-rates/{from_}/{to}/{date}", from_=from_, to=to, date=date),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_by_currencies(
        self,
        to: str,
        *,
        from_: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """
        List all exchange rates from/to the mentioned currencies.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/exchange-rates/{from_}/{to}", from_=from_, to=to),
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
                    exchange_rate_list_by_currencies_params.ExchangeRateListByCurrenciesParams,
                ),
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    def retrieve_by_date(
        self,
        date: str,
        *,
        from_: str,
        to: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """
        List the exchange rate for the from and to-currency on the requested date.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/exchange-rates/{from_}/{to}/{date}", from_=from_, to=to, date=date),
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
                    exchange_rate_retrieve_by_date_params.ExchangeRateRetrieveByDateParams,
                ),
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    def update_by_date(
        self,
        date: str,
        *,
        from_: str,
        to: str,
        rate: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateSingle:
        """
        Used to update a single currency exchange rate by its currency codes and date

        Args:
          rate: The exchange rate from the base currency to the destination currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._put(
            path_template("/v1/exchange-rates/{from_}/{to}/{date}", from_=from_, to=to, date=date),
            body=maybe_transform({"rate": rate}, exchange_rate_update_by_date_params.ExchangeRateUpdateByDateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateSingle,
        )


class AsyncExchangeRatesResource(AsyncAPIResource):
    """All currency exchange rates."""

    @cached_property
    def with_raw_response(self) -> AsyncExchangeRatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExchangeRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExchangeRatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncExchangeRatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        date: Union[str, date],
        from_: str,
        rates: object,
        to: str,
        rate: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateSingle:
        """Stores a new exchange rate.

        The data required can be submitted as a JSON body or
        as a list of parameters.

        Args:
          date: The date to which the exchange rate is applicable.

          from_: The base currency code.

          to: The destination currency code.

          rate: The exchange rate from the base currency to the destination currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/exchange-rates",
            body=await async_maybe_transform(
                {
                    "date": date,
                    "from_": from_,
                    "rates": rates,
                    "to": to,
                    "rate": rate,
                },
                exchange_rate_create_params.ExchangeRateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateSingle,
        )

    async def retrieve(
        self,
        id: str,
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
    ) -> CurrencyExchangeRateSingle:
        """
        List a single specific exchange rate by its ID.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/exchange-rates/{id}", id=id),
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
                    exchange_rate_retrieve_params.ExchangeRateRetrieveParams,
                ),
            ),
            cast_to=CurrencyExchangeRateSingle,
        )

    async def update(
        self,
        id: str,
        *,
        date: Union[str, date],
        rate: str,
        from_: Optional[str] | Omit = omit,
        to: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateSingle:
        """Used to update a single currency exchange rate by its ID.

        Including the from/to
        currency is optional.

        Args:
          date: The date to which the exchange rate is applicable.

          rate: The exchange rate from the base currency to the destination currency.

          from_: The base currency code.

          to: The destination currency code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._put(
            path_template("/v1/exchange-rates/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "date": date,
                    "rate": rate,
                    "from_": from_,
                    "to": to,
                },
                exchange_rate_update_params.ExchangeRateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateSingle,
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
    ) -> CurrencyExchangeRateArray:
        """
        List exchange rates that Firefly III knows.

        Args:
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
            "/v1/exchange-rates",
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
                    exchange_rate_list_params.ExchangeRateListParams,
                ),
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    async def delete(
        self,
        id: str,
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
        Delete a specific currency exchange rate by its internal ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/exchange-rates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_by_currencies(
        self,
        to: str,
        *,
        from_: str,
        body: Dict[str, str],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """Stores a new set of exchange rates for this pair.

        The date is variable, and the
        data required can be submitted as a JSON body.

        Args:
          body: The actual entries for this data set. They 'key' value is the date in
              YYYY-MM-DD. The value is the exchange rate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/exchange-rates/by-currencies/{from_}/{to}", from_=from_, to=to),
            body=await async_maybe_transform(
                body, exchange_rate_create_by_currencies_params.ExchangeRateCreateByCurrenciesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    async def create_by_date(
        self,
        path_date: str,
        *,
        body_date: object,
        from_: str,
        rates: Dict[str, str],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """Stores a new set of exchange rates.

        The date is fixed (in the URL parameter) and
        the data required can be submitted as a JSON body.

        Args:
          from_: The 'from'-currency

          rates: The actual entries for this data set. They 'key' value is 'to' currency. The
              value is the exchange rate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_date:
            raise ValueError(f"Expected a non-empty value for `path_date` but received {path_date!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/exchange-rates/by-date/{path_date}", path_date=path_date),
            body=await async_maybe_transform(
                {
                    "body_date": body_date,
                    "from_": from_,
                    "rates": rates,
                },
                exchange_rate_create_by_date_params.ExchangeRateCreateByDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    async def delete_all_by_currencies(
        self,
        to: str,
        *,
        from_: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes ALL currency exchange rates from 'from' to 'to'.

        It's important to know
        that the reverse exchange rates (from 'to' to 'from') will not be deleted and
        Firefly III will still be able to infer the correct exchange rate from the
        reverse one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/exchange-rates/{from_}/{to}", from_=from_, to=to),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_by_date(
        self,
        date: str,
        *,
        from_: str,
        to: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the currency exchange rate from 'from' to 'to' on the specified date.
        It's important to know that the reverse exchange rate (from 'to' to 'from') will
        not be deleted and Firefly III will still be able to infer the correct exchange
        rate from the reverse one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/exchange-rates/{from_}/{to}/{date}", from_=from_, to=to, date=date),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_by_currencies(
        self,
        to: str,
        *,
        from_: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """
        List all exchange rates from/to the mentioned currencies.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/exchange-rates/{from_}/{to}", from_=from_, to=to),
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
                    exchange_rate_list_by_currencies_params.ExchangeRateListByCurrenciesParams,
                ),
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    async def retrieve_by_date(
        self,
        date: str,
        *,
        from_: str,
        to: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateArray:
        """
        List the exchange rate for the from and to-currency on the requested date.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/exchange-rates/{from_}/{to}/{date}", from_=from_, to=to, date=date),
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
                    exchange_rate_retrieve_by_date_params.ExchangeRateRetrieveByDateParams,
                ),
            ),
            cast_to=CurrencyExchangeRateArray,
        )

    async def update_by_date(
        self,
        date: str,
        *,
        from_: str,
        to: str,
        rate: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyExchangeRateSingle:
        """
        Used to update a single currency exchange rate by its currency codes and date

        Args:
          rate: The exchange rate from the base currency to the destination currency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_:
            raise ValueError(f"Expected a non-empty value for `from_` but received {from_!r}")
        if not to:
            raise ValueError(f"Expected a non-empty value for `to` but received {to!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._put(
            path_template("/v1/exchange-rates/{from_}/{to}/{date}", from_=from_, to=to, date=date),
            body=await async_maybe_transform(
                {"rate": rate}, exchange_rate_update_by_date_params.ExchangeRateUpdateByDateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrencyExchangeRateSingle,
        )


class ExchangeRatesResourceWithRawResponse:
    def __init__(self, exchange_rates: ExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.create = to_raw_response_wrapper(
            exchange_rates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exchange_rates.retrieve,
        )
        self.update = to_raw_response_wrapper(
            exchange_rates.update,
        )
        self.list = to_raw_response_wrapper(
            exchange_rates.list,
        )
        self.delete = to_raw_response_wrapper(
            exchange_rates.delete,
        )
        self.create_by_currencies = to_raw_response_wrapper(
            exchange_rates.create_by_currencies,
        )
        self.create_by_date = to_raw_response_wrapper(
            exchange_rates.create_by_date,
        )
        self.delete_all_by_currencies = to_raw_response_wrapper(
            exchange_rates.delete_all_by_currencies,
        )
        self.delete_by_date = to_raw_response_wrapper(
            exchange_rates.delete_by_date,
        )
        self.list_by_currencies = to_raw_response_wrapper(
            exchange_rates.list_by_currencies,
        )
        self.retrieve_by_date = to_raw_response_wrapper(
            exchange_rates.retrieve_by_date,
        )
        self.update_by_date = to_raw_response_wrapper(
            exchange_rates.update_by_date,
        )


class AsyncExchangeRatesResourceWithRawResponse:
    def __init__(self, exchange_rates: AsyncExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.create = async_to_raw_response_wrapper(
            exchange_rates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exchange_rates.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            exchange_rates.update,
        )
        self.list = async_to_raw_response_wrapper(
            exchange_rates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            exchange_rates.delete,
        )
        self.create_by_currencies = async_to_raw_response_wrapper(
            exchange_rates.create_by_currencies,
        )
        self.create_by_date = async_to_raw_response_wrapper(
            exchange_rates.create_by_date,
        )
        self.delete_all_by_currencies = async_to_raw_response_wrapper(
            exchange_rates.delete_all_by_currencies,
        )
        self.delete_by_date = async_to_raw_response_wrapper(
            exchange_rates.delete_by_date,
        )
        self.list_by_currencies = async_to_raw_response_wrapper(
            exchange_rates.list_by_currencies,
        )
        self.retrieve_by_date = async_to_raw_response_wrapper(
            exchange_rates.retrieve_by_date,
        )
        self.update_by_date = async_to_raw_response_wrapper(
            exchange_rates.update_by_date,
        )


class ExchangeRatesResourceWithStreamingResponse:
    def __init__(self, exchange_rates: ExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.create = to_streamed_response_wrapper(
            exchange_rates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            exchange_rates.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            exchange_rates.update,
        )
        self.list = to_streamed_response_wrapper(
            exchange_rates.list,
        )
        self.delete = to_streamed_response_wrapper(
            exchange_rates.delete,
        )
        self.create_by_currencies = to_streamed_response_wrapper(
            exchange_rates.create_by_currencies,
        )
        self.create_by_date = to_streamed_response_wrapper(
            exchange_rates.create_by_date,
        )
        self.delete_all_by_currencies = to_streamed_response_wrapper(
            exchange_rates.delete_all_by_currencies,
        )
        self.delete_by_date = to_streamed_response_wrapper(
            exchange_rates.delete_by_date,
        )
        self.list_by_currencies = to_streamed_response_wrapper(
            exchange_rates.list_by_currencies,
        )
        self.retrieve_by_date = to_streamed_response_wrapper(
            exchange_rates.retrieve_by_date,
        )
        self.update_by_date = to_streamed_response_wrapper(
            exchange_rates.update_by_date,
        )


class AsyncExchangeRatesResourceWithStreamingResponse:
    def __init__(self, exchange_rates: AsyncExchangeRatesResource) -> None:
        self._exchange_rates = exchange_rates

        self.create = async_to_streamed_response_wrapper(
            exchange_rates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            exchange_rates.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            exchange_rates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            exchange_rates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            exchange_rates.delete,
        )
        self.create_by_currencies = async_to_streamed_response_wrapper(
            exchange_rates.create_by_currencies,
        )
        self.create_by_date = async_to_streamed_response_wrapper(
            exchange_rates.create_by_date,
        )
        self.delete_all_by_currencies = async_to_streamed_response_wrapper(
            exchange_rates.delete_all_by_currencies,
        )
        self.delete_by_date = async_to_streamed_response_wrapper(
            exchange_rates.delete_by_date,
        )
        self.list_by_currencies = async_to_streamed_response_wrapper(
            exchange_rates.list_by_currencies,
        )
        self.retrieve_by_date = async_to_streamed_response_wrapper(
            exchange_rates.retrieve_by_date,
        )
        self.update_by_date = async_to_streamed_response_wrapper(
            exchange_rates.update_by_date,
        )
