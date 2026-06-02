# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import transaction_link_list_params, transaction_link_create_params, transaction_link_update_params
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
from ..types.transaction_link_array import TransactionLinkArray
from ..types.transaction_link_single import TransactionLinkSingle

__all__ = ["TransactionLinksResource", "AsyncTransactionLinksResource"]


class TransactionLinksResource(SyncAPIResource):
    """
    Endpoints to manage links between transactions, and manage the type of links available.
    """

    @cached_property
    def with_raw_response(self) -> TransactionLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return TransactionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return TransactionLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        inward_id: str,
        link_type_id: str,
        outward_id: str,
        link_type_name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionLinkSingle:
        """Store a new link between two transactions.

        For this end point you need the
        journal_id from a transaction.

        Args:
          inward_id: The inward transaction transaction_journal_id for the link. This becomes the 'is
              paid by' transaction of the set.

          link_type_id: The link type ID to use. You can also use the link_type_name field.

          outward_id: The outward transaction transaction_journal_id for the link. This becomes the
              'pays for' transaction of the set.

          link_type_name: The link type name to use. You can also use the link_type_id field.

          notes: Optional. Some notes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/transaction-links",
            body=maybe_transform(
                {
                    "inward_id": inward_id,
                    "link_type_id": link_type_id,
                    "outward_id": outward_id,
                    "link_type_name": link_type_name,
                    "notes": notes,
                },
                transaction_link_create_params.TransactionLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLinkSingle,
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
    ) -> TransactionLinkSingle:
        """
        Returns a single link by its ID.

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
            path_template("/v1/transaction-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLinkSingle,
        )

    def update(
        self,
        id: str,
        *,
        inward_id: str | Omit = omit,
        link_type_id: str | Omit = omit,
        link_type_name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        outward_id: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionLinkSingle:
        """
        Used to update a single existing link.

        Args:
          inward_id: The inward transaction transaction_journal_id for the link. This becomes the 'is
              paid by' transaction of the set.

          link_type_id: The link type ID to use. Use this field OR use the link_type_name field.

          link_type_name: The link type name to use. Use this field OR use the link_type_id field.

          notes: Optional. Some notes. If you submit an empty string the current notes will be
              removed

          outward_id: The outward transaction transaction_journal_id for the link. This becomes the
              'pays for' transaction of the set.

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
            path_template("/v1/transaction-links/{id}", id=id),
            body=maybe_transform(
                {
                    "inward_id": inward_id,
                    "link_type_id": link_type_id,
                    "link_type_name": link_type_name,
                    "notes": notes,
                    "outward_id": outward_id,
                },
                transaction_link_update_params.TransactionLinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLinkSingle,
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
    ) -> TransactionLinkArray:
        """List all the transaction links.

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
            "/v1/transaction-links",
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
                    transaction_link_list_params.TransactionLinkListParams,
                ),
            ),
            cast_to=TransactionLinkArray,
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
        """Will permanently delete link.

        Transactions remain.

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
            path_template("/v1/transaction-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTransactionLinksResource(AsyncAPIResource):
    """
    Endpoints to manage links between transactions, and manage the type of links available.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTransactionLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncTransactionLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        inward_id: str,
        link_type_id: str,
        outward_id: str,
        link_type_name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionLinkSingle:
        """Store a new link between two transactions.

        For this end point you need the
        journal_id from a transaction.

        Args:
          inward_id: The inward transaction transaction_journal_id for the link. This becomes the 'is
              paid by' transaction of the set.

          link_type_id: The link type ID to use. You can also use the link_type_name field.

          outward_id: The outward transaction transaction_journal_id for the link. This becomes the
              'pays for' transaction of the set.

          link_type_name: The link type name to use. You can also use the link_type_id field.

          notes: Optional. Some notes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/transaction-links",
            body=await async_maybe_transform(
                {
                    "inward_id": inward_id,
                    "link_type_id": link_type_id,
                    "outward_id": outward_id,
                    "link_type_name": link_type_name,
                    "notes": notes,
                },
                transaction_link_create_params.TransactionLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLinkSingle,
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
    ) -> TransactionLinkSingle:
        """
        Returns a single link by its ID.

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
            path_template("/v1/transaction-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLinkSingle,
        )

    async def update(
        self,
        id: str,
        *,
        inward_id: str | Omit = omit,
        link_type_id: str | Omit = omit,
        link_type_name: str | Omit = omit,
        notes: Optional[str] | Omit = omit,
        outward_id: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionLinkSingle:
        """
        Used to update a single existing link.

        Args:
          inward_id: The inward transaction transaction_journal_id for the link. This becomes the 'is
              paid by' transaction of the set.

          link_type_id: The link type ID to use. Use this field OR use the link_type_name field.

          link_type_name: The link type name to use. Use this field OR use the link_type_id field.

          notes: Optional. Some notes. If you submit an empty string the current notes will be
              removed

          outward_id: The outward transaction transaction_journal_id for the link. This becomes the
              'pays for' transaction of the set.

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
            path_template("/v1/transaction-links/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "inward_id": inward_id,
                    "link_type_id": link_type_id,
                    "link_type_name": link_type_name,
                    "notes": notes,
                    "outward_id": outward_id,
                },
                transaction_link_update_params.TransactionLinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionLinkSingle,
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
    ) -> TransactionLinkArray:
        """List all the transaction links.

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
            "/v1/transaction-links",
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
                    transaction_link_list_params.TransactionLinkListParams,
                ),
            ),
            cast_to=TransactionLinkArray,
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
        """Will permanently delete link.

        Transactions remain.

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
            path_template("/v1/transaction-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TransactionLinksResourceWithRawResponse:
    def __init__(self, transaction_links: TransactionLinksResource) -> None:
        self._transaction_links = transaction_links

        self.create = to_raw_response_wrapper(
            transaction_links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transaction_links.retrieve,
        )
        self.update = to_raw_response_wrapper(
            transaction_links.update,
        )
        self.list = to_raw_response_wrapper(
            transaction_links.list,
        )
        self.delete = to_raw_response_wrapper(
            transaction_links.delete,
        )


class AsyncTransactionLinksResourceWithRawResponse:
    def __init__(self, transaction_links: AsyncTransactionLinksResource) -> None:
        self._transaction_links = transaction_links

        self.create = async_to_raw_response_wrapper(
            transaction_links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transaction_links.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            transaction_links.update,
        )
        self.list = async_to_raw_response_wrapper(
            transaction_links.list,
        )
        self.delete = async_to_raw_response_wrapper(
            transaction_links.delete,
        )


class TransactionLinksResourceWithStreamingResponse:
    def __init__(self, transaction_links: TransactionLinksResource) -> None:
        self._transaction_links = transaction_links

        self.create = to_streamed_response_wrapper(
            transaction_links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transaction_links.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            transaction_links.update,
        )
        self.list = to_streamed_response_wrapper(
            transaction_links.list,
        )
        self.delete = to_streamed_response_wrapper(
            transaction_links.delete,
        )


class AsyncTransactionLinksResourceWithStreamingResponse:
    def __init__(self, transaction_links: AsyncTransactionLinksResource) -> None:
        self._transaction_links = transaction_links

        self.create = async_to_streamed_response_wrapper(
            transaction_links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transaction_links.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            transaction_links.update,
        )
        self.list = async_to_streamed_response_wrapper(
            transaction_links.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            transaction_links.delete,
        )
