# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ConfigValueFilter, configuration_update_value_params
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
from ..types.config_value_filter import ConfigValueFilter
from ..types.configuration_single import ConfigurationSingle
from ..types.polymorphic_property_param import PolymorphicPropertyParam
from ..types.configuration_retrieve_response import ConfigurationRetrieveResponse

__all__ = ["ConfigurationResource", "AsyncConfigurationResource"]


class ConfigurationResource(SyncAPIResource):
    """These endpoints allow you to manage and update the Firefly III configuration.

    You need to have the &quot;owner&quot; role to update configuration.
    """

    @cached_property
    def with_raw_response(self) -> ConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return ConfigurationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationRetrieveResponse:
        """
        Returns all editable and not-editable configuration values for this Firefly III
        installation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationRetrieveResponse,
        )

    def retrieve_value(
        self,
        name: ConfigValueFilter,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationSingle:
        """
        Returns one configuration variable for this Firefly III installation

        Args:
          name: Title of the configuration value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/configuration/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationSingle,
        )

    def update_value(
        self,
        name: Literal[
            "configuration.is_demo_site",
            "configuration.permission_update_check",
            "configuration.last_update_check",
            "configuration.single_user_mode",
            "configuration.enable_exchange_rates",
            "configuration.use_running_balance",
            "configuration.enable_external_map",
            "configuration.enable_external_rates",
            "configuration.allow_webhooks",
            "configuration.valid_url_protocols",
        ],
        *,
        value: PolymorphicPropertyParam,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationSingle:
        """Set a single configuration value.

        Not all configuration values can be updated so
        the list of accepted configuration variables is small.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._put(
            path_template("/v1/configuration/{name}", name=name),
            body=maybe_transform({"value": value}, configuration_update_value_params.ConfigurationUpdateValueParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationSingle,
        )


class AsyncConfigurationResource(AsyncAPIResource):
    """These endpoints allow you to manage and update the Firefly III configuration.

    You need to have the &quot;owner&quot; role to update configuration.
    """

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncConfigurationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationRetrieveResponse:
        """
        Returns all editable and not-editable configuration values for this Firefly III
        installation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationRetrieveResponse,
        )

    async def retrieve_value(
        self,
        name: ConfigValueFilter,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationSingle:
        """
        Returns one configuration variable for this Firefly III installation

        Args:
          name: Title of the configuration value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/configuration/{name}", name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationSingle,
        )

    async def update_value(
        self,
        name: Literal[
            "configuration.is_demo_site",
            "configuration.permission_update_check",
            "configuration.last_update_check",
            "configuration.single_user_mode",
            "configuration.enable_exchange_rates",
            "configuration.use_running_balance",
            "configuration.enable_external_map",
            "configuration.enable_external_rates",
            "configuration.allow_webhooks",
            "configuration.valid_url_protocols",
        ],
        *,
        value: PolymorphicPropertyParam,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationSingle:
        """Set a single configuration value.

        Not all configuration values can be updated so
        the list of accepted configuration variables is small.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._put(
            path_template("/v1/configuration/{name}", name=name),
            body=await async_maybe_transform(
                {"value": value}, configuration_update_value_params.ConfigurationUpdateValueParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationSingle,
        )


class ConfigurationResourceWithRawResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = to_raw_response_wrapper(
            configuration.retrieve,
        )
        self.retrieve_value = to_raw_response_wrapper(
            configuration.retrieve_value,
        )
        self.update_value = to_raw_response_wrapper(
            configuration.update_value,
        )


class AsyncConfigurationResourceWithRawResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = async_to_raw_response_wrapper(
            configuration.retrieve,
        )
        self.retrieve_value = async_to_raw_response_wrapper(
            configuration.retrieve_value,
        )
        self.update_value = async_to_raw_response_wrapper(
            configuration.update_value,
        )


class ConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = to_streamed_response_wrapper(
            configuration.retrieve,
        )
        self.retrieve_value = to_streamed_response_wrapper(
            configuration.retrieve_value,
        )
        self.update_value = to_streamed_response_wrapper(
            configuration.update_value,
        )


class AsyncConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = async_to_streamed_response_wrapper(
            configuration.retrieve,
        )
        self.retrieve_value = async_to_streamed_response_wrapper(
            configuration.retrieve_value,
        )
        self.update_value = async_to_streamed_response_wrapper(
            configuration.update_value,
        )
