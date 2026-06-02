# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date

import httpx

from ..types import (
    rule_group_create_params,
    rule_group_update_params,
    rule_group_list_all_params,
    rule_group_list_rules_params,
    rule_group_trigger_rules_params,
    rule_group_test_transactions_params,
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
from ..types.rule_array import RuleArray
from ..types.rule_group_single import RuleGroupSingle
from ..types.transaction_array import TransactionArray
from ..types.rule_group_list_all_response import RuleGroupListAllResponse

__all__ = ["RuleGroupsResource", "AsyncRuleGroupsResource"]


class RuleGroupsResource(SyncAPIResource):
    """
    Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
    """

    @cached_property
    def with_raw_response(self) -> RuleGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return RuleGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RuleGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return RuleGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        title: str,
        active: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleGroupSingle:
        """Creates a new rule group.

        The data required can be submitted as a JSON body or
        as a list of parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/rule-groups",
            body=maybe_transform(
                {
                    "title": title,
                    "active": active,
                    "description": description,
                    "order": order,
                },
                rule_group_create_params.RuleGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleGroupSingle,
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
    ) -> RuleGroupSingle:
        """Get a single rule group.

        This does not include the rules. For that, see below.

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
            path_template("/v1/rule-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleGroupSingle,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        title: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleGroupSingle:
        """
        Update existing rule group.

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
            path_template("/v1/rule-groups/{id}", id=id),
            body=maybe_transform(
                {
                    "active": active,
                    "description": description,
                    "order": order,
                    "title": title,
                },
                rule_group_update_params.RuleGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleGroupSingle,
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
        Delete a rule group.

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
            path_template("/v1/rule-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_all(
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
    ) -> RuleGroupListAllResponse:
        """List all rule groups.

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
            "/v1/rule-groups",
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
                    rule_group_list_all_params.RuleGroupListAllParams,
                ),
            ),
            cast_to=RuleGroupListAllResponse,
        )

    def list_rules(
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
    ) -> RuleArray:
        """List rules in this rule group.

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
            path_template("/v1/rule-groups/{id}/rules", id=id),
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
                    rule_group_list_rules_params.RuleGroupListRulesParams,
                ),
            ),
            cast_to=RuleArray,
        )

    def test_transactions(
        self,
        id: str,
        *,
        accounts: Iterable[int] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search_limit: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        triggered_limit: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """Test which transactions would be hit by the rule group.

        No changes will be made.
        Limit the result if you want to.

        Args:
          accounts: Limit the testing of the rule group to these asset accounts or liabilities. Only
              asset accounts and liabilities will be accepted. Other types will be silently
              dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          search_limit: Maximum number of transactions Firefly III will try. Don't set this too high, or
              it will take Firefly III very long to run the test. I suggest a max of 200.

          start: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

          triggered_limit: Maximum number of transactions the rule group can actually trigger on, before
              Firefly III stops. I would suggest setting this to 10 or 15. Don't go above the
              user's page size, because browsing to page 2 or 3 of a test result would fire
              the test again, making any navigation efforts very slow.

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
            path_template("/v1/rule-groups/{id}/test", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "accounts": accounts,
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "search_limit": search_limit,
                        "start": start,
                        "triggered_limit": triggered_limit,
                    },
                    rule_group_test_transactions_params.RuleGroupTestTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    def trigger_rules(
        self,
        id: str,
        *,
        accounts: Iterable[int] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Fire the rule group on your transactions.

        Changes will be made by the rules in
        the rule group. Limit the result if you want to.

        Args:
          accounts: Limit the triggering of the rule group to these asset accounts or liabilities.
              Only asset accounts and liabilities will be accepted. Other types will be
              silently dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. Both the start date and the end date must be present.

          start: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. Both the start date and the end date must be present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/rule-groups/{id}/trigger", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "accounts": accounts,
                        "end": end,
                        "start": start,
                    },
                    rule_group_trigger_rules_params.RuleGroupTriggerRulesParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncRuleGroupsResource(AsyncAPIResource):
    """
    Manage all of the user&#039;s groups of rules and trigger the execution of entire groups.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRuleGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRuleGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRuleGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncRuleGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        title: str,
        active: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleGroupSingle:
        """Creates a new rule group.

        The data required can be submitted as a JSON body or
        as a list of parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/rule-groups",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "active": active,
                    "description": description,
                    "order": order,
                },
                rule_group_create_params.RuleGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleGroupSingle,
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
    ) -> RuleGroupSingle:
        """Get a single rule group.

        This does not include the rules. For that, see below.

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
            path_template("/v1/rule-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleGroupSingle,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        order: int | Omit = omit,
        title: str | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleGroupSingle:
        """
        Update existing rule group.

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
            path_template("/v1/rule-groups/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "description": description,
                    "order": order,
                    "title": title,
                },
                rule_group_update_params.RuleGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleGroupSingle,
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
        Delete a rule group.

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
            path_template("/v1/rule-groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_all(
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
    ) -> RuleGroupListAllResponse:
        """List all rule groups.

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
            "/v1/rule-groups",
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
                    rule_group_list_all_params.RuleGroupListAllParams,
                ),
            ),
            cast_to=RuleGroupListAllResponse,
        )

    async def list_rules(
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
    ) -> RuleArray:
        """List rules in this rule group.

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
            path_template("/v1/rule-groups/{id}/rules", id=id),
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
                    rule_group_list_rules_params.RuleGroupListRulesParams,
                ),
            ),
            cast_to=RuleArray,
        )

    async def test_transactions(
        self,
        id: str,
        *,
        accounts: Iterable[int] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search_limit: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        triggered_limit: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """Test which transactions would be hit by the rule group.

        No changes will be made.
        Limit the result if you want to.

        Args:
          accounts: Limit the testing of the rule group to these asset accounts or liabilities. Only
              asset accounts and liabilities will be accepted. Other types will be silently
              dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          search_limit: Maximum number of transactions Firefly III will try. Don't set this too high, or
              it will take Firefly III very long to run the test. I suggest a max of 200.

          start: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

          triggered_limit: Maximum number of transactions the rule group can actually trigger on, before
              Firefly III stops. I would suggest setting this to 10 or 15. Don't go above the
              user's page size, because browsing to page 2 or 3 of a test result would fire
              the test again, making any navigation efforts very slow.

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
            path_template("/v1/rule-groups/{id}/test", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "accounts": accounts,
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "search_limit": search_limit,
                        "start": start,
                        "triggered_limit": triggered_limit,
                    },
                    rule_group_test_transactions_params.RuleGroupTestTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    async def trigger_rules(
        self,
        id: str,
        *,
        accounts: Iterable[int] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Fire the rule group on your transactions.

        Changes will be made by the rules in
        the rule group. Limit the result if you want to.

        Args:
          accounts: Limit the triggering of the rule group to these asset accounts or liabilities.
              Only asset accounts and liabilities will be accepted. Other types will be
              silently dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. Both the start date and the end date must be present.

          start: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. Both the start date and the end date must be present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/rule-groups/{id}/trigger", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "accounts": accounts,
                        "end": end,
                        "start": start,
                    },
                    rule_group_trigger_rules_params.RuleGroupTriggerRulesParams,
                ),
            ),
            cast_to=NoneType,
        )


class RuleGroupsResourceWithRawResponse:
    def __init__(self, rule_groups: RuleGroupsResource) -> None:
        self._rule_groups = rule_groups

        self.create = to_raw_response_wrapper(
            rule_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            rule_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            rule_groups.update,
        )
        self.delete = to_raw_response_wrapper(
            rule_groups.delete,
        )
        self.list_all = to_raw_response_wrapper(
            rule_groups.list_all,
        )
        self.list_rules = to_raw_response_wrapper(
            rule_groups.list_rules,
        )
        self.test_transactions = to_raw_response_wrapper(
            rule_groups.test_transactions,
        )
        self.trigger_rules = to_raw_response_wrapper(
            rule_groups.trigger_rules,
        )


class AsyncRuleGroupsResourceWithRawResponse:
    def __init__(self, rule_groups: AsyncRuleGroupsResource) -> None:
        self._rule_groups = rule_groups

        self.create = async_to_raw_response_wrapper(
            rule_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            rule_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            rule_groups.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rule_groups.delete,
        )
        self.list_all = async_to_raw_response_wrapper(
            rule_groups.list_all,
        )
        self.list_rules = async_to_raw_response_wrapper(
            rule_groups.list_rules,
        )
        self.test_transactions = async_to_raw_response_wrapper(
            rule_groups.test_transactions,
        )
        self.trigger_rules = async_to_raw_response_wrapper(
            rule_groups.trigger_rules,
        )


class RuleGroupsResourceWithStreamingResponse:
    def __init__(self, rule_groups: RuleGroupsResource) -> None:
        self._rule_groups = rule_groups

        self.create = to_streamed_response_wrapper(
            rule_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            rule_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            rule_groups.update,
        )
        self.delete = to_streamed_response_wrapper(
            rule_groups.delete,
        )
        self.list_all = to_streamed_response_wrapper(
            rule_groups.list_all,
        )
        self.list_rules = to_streamed_response_wrapper(
            rule_groups.list_rules,
        )
        self.test_transactions = to_streamed_response_wrapper(
            rule_groups.test_transactions,
        )
        self.trigger_rules = to_streamed_response_wrapper(
            rule_groups.trigger_rules,
        )


class AsyncRuleGroupsResourceWithStreamingResponse:
    def __init__(self, rule_groups: AsyncRuleGroupsResource) -> None:
        self._rule_groups = rule_groups

        self.create = async_to_streamed_response_wrapper(
            rule_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            rule_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            rule_groups.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rule_groups.delete,
        )
        self.list_all = async_to_streamed_response_wrapper(
            rule_groups.list_all,
        )
        self.list_rules = async_to_streamed_response_wrapper(
            rule_groups.list_rules,
        )
        self.test_transactions = async_to_streamed_response_wrapper(
            rule_groups.test_transactions,
        )
        self.trigger_rules = async_to_streamed_response_wrapper(
            rule_groups.trigger_rules,
        )
