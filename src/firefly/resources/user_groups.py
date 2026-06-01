# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import user_group_list_params, user_group_update_params
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
from ..types.user_group_single import UserGroupSingle
from ..types.user_group_list_response import UserGroupListResponse

__all__ = ["UserGroupsResource", "AsyncUserGroupsResource"]


class UserGroupsResource(SyncAPIResource):
    """
    User groups are the objects around which &quot;financial administrations&quot; are built.
    """

    @cached_property
    def with_raw_response(self) -> UserGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return UserGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return UserGroupsResourceWithStreamingResponse(self)

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
    ) -> UserGroupSingle:
        """
        Returns a single user group by its ID.

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
            path_template("/v1/user-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupSingle,
        )

    def update(
        self,
        id: str,
        *,
        title: str,
        primary_currency_code: str | Omit = omit,
        primary_currency_id: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupSingle:
        """Used to update a single user group.

        The available fields are still limited.

        Args:
          title: A descriptive title for the user group.

          primary_currency_code: Use either primary_currency_id or primary_currency_code. This will set the
              primary currency for the user group ('financial administration').

          primary_currency_id: Use either primary_currency_id or primary_currency_code. This will set the
              primary currency for the user group ('financial administration').

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
            path_template("/v1/user-groups/{id}", id=id),
            body=maybe_transform(
                {
                    "title": title,
                    "primary_currency_code": primary_currency_code,
                    "primary_currency_id": primary_currency_id,
                },
                user_group_update_params.UserGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupSingle,
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
    ) -> UserGroupListResponse:
        """List all the user groups available to this user.

        These are essentially the
        'financial administrations' that Firefly III supports.

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
            "/v1/user-groups",
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
                    user_group_list_params.UserGroupListParams,
                ),
            ),
            cast_to=UserGroupListResponse,
        )


class AsyncUserGroupsResource(AsyncAPIResource):
    """
    User groups are the objects around which &quot;financial administrations&quot; are built.
    """

    @cached_property
    def with_raw_response(self) -> AsyncUserGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncUserGroupsResourceWithStreamingResponse(self)

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
    ) -> UserGroupSingle:
        """
        Returns a single user group by its ID.

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
            path_template("/v1/user-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupSingle,
        )

    async def update(
        self,
        id: str,
        *,
        title: str,
        primary_currency_code: str | Omit = omit,
        primary_currency_id: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGroupSingle:
        """Used to update a single user group.

        The available fields are still limited.

        Args:
          title: A descriptive title for the user group.

          primary_currency_code: Use either primary_currency_id or primary_currency_code. This will set the
              primary currency for the user group ('financial administration').

          primary_currency_id: Use either primary_currency_id or primary_currency_code. This will set the
              primary currency for the user group ('financial administration').

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
            path_template("/v1/user-groups/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "title": title,
                    "primary_currency_code": primary_currency_code,
                    "primary_currency_id": primary_currency_id,
                },
                user_group_update_params.UserGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGroupSingle,
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
    ) -> UserGroupListResponse:
        """List all the user groups available to this user.

        These are essentially the
        'financial administrations' that Firefly III supports.

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
            "/v1/user-groups",
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
                    user_group_list_params.UserGroupListParams,
                ),
            ),
            cast_to=UserGroupListResponse,
        )


class UserGroupsResourceWithRawResponse:
    def __init__(self, user_groups: UserGroupsResource) -> None:
        self._user_groups = user_groups

        self.retrieve = to_raw_response_wrapper(
            user_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            user_groups.update,
        )
        self.list = to_raw_response_wrapper(
            user_groups.list,
        )


class AsyncUserGroupsResourceWithRawResponse:
    def __init__(self, user_groups: AsyncUserGroupsResource) -> None:
        self._user_groups = user_groups

        self.retrieve = async_to_raw_response_wrapper(
            user_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            user_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            user_groups.list,
        )


class UserGroupsResourceWithStreamingResponse:
    def __init__(self, user_groups: UserGroupsResource) -> None:
        self._user_groups = user_groups

        self.retrieve = to_streamed_response_wrapper(
            user_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            user_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            user_groups.list,
        )


class AsyncUserGroupsResourceWithStreamingResponse:
    def __init__(self, user_groups: AsyncUserGroupsResource) -> None:
        self._user_groups = user_groups

        self.retrieve = async_to_streamed_response_wrapper(
            user_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            user_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            user_groups.list,
        )
