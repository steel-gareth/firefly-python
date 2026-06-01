# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date

import httpx

from ..types import (
    piggy_bank_list_params,
    piggy_bank_create_params,
    piggy_bank_update_params,
    piggy_bank_list_events_params,
    piggy_bank_list_attachments_params,
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
from ..types.attachment_array import AttachmentArray
from ..types.piggy_bank_array import PiggyBankArray
from ..types.piggy_bank_single import PiggyBankSingle
from ..types.piggy_bank_event_array import PiggyBankEventArray

__all__ = ["PiggyBanksResource", "AsyncPiggyBanksResource"]


class PiggyBanksResource(SyncAPIResource):
    """
    Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
    """

    @cached_property
    def with_raw_response(self) -> PiggyBanksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return PiggyBanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PiggyBanksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return PiggyBanksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: object,
        name: str,
        start_date: Union[str, date],
        target_amount: Optional[str],
        accounts: Iterable[piggy_bank_create_params.Account] | Omit = omit,
        current_amount: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        target_date: Union[str, date, None] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiggyBankSingle:
        """Creates a new piggy bank.

        The data required can be submitted as a JSON body or
        as a list of parameters.

        Args:
          start_date: The date you started with this piggy bank.

          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          target_date: The date you intend to finish saving money.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/piggy-banks",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "start_date": start_date,
                    "target_amount": target_amount,
                    "accounts": accounts,
                    "current_amount": current_amount,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "order": order,
                    "target_date": target_date,
                },
                piggy_bank_create_params.PiggyBankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiggyBankSingle,
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
    ) -> PiggyBankSingle:
        """
        Get a single piggy bank.

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
            path_template("/v1/piggy-banks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiggyBankSingle,
        )

    def update(
        self,
        id: str,
        *,
        accounts: Iterable[piggy_bank_update_params.Account] | Omit = omit,
        name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        target_amount: Optional[str] | Omit = omit,
        target_date: Union[str, date, None] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiggyBankSingle:
        """
        Update existing piggy bank.

        Args:
          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          start_date: The date you started with this piggy bank.

          target_date: The date you intend to finish saving money.

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
            path_template("/v1/piggy-banks/{id}", id=id),
            body=maybe_transform(
                {
                    "accounts": accounts,
                    "name": name,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "order": order,
                    "start_date": start_date,
                    "target_amount": target_amount,
                    "target_date": target_date,
                },
                piggy_bank_update_params.PiggyBankUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiggyBankSingle,
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
    ) -> PiggyBankArray:
        """List all piggy banks.

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
            "/v1/piggy-banks",
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
                    piggy_bank_list_params.PiggyBankListParams,
                ),
            ),
            cast_to=PiggyBankArray,
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
        Delete a piggy bank.

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
            path_template("/v1/piggy-banks/{id}", id=id),
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
        """Lists all attachments.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

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
            path_template("/v1/piggy-banks/{id}/attachments", id=id),
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
                    piggy_bank_list_attachments_params.PiggyBankListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    def list_events(
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
    ) -> PiggyBankEventArray:
        """
        List all events linked to a piggy bank (adding and removing money).

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
            path_template("/v1/piggy-banks/{id}/events", id=id),
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
                    piggy_bank_list_events_params.PiggyBankListEventsParams,
                ),
            ),
            cast_to=PiggyBankEventArray,
        )


