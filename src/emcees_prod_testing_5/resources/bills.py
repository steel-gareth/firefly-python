# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date, datetime

import httpx

from ..types import (
    BillRepeatFrequency,
    TransactionTypeFilter,
    bill_list_params,
    bill_create_params,
    bill_update_params,
    bill_retrieve_params,
    bill_list_attachments_params,
    bill_list_transactions_params,
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
from ..types.bill_array import BillArray
from ..types.rule_array import RuleArray
from ..types.bill_single import BillSingle
from ..types.attachment_array import AttachmentArray
from ..types.transaction_array import TransactionArray
from ..types.bill_repeat_frequency import BillRepeatFrequency
from ..types.transaction_type_filter import TransactionTypeFilter

__all__ = ["BillsResource", "AsyncBillsResource"]


class BillsResource(SyncAPIResource):
    """Endpoints to manage a user&#039;s bills and all related objects."""

    @cached_property
    def with_raw_response(self) -> BillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return BillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return BillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount_max: str,
        amount_min: str,
        date: Union[str, datetime],
        name: str,
        repeat_freq: BillRepeatFrequency,
        active: bool | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        extension_date: Union[str, datetime] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        skip: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillSingle:
        """Creates a new bill.

        The data required can be submitted as a JSON body or as a
        list of parameters.

        Args:
          repeat_freq: How often the bill must be paid.

          active: If the bill is active.

          currency_code: Use either currency_id or currency_code

          currency_id: Use either currency_id or currency_code

          end_date: The date after which this bill is no longer valid or applicable

          extension_date: The date before which the bill must be renewed (or cancelled)

          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          skip: How often the bill must be skipped. 1 means a bi-monthly bill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/bills",
            body=maybe_transform(
                {
                    "amount_max": amount_max,
                    "amount_min": amount_min,
                    "date": date,
                    "name": name,
                    "repeat_freq": repeat_freq,
                    "active": active,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "end_date": end_date,
                    "extension_date": extension_date,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "skip": skip,
                },
                bill_create_params.BillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillSingle,
        )

    def retrieve(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillSingle:
        """Get a single bill.

        Args:
          end: A date formatted YYYY-MM-DD.

        If it is added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

          start: A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

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
            path_template("/v1/bills/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    bill_retrieve_params.BillRetrieveParams,
                ),
            ),
            cast_to=BillSingle,
        )

    def update(
        self,
        id: str,
        *,
        name: str,
        active: bool | Omit = omit,
        amount_max: str | Omit = omit,
        amount_min: str | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        extension_date: Union[str, datetime] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        repeat_freq: BillRepeatFrequency | Omit = omit,
        skip: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillSingle:
        """
        Update existing bill.

        Args:
          active: If the bill is active.

          currency_code: Use either currency_id or currency_code

          currency_id: Use either currency_id or currency_code

          end_date: The date after which this bill is no longer valid or applicable

          extension_date: The date before which the bill must be renewed (or cancelled)

          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          repeat_freq: How often the bill must be paid.

          skip: How often the bill must be skipped. 1 means a bi-monthly bill.

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
            path_template("/v1/bills/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "amount_max": amount_max,
                    "amount_min": amount_min,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "date": date,
                    "end_date": end_date,
                    "extension_date": extension_date,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "repeat_freq": repeat_freq,
                    "skip": skip,
                },
                bill_update_params.BillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillSingle,
        )

    def list(
        self,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillArray:
        """
        This endpoint will list all the user's bills.

        Args:
          end: A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/bills",
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
                    },
                    bill_list_params.BillListParams,
                ),
            ),
            cast_to=BillArray,
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
        """Delete a bill.

        This will not delete any associated rules. Will not remove
        associated transactions. WILL remove all associated attachments.

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
            path_template("/v1/bills/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_attachments(
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
    ) -> AttachmentArray:
        """
        This endpoint will list all attachments linked to the bill.

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
            path_template("/v1/bills/{id}/attachments", id=id),
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
                    bill_list_attachments_params.BillListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    def list_rules(
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
    ) -> RuleArray:
        """
        This endpoint will list all rules that have an action to set the bill to this
        bill.

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
            path_template("/v1/bills/{id}/rules", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleArray,
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
        This endpoint will list all transactions linked to this bill.

        Args:
          end: A date formatted YYYY-MM-DD.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD.

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
            path_template("/v1/bills/{id}/transactions", id=id),
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
                    bill_list_transactions_params.BillListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncBillsResource(AsyncAPIResource):
    """Endpoints to manage a user&#039;s bills and all related objects."""

    @cached_property
    def with_raw_response(self) -> AsyncBillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncBillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount_max: str,
        amount_min: str,
        date: Union[str, datetime],
        name: str,
        repeat_freq: BillRepeatFrequency,
        active: bool | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        extension_date: Union[str, datetime] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        skip: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillSingle:
        """Creates a new bill.

        The data required can be submitted as a JSON body or as a
        list of parameters.

        Args:
          repeat_freq: How often the bill must be paid.

          active: If the bill is active.

          currency_code: Use either currency_id or currency_code

          currency_id: Use either currency_id or currency_code

          end_date: The date after which this bill is no longer valid or applicable

          extension_date: The date before which the bill must be renewed (or cancelled)

          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          skip: How often the bill must be skipped. 1 means a bi-monthly bill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/bills",
            body=await async_maybe_transform(
                {
                    "amount_max": amount_max,
                    "amount_min": amount_min,
                    "date": date,
                    "name": name,
                    "repeat_freq": repeat_freq,
                    "active": active,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "end_date": end_date,
                    "extension_date": extension_date,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "skip": skip,
                },
                bill_create_params.BillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillSingle,
        )

    async def retrieve(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillSingle:
        """Get a single bill.

        Args:
          end: A date formatted YYYY-MM-DD.

        If it is added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

          start: A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

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
            path_template("/v1/bills/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    bill_retrieve_params.BillRetrieveParams,
                ),
            ),
            cast_to=BillSingle,
        )

    async def update(
        self,
        id: str,
        *,
        name: str,
        active: bool | Omit = omit,
        amount_max: str | Omit = omit,
        amount_min: str | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        end_date: Union[str, datetime] | Omit = omit,
        extension_date: Union[str, datetime] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        repeat_freq: BillRepeatFrequency | Omit = omit,
        skip: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillSingle:
        """
        Update existing bill.

        Args:
          active: If the bill is active.

          currency_code: Use either currency_id or currency_code

          currency_id: Use either currency_id or currency_code

          end_date: The date after which this bill is no longer valid or applicable

          extension_date: The date before which the bill must be renewed (or cancelled)

          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          repeat_freq: How often the bill must be paid.

          skip: How often the bill must be skipped. 1 means a bi-monthly bill.

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
            path_template("/v1/bills/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "active": active,
                    "amount_max": amount_max,
                    "amount_min": amount_min,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "date": date,
                    "end_date": end_date,
                    "extension_date": extension_date,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "repeat_freq": repeat_freq,
                    "skip": skip,
                },
                bill_update_params.BillUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillSingle,
        )

    async def list(
        self,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillArray:
        """
        This endpoint will list all the user's bills.

        Args:
          end: A date formatted YYYY-MM-DD. If it is added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD. If it is are added to the request, Firefly III will
              calculate the appropriate payment and paid dates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/bills",
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
                    },
                    bill_list_params.BillListParams,
                ),
            ),
            cast_to=BillArray,
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
        """Delete a bill.

        This will not delete any associated rules. Will not remove
        associated transactions. WILL remove all associated attachments.

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
            path_template("/v1/bills/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_attachments(
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
    ) -> AttachmentArray:
        """
        This endpoint will list all attachments linked to the bill.

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
            path_template("/v1/bills/{id}/attachments", id=id),
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
                    bill_list_attachments_params.BillListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    async def list_rules(
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
    ) -> RuleArray:
        """
        This endpoint will list all rules that have an action to set the bill to this
        bill.

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
            path_template("/v1/bills/{id}/rules", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleArray,
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
        This endpoint will list all transactions linked to this bill.

        Args:
          end: A date formatted YYYY-MM-DD.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD.

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
            path_template("/v1/bills/{id}/transactions", id=id),
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
                    bill_list_transactions_params.BillListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class BillsResourceWithRawResponse:
    def __init__(self, bills: BillsResource) -> None:
        self._bills = bills

        self.create = to_raw_response_wrapper(
            bills.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bills.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bills.update,
        )
        self.list = to_raw_response_wrapper(
            bills.list,
        )
        self.delete = to_raw_response_wrapper(
            bills.delete,
        )
        self.list_attachments = to_raw_response_wrapper(
            bills.list_attachments,
        )
        self.list_rules = to_raw_response_wrapper(
            bills.list_rules,
        )
        self.list_transactions = to_raw_response_wrapper(
            bills.list_transactions,
        )


class AsyncBillsResourceWithRawResponse:
    def __init__(self, bills: AsyncBillsResource) -> None:
        self._bills = bills

        self.create = async_to_raw_response_wrapper(
            bills.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bills.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bills.update,
        )
        self.list = async_to_raw_response_wrapper(
            bills.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bills.delete,
        )
        self.list_attachments = async_to_raw_response_wrapper(
            bills.list_attachments,
        )
        self.list_rules = async_to_raw_response_wrapper(
            bills.list_rules,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            bills.list_transactions,
        )


class BillsResourceWithStreamingResponse:
    def __init__(self, bills: BillsResource) -> None:
        self._bills = bills

        self.create = to_streamed_response_wrapper(
            bills.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bills.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bills.update,
        )
        self.list = to_streamed_response_wrapper(
            bills.list,
        )
        self.delete = to_streamed_response_wrapper(
            bills.delete,
        )
        self.list_attachments = to_streamed_response_wrapper(
            bills.list_attachments,
        )
        self.list_rules = to_streamed_response_wrapper(
            bills.list_rules,
        )
        self.list_transactions = to_streamed_response_wrapper(
            bills.list_transactions,
        )


class AsyncBillsResourceWithStreamingResponse:
    def __init__(self, bills: AsyncBillsResource) -> None:
        self._bills = bills

        self.create = async_to_streamed_response_wrapper(
            bills.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bills.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bills.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bills.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bills.delete,
        )
        self.list_attachments = async_to_streamed_response_wrapper(
            bills.list_attachments,
        )
        self.list_rules = async_to_streamed_response_wrapper(
            bills.list_rules,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            bills.list_transactions,
        )
