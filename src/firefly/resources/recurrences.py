# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date

import httpx

from ..types import (
    TransactionTypeFilter,
    RecurrenceTransactionType,
    recurrence_list_params,
    recurrence_create_params,
    recurrence_update_params,
    recurrence_list_transactions_params,
    recurrence_trigger_transaction_params,
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
from ..types.recurrence_array import RecurrenceArray
from ..types.recurrence_single import RecurrenceSingle
from ..types.transaction_array import TransactionArray
from ..types.transaction_type_filter import TransactionTypeFilter
from ..types.recurrence_transaction_type import RecurrenceTransactionType

__all__ = ["RecurrencesResource", "AsyncRecurrencesResource"]


class RecurrencesResource(SyncAPIResource):
    """
    Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
    """

    @cached_property
    def with_raw_response(self) -> RecurrencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return RecurrencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecurrencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return RecurrencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        first_date: Union[str, date],
        repeat_until: Union[str, date, None],
        repetitions: Iterable[recurrence_create_params.Repetition],
        title: str,
        transactions: Iterable[recurrence_create_params.Transaction],
        type: RecurrenceTransactionType,
        active: bool | Omit = omit,
        apply_rules: bool | Omit = omit,
        description: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        nr_of_repetitions: Optional[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecurrenceSingle:
        """Creates a new recurring transaction.

        The data required can be submitted as a
        JSON body or as a list of parameters.

        Args:
          first_date: First time the recurring transaction will fire. Must be after today.

          repeat_until: Date until the recurring transaction can fire. Use either this field or
              repetitions.

          active: If the recurrence is even active.

          apply_rules: Whether or not to fire the rules after the creation of a transaction.

          description: Not to be confused with the description of the actual transaction(s) being
              created.

          nr_of_repetitions: Max number of created transactions. Use either this field or repeat_until.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/recurrences",
            body=maybe_transform(
                {
                    "first_date": first_date,
                    "repeat_until": repeat_until,
                    "repetitions": repetitions,
                    "title": title,
                    "transactions": transactions,
                    "type": type,
                    "active": active,
                    "apply_rules": apply_rules,
                    "description": description,
                    "notes": notes,
                    "nr_of_repetitions": nr_of_repetitions,
                },
                recurrence_create_params.RecurrenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurrenceSingle,
        )

    def retrieve(
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
    ) -> RecurrenceSingle:
        """
        Get a single recurring transaction.

        Args:
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
            path_template("/v1/recurrences/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurrenceSingle,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        apply_rules: bool | Omit = omit,
        description: str | Omit = omit,
        first_date: Union[str, date] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        nr_of_repetitions: Optional[int] | Omit = omit,
        repeat_until: Union[str, date, None] | Omit = omit,
        repetitions: Iterable[recurrence_update_params.Repetition] | Omit = omit,
        title: str | Omit = omit,
        transactions: Iterable[recurrence_update_params.Transaction] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecurrenceSingle:
        """
        Update existing recurring transaction.

        Args:
          active: If the recurrence is even active.

          apply_rules: Whether or not to fire the rules after the creation of a transaction.

          description: Not to be confused with the description of the actual transaction(s) being
              created.

          first_date: First time the recurring transaction will fire.

          nr_of_repetitions: Max number of created transactions. Use either this field or repeat_until.

          repeat_until: Date until when the recurring transaction can fire. After that date, it's
              basically inactive. Use either this field or repetitions.

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
            path_template("/v1/recurrences/{id}", id=id),
            body=maybe_transform(
                {
                    "active": active,
                    "apply_rules": apply_rules,
                    "description": description,
                    "first_date": first_date,
                    "notes": notes,
                    "nr_of_repetitions": nr_of_repetitions,
                    "repeat_until": repeat_until,
                    "repetitions": repetitions,
                    "title": title,
                    "transactions": transactions,
                },
                recurrence_update_params.RecurrenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurrenceSingle,
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
    ) -> RecurrenceArray:
        """List all recurring transactions.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/recurrences",
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
                    recurrence_list_params.RecurrenceListParams,
                ),
            ),
            cast_to=RecurrenceArray,
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
        """Delete a recurring transaction.

        Transactions created by the recurring
        transaction will not be deleted.

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
            path_template("/v1/recurrences/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_transactions(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        List all transactions created by a recurring transaction, optionally limited to
        the date ranges specified.

        Args:
          end: A date formatted YYYY-MM-DD. Both the start and end date must be present.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD. Both the start and end date must be present.

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
            path_template("/v1/recurrences/{id}/transactions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                        "type": type,
                    },
                    recurrence_list_transactions_params.RecurrenceListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    def trigger_transaction(
        self,
        id: str,
        *,
        date: Union[str, date],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """Trigger the creation of a transaction for a specific recurring transaction.

        All
        recurrences have a set of future occurrences. For those moments, you can trigger
        the creation of the transaction. That means the transaction will be created NOW,
        instead of on the indicated date. The transaction will be dated to _today_.

        So, if you recurring transaction that occurs every Monday, you can trigger the
        creation of a transaction for Monday in two weeks, today. On that Monday two
        weeks from now, no transaction will be created. Instead, the transaction is
        created right now, and dated _today_.

        Args:
          date: A date formatted YYYY-MM-DD. This is the date for which you want the recurrence
              to fire. You can take the date from the list of occurrences in the recurring
              transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/recurrences/{id}/trigger", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"date": date}, recurrence_trigger_transaction_params.RecurrenceTriggerTransactionParams
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncRecurrencesResource(AsyncAPIResource):
    """
    Use these endpoints to manage the user&#039;s recurring transactions, trigger the creation of transactions and manage the settings.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRecurrencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecurrencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecurrencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncRecurrencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        first_date: Union[str, date],
        repeat_until: Union[str, date, None],
        repetitions: Iterable[recurrence_create_params.Repetition],
        title: str,
        transactions: Iterable[recurrence_create_params.Transaction],
        type: RecurrenceTransactionType,
        active: bool | Omit = omit,
        apply_rules: bool | Omit = omit,
        description: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        nr_of_repetitions: Optional[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecurrenceSingle:
        """Creates a new recurring transaction.

        The data required can be submitted as a
        JSON body or as a list of parameters.

        Args:
          first_date: First time the recurring transaction will fire. Must be after today.

          repeat_until: Date until the recurring transaction can fire. Use either this field or
              repetitions.

          active: If the recurrence is even active.

          apply_rules: Whether or not to fire the rules after the creation of a transaction.

          description: Not to be confused with the description of the actual transaction(s) being
              created.

          nr_of_repetitions: Max number of created transactions. Use either this field or repeat_until.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/recurrences",
            body=await async_maybe_transform(
                {
                    "first_date": first_date,
                    "repeat_until": repeat_until,
                    "repetitions": repetitions,
                    "title": title,
                    "transactions": transactions,
                    "type": type,
                    "active": active,
                    "apply_rules": apply_rules,
                    "description": description,
                    "notes": notes,
                    "nr_of_repetitions": nr_of_repetitions,
                },
                recurrence_create_params.RecurrenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurrenceSingle,
        )

    async def retrieve(
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
    ) -> RecurrenceSingle:
        """
        Get a single recurring transaction.

        Args:
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
            path_template("/v1/recurrences/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurrenceSingle,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        apply_rules: bool | Omit = omit,
        description: str | Omit = omit,
        first_date: Union[str, date] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        nr_of_repetitions: Optional[int] | Omit = omit,
        repeat_until: Union[str, date, None] | Omit = omit,
        repetitions: Iterable[recurrence_update_params.Repetition] | Omit = omit,
        title: str | Omit = omit,
        transactions: Iterable[recurrence_update_params.Transaction] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecurrenceSingle:
        """
        Update existing recurring transaction.

        Args:
          active: If the recurrence is even active.

          apply_rules: Whether or not to fire the rules after the creation of a transaction.

          description: Not to be confused with the description of the actual transaction(s) being
              created.

          first_date: First time the recurring transaction will fire.

          nr_of_repetitions: Max number of created transactions. Use either this field or repeat_until.

          repeat_until: Date until when the recurring transaction can fire. After that date, it's
              basically inactive. Use either this field or repetitions.

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
            path_template("/v1/recurrences/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "apply_rules": apply_rules,
                    "description": description,
                    "first_date": first_date,
                    "notes": notes,
                    "nr_of_repetitions": nr_of_repetitions,
                    "repeat_until": repeat_until,
                    "repetitions": repetitions,
                    "title": title,
                    "transactions": transactions,
                },
                recurrence_update_params.RecurrenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurrenceSingle,
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
    ) -> RecurrenceArray:
        """List all recurring transactions.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/recurrences",
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
                    recurrence_list_params.RecurrenceListParams,
                ),
            ),
            cast_to=RecurrenceArray,
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
        """Delete a recurring transaction.

        Transactions created by the recurring
        transaction will not be deleted.

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
            path_template("/v1/recurrences/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_transactions(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        List all transactions created by a recurring transaction, optionally limited to
        the date ranges specified.

        Args:
          end: A date formatted YYYY-MM-DD. Both the start and end date must be present.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD. Both the start and end date must be present.

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
            path_template("/v1/recurrences/{id}/transactions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                        "type": type,
                    },
                    recurrence_list_transactions_params.RecurrenceListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    async def trigger_transaction(
        self,
        id: str,
        *,
        date: Union[str, date],
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """Trigger the creation of a transaction for a specific recurring transaction.

        All
        recurrences have a set of future occurrences. For those moments, you can trigger
        the creation of the transaction. That means the transaction will be created NOW,
        instead of on the indicated date. The transaction will be dated to _today_.

        So, if you recurring transaction that occurs every Monday, you can trigger the
        creation of a transaction for Monday in two weeks, today. On that Monday two
        weeks from now, no transaction will be created. Instead, the transaction is
        created right now, and dated _today_.

        Args:
          date: A date formatted YYYY-MM-DD. This is the date for which you want the recurrence
              to fire. You can take the date from the list of occurrences in the recurring
              transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/recurrences/{id}/trigger", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, recurrence_trigger_transaction_params.RecurrenceTriggerTransactionParams
                ),
            ),
            cast_to=TransactionArray,
        )


class RecurrencesResourceWithRawResponse:
    def __init__(self, recurrences: RecurrencesResource) -> None:
        self._recurrences = recurrences

        self.create = to_raw_response_wrapper(
            recurrences.create,
        )
        self.retrieve = to_raw_response_wrapper(
            recurrences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            recurrences.update,
        )
        self.list = to_raw_response_wrapper(
            recurrences.list,
        )
        self.delete = to_raw_response_wrapper(
            recurrences.delete,
        )
        self.list_transactions = to_raw_response_wrapper(
            recurrences.list_transactions,
        )
        self.trigger_transaction = to_raw_response_wrapper(
            recurrences.trigger_transaction,
        )


class AsyncRecurrencesResourceWithRawResponse:
    def __init__(self, recurrences: AsyncRecurrencesResource) -> None:
        self._recurrences = recurrences

        self.create = async_to_raw_response_wrapper(
            recurrences.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            recurrences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            recurrences.update,
        )
        self.list = async_to_raw_response_wrapper(
            recurrences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            recurrences.delete,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            recurrences.list_transactions,
        )
        self.trigger_transaction = async_to_raw_response_wrapper(
            recurrences.trigger_transaction,
        )


class RecurrencesResourceWithStreamingResponse:
    def __init__(self, recurrences: RecurrencesResource) -> None:
        self._recurrences = recurrences

        self.create = to_streamed_response_wrapper(
            recurrences.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            recurrences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            recurrences.update,
        )
        self.list = to_streamed_response_wrapper(
            recurrences.list,
        )
        self.delete = to_streamed_response_wrapper(
            recurrences.delete,
        )
        self.list_transactions = to_streamed_response_wrapper(
            recurrences.list_transactions,
        )
        self.trigger_transaction = to_streamed_response_wrapper(
            recurrences.trigger_transaction,
        )


class AsyncRecurrencesResourceWithStreamingResponse:
    def __init__(self, recurrences: AsyncRecurrencesResource) -> None:
        self._recurrences = recurrences

        self.create = async_to_streamed_response_wrapper(
            recurrences.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            recurrences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            recurrences.update,
        )
        self.list = async_to_streamed_response_wrapper(
            recurrences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            recurrences.delete,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            recurrences.list_transactions,
        )
        self.trigger_transaction = async_to_streamed_response_wrapper(
            recurrences.trigger_transaction,
        )