class AsyncPiggyBanksResource(AsyncAPIResource):
    """
    Endpoints to control and manage all of the user&#039;s piggy banks and related objects and information.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPiggyBanksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPiggyBanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPiggyBanksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncPiggyBanksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: object,
        name: str,
        start_date: Union[str, date],
        target_amount: Optional[str],
        accounts: Iterable[piggy_bank_create_params.Account] | Omit = omit,
        current_amount: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        target_date: Union[str, date, None] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiggyBankSingle:
        """Creates a new piggy bank.

        The data required can be submitted as a JSON body or
        as a list of parameters.

        Args:
          start_date: The date you started with this piggy bank.

          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          target_date: The date you intend to finish saving money.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/piggy-banks",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "name": name,
                    "start_date": start_date,
                    "target_amount": target_amount,
                    "accounts": accounts,
                    "current_amount": current_amount,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "order": order,
                    "target_date": target_date,
                },
                piggy_bank_create_params.PiggyBankCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiggyBankSingle,
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
    ) -> PiggyBankSingle:
        """
        Get a single piggy bank.

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
            path_template("/v1/piggy-banks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiggyBankSingle,
        )

    async def update(
        self,
        id: str,
        *,
        accounts: Iterable[piggy_bank_update_params.Account] | Omit = omit,
        name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        object_group_id: Optional[str] | Omit = omit,
        object_group_title: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        target_amount: Optional[str] | Omit = omit,
        target_date: Union[str, date, None] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiggyBankSingle:
        """
        Update existing piggy bank.

        Args:
          object_group_id: The group ID of the group this object is part of. NULL if no group.

          object_group_title: The name of the group. NULL if no group.

          start_date: The date you started with this piggy bank.

          target_date: The date you intend to finish saving money.

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
            path_template("/v1/piggy-banks/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "accounts": accounts,
                    "name": name,
                    "notes": notes,
                    "object_group_id": object_group_id,
                    "object_group_title": object_group_title,
                    "order": order,
                    "start_date": start_date,
                    "target_amount": target_amount,
                    "target_date": target_date,
                },
                piggy_bank_update_params.PiggyBankUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiggyBankSingle,
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
    ) -> PiggyBankArray:
        """List all piggy banks.

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
            "/v1/piggy-banks",
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
                    piggy_bank_list_params.PiggyBankListParams,
                ),
            ),
            cast_to=PiggyBankArray,
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
        Delete a piggy bank.

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
            path_template("/v1/piggy-banks/{id}", id=id),
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
        """Lists all attachments.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

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
            path_template("/v1/piggy-banks/{id}/attachments", id=id),
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
                    piggy_bank_list_attachments_params.PiggyBankListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    async def list_events(
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
    ) -> PiggyBankEventArray:
        """
        List all events linked to a piggy bank (adding and removing money).

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
            path_template("/v1/piggy-banks/{id}/events", id=id),
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
                    piggy_bank_list_events_params.PiggyBankListEventsParams,
                ),
            ),
            cast_to=PiggyBankEventArray,
        )


class PiggyBanksResourceWithRawResponse:
    def __init__(self, piggy_banks: PiggyBanksResource) -> None:
        self._piggy_banks = piggy_banks

        self.create = to_raw_response_wrapper(
            piggy_banks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            piggy_banks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            piggy_banks.update,
        )
        self.list = to_raw_response_wrapper(
            piggy_banks.list,
        )
        self.delete = to_raw_response_wrapper(
            piggy_banks.delete,
        )
        self.list_attachments = to_raw_response_wrapper(
            piggy_banks.list_attachments,
        )
        self.list_events = to_raw_response_wrapper(
            piggy_banks.list_events,
        )


class AsyncPiggyBanksResourceWithRawResponse:
    def __init__(self, piggy_banks: AsyncPiggyBanksResource) -> None:
        self._piggy_banks = piggy_banks

        self.create = async_to_raw_response_wrapper(
            piggy_banks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            piggy_banks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            piggy_banks.update,
        )
        self.list = async_to_raw_response_wrapper(
            piggy_banks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            piggy_banks.delete,
        )
        self.list_attachments = async_to_raw_response_wrapper(
            piggy_banks.list_attachments,
        )
        self.list_events = async_to_raw_response_wrapper(
            piggy_banks.list_events,
        )


class PiggyBanksResourceWithStreamingResponse:
    def __init__(self, piggy_banks: PiggyBanksResource) -> None:
        self._piggy_banks = piggy_banks

        self.create = to_streamed_response_wrapper(
            piggy_banks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            piggy_banks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            piggy_banks.update,
        )
        self.list = to_streamed_response_wrapper(
            piggy_banks.list,
        )
        self.delete = to_streamed_response_wrapper(
            piggy_banks.delete,
        )
        self.list_attachments = to_streamed_response_wrapper(
            piggy_banks.list_attachments,
        )
        self.list_events = to_streamed_response_wrapper(
            piggy_banks.list_events,
        )


class AsyncPiggyBanksResourceWithStreamingResponse:
    def __init__(self, piggy_banks: AsyncPiggyBanksResource) -> None:
        self._piggy_banks = piggy_banks

        self.create = async_to_streamed_response_wrapper(
            piggy_banks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            piggy_banks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            piggy_banks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            piggy_banks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            piggy_banks.delete,
        )
        self.list_attachments = async_to_streamed_response_wrapper(
            piggy_banks.list_attachments,
        )
        self.list_events = async_to_streamed_response_wrapper(
            piggy_banks.list_events,
        )
