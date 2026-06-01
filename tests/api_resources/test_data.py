# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_destroy(self, client: EmceesProdTesting5) -> None:
        data = client.data.destroy(
            objects="not_assets_liabilities",
        )
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_destroy_with_all_params(self, client: EmceesProdTesting5) -> None:
        data = client.data.destroy(
            objects="not_assets_liabilities",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_destroy(self, client: EmceesProdTesting5) -> None:
        response = client.data.with_raw_response.destroy(
            objects="not_assets_liabilities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = response.parse()
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_destroy(self, client: EmceesProdTesting5) -> None:
        with client.data.with_streaming_response.destroy(
            objects="not_assets_liabilities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = response.parse()
            assert data is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_purge(self, client: EmceesProdTesting5) -> None:
        data = client.data.purge()
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_purge_with_all_params(self, client: EmceesProdTesting5) -> None:
        data = client.data.purge(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_purge(self, client: EmceesProdTesting5) -> None:
        response = client.data.with_raw_response.purge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = response.parse()
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_purge(self, client: EmceesProdTesting5) -> None:
        with client.data.with_streaming_response.purge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = response.parse()
            assert data is None

        assert cast(Any, response.is_closed) is True


class TestAsyncData:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_destroy(self, async_client: AsyncEmceesProdTesting5) -> None:
        data = await async_client.data.destroy(
            objects="not_assets_liabilities",
        )
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_destroy_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        data = await async_client.data.destroy(
            objects="not_assets_liabilities",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_destroy(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.data.with_raw_response.destroy(
            objects="not_assets_liabilities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = await response.parse()
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_destroy(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.data.with_streaming_response.destroy(
            objects="not_assets_liabilities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = await response.parse()
            assert data is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_purge(self, async_client: AsyncEmceesProdTesting5) -> None:
        data = await async_client.data.purge()
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_purge_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        data = await async_client.data.purge(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_purge(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.data.with_raw_response.purge()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = await response.parse()
        assert data is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_purge(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.data.with_streaming_response.purge() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = await response.parse()
            assert data is None

        assert cast(Any, response.is_closed) is True
