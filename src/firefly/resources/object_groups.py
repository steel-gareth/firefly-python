# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    object_group_list_params,
    object_group_update_params,
    object_group_list_bills_params,
    object_group_list_piggy_banks_params,
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
from ..types.piggy_bank_array import PiggyBankArray
from ..types.object_group_single import ObjectGroupSingle
from ..types.object_group_list_response import ObjectGroupListResponse

__all__ = ["ObjectGroupsResource", "AsyncObjectGroupsResource"]


class ObjectGroupsResource(SyncAPIResource):
    """Endpoints to control and manage all of the user&#039;s object groups.

    Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
    """

    @cached_property
    def with_raw_response(self) -> ObjectGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return ObjectGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return ObjectGroupsResourceWithStreamingResponse(self)

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
    ) -> ObjectGroupSingle:
        """
        Get a single object group.

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
            path_template("/v1/object-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGroupSingle,
        )

    def update(
        self,
        id: str,
        *,
        title: str,
        order: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGroupSingle:
        """
        Update existing object group.

        Args:
          order: Order of the object group

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
            path_template("/v1/object-groups/{id}", id=id),
            body=maybe_transform(
                {
                    "title": title,
                    "order": order,
                },
                object_group_update_params.ObjectGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGroupSingle,
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
    ) -> ObjectGroupListResponse:
        """List all object groups.

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
            "/v1/object-groups",
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
                    object_group_list_params.ObjectGroupListParams,
                ),
            ),
            cast_to=ObjectGroupListResponse,
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
        Delete a object group.

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
            path_template("/v1/object-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_bills(
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
    ) -> BillArray:
        """List all bills with this object group.

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
            path_template("/v1/object-groups/{id}/bills", id=id),
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
                    object_group_list_bills_params.ObjectGroupListBillsParams,
                ),
            ),
            cast_to=BillArray,
        )

    def list_piggy_banks(
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
    ) -> PiggyBankArray:
        """
        This endpoint returns a list of all the piggy banks connected to the object
        group.

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
            path_template("/v1/object-groups/{id}/piggy-banks", id=id),
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
                    object_group_list_piggy_banks_params.ObjectGroupListPiggyBanksParams,
                ),
            ),
            cast_to=PiggyBankArray,
        )


class AsyncObjectGroupsResource(AsyncAPIResource):
    """Endpoints to control and manage all of the user&#039;s object groups.

    Can only be created in conjunction with another object (for example a piggy bank) and will auto-delete when no other items are linked to it.
    """

    @cached_property
    def with_raw_response(self) -> AsyncObjectGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncObjectGroupsResourceWithStreamingResponse(self)

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
    ) -> ObjectGroupSingle:
        """
        Get a single object group.

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
            path_template("/v1/object-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGroupSingle,
        )

    async def update(
        self,
        id: str,
        *,
        title: str,
        order: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectGroupSingle:
        """
        Update existing object group.

        Args:
          order: Order of the object group

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
            path_template("/v1/object-groups/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "order": order,
                },
                object_group_update_params.ObjectGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectGroupSingle,
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
    ) -> ObjectGroupListResponse:
        """List all object groups.

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
            "/v1/object-groups",
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
                    object_group_list_params.ObjectGroupListParams,
                ),
            ),
            cast_to=ObjectGroupListResponse,
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
        Delete a object group.

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
            path_template("/v1/object-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_bills(
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
    ) -> BillArray:
        """List all bills with this object group.

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
            path_template("/v1/object-groups/{id}/bills", id=id),
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
                    object_group_list_bills_params.ObjectGroupListBillsParams,
                ),
            ),
            cast_to=BillArray,
        )

    async def list_piggy_banks(
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
    ) -> PiggyBankArray:
        """
        This endpoint returns a list of all the piggy banks connected to the object
        group.

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
            path_template("/v1/object-groups/{id}/piggy-banks", id=id),
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
                    object_group_list_piggy_banks_params.ObjectGroupListPiggyBanksParams,
                ),
            ),
            cast_to=PiggyBankArray,
        )


class ObjectGroupsResourceWithRawResponse:
    def __init__(self, object_groups: ObjectGroupsResource) -> None:
        self._object_groups = object_groups

        self.retrieve = to_raw_response_wrapper(
            object_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            object_groups.update,
        )
        self.list = to_raw_response_wrapper(
            object_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            object_groups.delete,
        )
        self.list_bills = to_raw_response_wrapper(
            object_groups.list_bills,
        )
        self.list_piggy_banks = to_raw_response_wrapper(
            object_groups.list_piggy_banks,
        )


class AsyncObjectGroupsResourceWithRawResponse:
    def __init__(self, object_groups: AsyncObjectGroupsResource) -> None:
        self._object_groups = object_groups

        self.retrieve = async_to_raw_response_wrapper(
            object_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            object_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            object_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            object_groups.delete,
        )
        self.list_bills = async_to_raw_response_wrapper(
            object_groups.list_bills,
        )
        self.list_piggy_banks = async_to_raw_response_wrapper(
            object_groups.list_piggy_banks,
        )


class ObjectGroupsResourceWithStreamingResponse:
    def __init__(self, object_groups: ObjectGroupsResource) -> None:
        self._object_groups = object_groups

        self.retrieve = to_streamed_response_wrapper(
            object_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            object_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            object_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            object_groups.delete,
        )
        self.list_bills = to_streamed_response_wrapper(
            object_groups.list_bills,
        )
        self.list_piggy_banks = to_streamed_response_wrapper(
            object_groups.list_piggy_banks,
        )


class AsyncObjectGroupsResourceWithStreamingResponse:
    def __init__(self, object_groups: AsyncObjectGroupsResource) -> None:
        self._object_groups = object_groups

        self.retrieve = async_to_streamed_response_wrapper(
            object_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            object_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            object_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            object_groups.delete,
        )
        self.list_bills = async_to_streamed_response_wrapper(
            object_groups.list_bills,
        )
        self.list_piggy_banks = async_to_streamed_response_wrapper(
            object_groups.list_piggy_banks,
        )
