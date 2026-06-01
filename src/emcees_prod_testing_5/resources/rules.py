# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ..types import (
    RuleTriggerType,
    rule_list_params,
    rule_test_params,
    rule_create_params,
    rule_update_params,
    rule_trigger_params,
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
from ..types.rule_single import RuleSingle
from ..types.rule_trigger_type import RuleTriggerType
from ..types.transaction_array import TransactionArray

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    """These endpoints can be used to manage all of the user&#039;s rules.

    Also includes triggers to execute or test rules and individual triggers.
    """

    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        actions: Iterable[rule_create_params.Action],
        rule_group_id: str,
        title: str,
        trigger: RuleTriggerType,
        triggers: Iterable[rule_create_params.Trigger],
        active: bool | Omit = omit,
        description: str | Omit = omit,
        order: int | Omit = omit,
        rule_group_title: str | Omit = omit,
        stop_processing: bool | Omit = omit,
        strict: bool | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleSingle:
        """Creates a new rule.

        The data required can be submitted as a JSON body or as a
        list of parameters.

        Args:
          rule_group_id: ID of the rule group under which the rule must be stored. Either this field or
              rule_group_title is mandatory.

          trigger: Which action is necessary for the rule to fire? Use either store-journal,
              update-journal or manual-activation.

          active: Whether or not the rule is even active. Default is true.

          rule_group_title: Title of the rule group under which the rule must be stored. Either this field
              or rule_group_id is mandatory.

          stop_processing: If this value is true and the rule is triggered, other rules after this one in
              the group will be skipped. Default value is false.

          strict: If the rule is set to be strict, ALL triggers must hit in order for the rule to
              fire. Otherwise, just one is enough. Default value is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/rules",
            body=maybe_transform(
                {
                    "actions": actions,
                    "rule_group_id": rule_group_id,
                    "title": title,
                    "trigger": trigger,
                    "triggers": triggers,
                    "active": active,
                    "description": description,
                    "order": order,
                    "rule_group_title": rule_group_title,
                    "stop_processing": stop_processing,
                    "strict": strict,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleSingle,
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
    ) -> RuleSingle:
        """
        Get a single rule.

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
            path_template("/v1/rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleSingle,
        )

    def update(
        self,
        id: str,
        *,
        actions: Iterable[rule_update_params.Action] | Omit = omit,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        order: int | Omit = omit,
        rule_group_id: str | Omit = omit,
        stop_processing: bool | Omit = omit,
        strict: bool | Omit = omit,
        title: str | Omit = omit,
        trigger: RuleTriggerType | Omit = omit,
        triggers: Iterable[rule_update_params.Trigger] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleSingle:
        """Update existing rule.

        Args:
          active: Whether or not the rule is even active.

        Default is true.

          rule_group_id: ID of the rule group under which the rule must be stored. Either this field or
              rule_group_title is mandatory.

          stop_processing: If this value is true and the rule is triggered, other rules after this one in
              the group will be skipped. Default value is false.

          strict: If the rule is set to be strict, ALL triggers must hit in order for the rule to
              fire. Otherwise, just one is enough. Default value is true.

          trigger: Which action is necessary for the rule to fire? Use either store-journal,
              update-journal or manual-activation.

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
            path_template("/v1/rules/{id}", id=id),
            body=maybe_transform(
                {
                    "actions": actions,
                    "active": active,
                    "description": description,
                    "order": order,
                    "rule_group_id": rule_group_id,
                    "stop_processing": stop_processing,
                    "strict": strict,
                    "title": title,
                    "trigger": trigger,
                    "triggers": triggers,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleSingle,
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
    ) -> RuleArray:
        """List all rules.

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
            "/v1/rules",
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
                    rule_list_params.RuleListParams,
                ),
            ),
            cast_to=RuleArray,
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
        Delete an rule.

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
            path_template("/v1/rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def test(
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
    ) -> TransactionArray:
        """Test which transactions would be hit by the rule.

        No changes will be made. Limit
        the result if you want to.

        Args:
          accounts: Limit the testing of the rule to these asset accounts or liabilities. Only asset
              accounts and liabilities will be accepted. Other types will be silently dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

          start: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

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
            path_template("/v1/rules/{id}/test", id=id),
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
                    rule_test_params.RuleTestParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    def trigger(
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
        the group. Limit the result if you want to.

        Args:
          accounts: Limit the triggering of the rule to these asset accounts or liabilities. Only
              asset accounts and liabilities will be accepted. Other types will be silently
              dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. If the end date is not present, it will be set to today. If you use
              this field, both the start date and the end date must be present.

          start: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. If the start date is not present, it will be set to one year ago. If
              you use this field, both the start date and the end date must be present.

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
            path_template("/v1/rules/{id}/trigger", id=id),
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
                    rule_trigger_params.RuleTriggerParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncRulesResource(AsyncAPIResource):
    """These endpoints can be used to manage all of the user&#039;s rules.

    Also includes triggers to execute or test rules and individual triggers.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/emcees-prod-testing-5-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        actions: Iterable[rule_create_params.Action],
        rule_group_id: str,
        title: str,
        trigger: RuleTriggerType,
        triggers: Iterable[rule_create_params.Trigger],
        active: bool | Omit = omit,
        description: str | Omit = omit,
        order: int | Omit = omit,
        rule_group_title: str | Omit = omit,
        stop_processing: bool | Omit = omit,
        strict: bool | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleSingle:
        """Creates a new rule.

        The data required can be submitted as a JSON body or as a
        list of parameters.

        Args:
          rule_group_id: ID of the rule group under which the rule must be stored. Either this field or
              rule_group_title is mandatory.

          trigger: Which action is necessary for the rule to fire? Use either store-journal,
              update-journal or manual-activation.

          active: Whether or not the rule is even active. Default is true.

          rule_group_title: Title of the rule group under which the rule must be stored. Either this field
              or rule_group_id is mandatory.

          stop_processing: If this value is true and the rule is triggered, other rules after this one in
              the group will be skipped. Default value is false.

          strict: If the rule is set to be strict, ALL triggers must hit in order for the rule to
              fire. Otherwise, just one is enough. Default value is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/rules",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "rule_group_id": rule_group_id,
                    "title": title,
                    "trigger": trigger,
                    "triggers": triggers,
                    "active": active,
                    "description": description,
                    "order": order,
                    "rule_group_title": rule_group_title,
                    "stop_processing": stop_processing,
                    "strict": strict,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleSingle,
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
    ) -> RuleSingle:
        """
        Get a single rule.

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
            path_template("/v1/rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleSingle,
        )

    async def update(
        self,
        id: str,
        *,
        actions: Iterable[rule_update_params.Action] | Omit = omit,
        active: bool | Omit = omit,
        description: str | Omit = omit,
        order: int | Omit = omit,
        rule_group_id: str | Omit = omit,
        stop_processing: bool | Omit = omit,
        strict: bool | Omit = omit,
        title: str | Omit = omit,
        trigger: RuleTriggerType | Omit = omit,
        triggers: Iterable[rule_update_params.Trigger] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleSingle:
        """Update existing rule.

        Args:
          active: Whether or not the rule is even active.

        Default is true.

          rule_group_id: ID of the rule group under which the rule must be stored. Either this field or
              rule_group_title is mandatory.

          stop_processing: If this value is true and the rule is triggered, other rules after this one in
              the group will be skipped. Default value is false.

          strict: If the rule is set to be strict, ALL triggers must hit in order for the rule to
              fire. Otherwise, just one is enough. Default value is true.

          trigger: Which action is necessary for the rule to fire? Use either store-journal,
              update-journal or manual-activation.

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
            path_template("/v1/rules/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "active": active,
                    "description": description,
                    "order": order,
                    "rule_group_id": rule_group_id,
                    "stop_processing": stop_processing,
                    "strict": strict,
                    "title": title,
                    "trigger": trigger,
                    "triggers": triggers,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleSingle,
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
    ) -> RuleArray:
        """List all rules.

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
            "/v1/rules",
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
                    rule_list_params.RuleListParams,
                ),
            ),
            cast_to=RuleArray,
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
        Delete an rule.

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
            path_template("/v1/rules/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def test(
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
    ) -> TransactionArray:
        """Test which transactions would be hit by the rule.

        No changes will be made. Limit
        the result if you want to.

        Args:
          accounts: Limit the testing of the rule to these asset accounts or liabilities. Only asset
              accounts and liabilities will be accepted. Other types will be silently dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

          start: A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
              to. Both the start date and the end date must be present.

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
            path_template("/v1/rules/{id}/test", id=id),
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
                    rule_test_params.RuleTestParams,
                ),
            ),
            cast_to=TransactionArray,
        )

    async def trigger(
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
        the group. Limit the result if you want to.

        Args:
          accounts: Limit the triggering of the rule to these asset accounts or liabilities. Only
              asset accounts and liabilities will be accepted. Other types will be silently
              dropped.

          end: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. If the end date is not present, it will be set to today. If you use
              this field, both the start date and the end date must be present.

          start: A date formatted YYYY-MM-DD, to limit the transactions the actions will be
              applied to. If the start date is not present, it will be set to one year ago. If
              you use this field, both the start date and the end date must be present.

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
            path_template("/v1/rules/{id}/trigger", id=id),
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
                    rule_trigger_params.RuleTriggerParams,
                ),
            ),
            cast_to=NoneType,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            rules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.test = to_raw_response_wrapper(
            rules.test,
        )
        self.trigger = to_raw_response_wrapper(
            rules.trigger,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            rules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.test = async_to_raw_response_wrapper(
            rules.test,
        )
        self.trigger = async_to_raw_response_wrapper(
            rules.trigger,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            rules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.test = to_streamed_response_wrapper(
            rules.test,
        )
        self.trigger = to_streamed_response_wrapper(
            rules.trigger,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            rules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.test = async_to_streamed_response_wrapper(
            rules.test,
        )
        self.trigger = async_to_streamed_response_wrapper(
            rules.trigger,
        )
