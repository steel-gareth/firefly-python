# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import (
    TransactionTypeFilter,
    link_type_list_params,
    link_type_create_params,
    link_type_update_params,
    link_type_list_transactions_params,
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
from ..types.link_type_single import LinkTypeSingle
from ..types.transaction_array import TransactionArray
from ..types.link_type_list_response import LinkTypeListResponse
from ..types.transaction_type_filter import TransactionTypeFilter

__all__ = ["LinkTypesResource", "AsyncLinkTypesResource"]


class LinkTypesResource(SyncAPIResource):
    """
    Endpoints to manage links between transactions, and manage the type of links available.
    """

    @cached_property
    def with_raw_response(self) -> LinkTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return LinkTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return LinkTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        inward: str,
        name: str,
        outward: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkTypeSingle:
        """Creates a new link type.

        The data required can be submitted as a JSON body or as
        a list of parameters (in key=value pairs, like a webform).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/link-types",
            body=maybe_transform(
                {
                    "inward": inward,
                    "name": name,
                    "outward": outward,
                },
                link_type_create_params.LinkTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkTypeSingle,
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
    ) -> LinkTypeSingle:
        """
        Returns a single link type by its ID.

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
            path_template("/v1/link-types/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkTypeSingle,
        )

    def update(
        self,
        id: str,
        *,
        inward: str | Omit = omit,
        name: str | Omit = omit,
        outward: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkTypeSingle:
        """Used to update a single link type.

        All fields that are not submitted will be
        cleared (set to NULL). The model will tell you which fields are mandatory. You
        cannot update some of the system provided link types, indicated by the
        editable=false flag when you list it.

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
        return self._put(
            path_template("/v1/link-types/{id}", id=id),
            body=maybe_transform(
                {
                    "inward": inward,
                    "name": name,
                    "outward": outward,
                },
                link_type_update_params.LinkTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkTypeSingle,
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
    ) -> LinkTypeListResponse:
        """List all the link types the system has.

        These include the default ones as well
        as any new ones.

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
            "/v1/link-types",
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
                    link_type_list_params.LinkTypeListParams,
                ),
            ),
            cast_to=LinkTypeListResponse,
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
        """Will permanently delete a link type.

        The links between transactions will be
        removed. The transactions themselves remain. You cannot delete some of the
        system provided link types, indicated by the editable=false flag when you list
        it.

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
            path_template("/v1/link-types/{id}", id=id),
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
        List all transactions under this link type, both the inward and outward
        transactions.

        Args:
          end: A date formatted YYYY-MM-DD, to limit the results.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD, to limit the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/link-types/{id}/transactions", id=id),
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
                    link_type_list_transactions_params.LinkTypeListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncLinkTypesResource(AsyncAPIResource):
    """
    Endpoints to manage links between transactions, and manage the type of links available.
    """

    @cached_property
    def with_raw_response(self) -> AsyncLinkTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncLinkTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        inward: str,
        name: str,
        outward: str,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkTypeSingle:
        """Creates a new link type.

        The data required can be submitted as a JSON body or as
        a list of parameters (in key=value pairs, like a webform).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/link-types",
            body=await async_maybe_transform(
                {
                    "inward": inward,
                    "name": name,
                    "outward": outward,
                },
                link_type_create_params.LinkTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkTypeSingle,
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
    ) -> LinkTypeSingle:
        """
        Returns a single link type by its ID.

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
            path_template("/v1/link-types/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkTypeSingle,
        )

    async def update(
        self,
        id: str,
        *,
        inward: str | Omit = omit,
        name: str | Omit = omit,
        outward: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkTypeSingle:
        """Used to update a single link type.

        All fields that are not submitted will be
        cleared (set to NULL). The model will tell you which fields are mandatory. You
        cannot update some of the system provided link types, indicated by the
        editable=false flag when you list it.

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
        return await self._put(
            path_template("/v1/link-types/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "inward": inward,
                    "name": name,
                    "outward": outward,
                },
                link_type_update_params.LinkTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkTypeSingle,
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
    ) -> LinkTypeListResponse:
        """List all the link types the system has.

        These include the default ones as well
        as any new ones.

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
            "/v1/link-types",
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
                    link_type_list_params.LinkTypeListParams,
                ),
            ),
            cast_to=LinkTypeListResponse,
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
        """Will permanently delete a link type.

        The links between transactions will be
        removed. The transactions themselves remain. You cannot delete some of the
        system provided link types, indicated by the editable=false flag when you list
        it.

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
            path_template("/v1/link-types/{id}", id=id),
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
        List all transactions under this link type, both the inward and outward
        transactions.

        Args:
          end: A date formatted YYYY-MM-DD, to limit the results.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD, to limit the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/link-types/{id}/transactions", id=id),
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
                    link_type_list_transactions_params.LinkTypeListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class LinkTypesResourceWithRawResponse:
    def __init__(self, link_types: LinkTypesResource) -> None:
        self._link_types = link_types

        self.create = to_raw_response_wrapper(
            link_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            link_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            link_types.update,
        )
        self.list = to_raw_response_wrapper(
            link_types.list,
        )
        self.delete = to_raw_response_wrapper(
            link_types.delete,
        )
        self.list_transactions = to_raw_response_wrapper(
            link_types.list_transactions,
        )


class AsyncLinkTypesResourceWithRawResponse:
    def __init__(self, link_types: AsyncLinkTypesResource) -> None:
        self._link_types = link_types

        self.create = async_to_raw_response_wrapper(
            link_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            link_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            link_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            link_types.list,
        )
        self.delete = async_to_raw_response_wrapper(
            link_types.delete,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            link_types.list_transactions,
        )


class LinkTypesResourceWithStreamingResponse:
    def __init__(self, link_types: LinkTypesResource) -> None:
        self._link_types = link_types

        self.create = to_streamed_response_wrapper(
            link_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            link_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            link_types.update,
        )
        self.list = to_streamed_response_wrapper(
            link_types.list,
        )
        self.delete = to_streamed_response_wrapper(
            link_types.delete,
        )
        self.list_transactions = to_streamed_response_wrapper(
            link_types.list_transactions,
        )


class AsyncLinkTypesResourceWithStreamingResponse:
    def __init__(self, link_types: AsyncLinkTypesResource) -> None:
        self._link_types = link_types

        self.create = async_to_streamed_response_wrapper(
            link_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            link_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            link_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            link_types.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            link_types.delete,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            link_types.list_transactions,
        )
