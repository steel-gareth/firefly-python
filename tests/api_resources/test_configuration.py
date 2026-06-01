# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    ConfigurationSingle,
    ConfigurationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfiguration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        configuration = client.configuration.retrieve()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        configuration = client.configuration.retrieve(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.configuration.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.configuration.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_value(self, client: EmceesProdTesting5) -> None:
        configuration = client.configuration.retrieve_value(
            name="configuration.is_demo_site",
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_value_with_all_params(self, client: EmceesProdTesting5) -> None:
        configuration = client.configuration.retrieve_value(
            name="configuration.is_demo_site",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_value(self, client: EmceesProdTesting5) -> None:
        response = client.configuration.with_raw_response.retrieve_value(
            name="configuration.is_demo_site",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_value(self, client: EmceesProdTesting5) -> None:
        with client.configuration.with_streaming_response.retrieve_value(
            name="configuration.is_demo_site",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationSingle, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_value(self, client: EmceesProdTesting5) -> None:
        configuration = client.configuration.update_value(
            name="configuration.is_demo_site",
            value=True,
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_value_with_all_params(self, client: EmceesProdTesting5) -> None:
        configuration = client.configuration.update_value(
            name="configuration.is_demo_site",
            value=True,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_value(self, client: EmceesProdTesting5) -> None:
        response = client.configuration.with_raw_response.update_value(
            name="configuration.is_demo_site",
            value=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_value(self, client: EmceesProdTesting5) -> None:
        with client.configuration.with_streaming_response.update_value(
            name="configuration.is_demo_site",
            value=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationSingle, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfiguration:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        configuration = await async_client.configuration.retrieve()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        configuration = await async_client.configuration.retrieve(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.configuration.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.configuration.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationRetrieveResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_value(self, async_client: AsyncEmceesProdTesting5) -> None:
        configuration = await async_client.configuration.retrieve_value(
            name="configuration.is_demo_site",
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_value_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        configuration = await async_client.configuration.retrieve_value(
            name="configuration.is_demo_site",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_value(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.configuration.with_raw_response.retrieve_value(
            name="configuration.is_demo_site",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_value(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.configuration.with_streaming_response.retrieve_value(
            name="configuration.is_demo_site",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationSingle, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_value(self, async_client: AsyncEmceesProdTesting5) -> None:
        configuration = await async_client.configuration.update_value(
            name="configuration.is_demo_site",
            value=True,
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_value_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        configuration = await async_client.configuration.update_value(
            name="configuration.is_demo_site",
            value=True,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_value(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.configuration.with_raw_response.update_value(
            name="configuration.is_demo_site",
            value=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationSingle, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_value(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.configuration.with_streaming_response.update_value(
            name="configuration.is_demo_site",
            value=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationSingle, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
