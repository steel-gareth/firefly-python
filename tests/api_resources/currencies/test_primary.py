# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import CurrencySingle

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrimary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        primary = client.currencies.primary.retrieve()
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        primary = client.currencies.primary.retrieve(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.currencies.primary.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        primary = response.parse()
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.currencies.primary.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            primary = response.parse()
            assert_matches_type(CurrencySingle, primary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_make_primary(self, client: EmceesProdTesting5) -> None:
        primary = client.currencies.primary.make_primary(
            code="USD",
        )
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_make_primary_with_all_params(self, client: EmceesProdTesting5) -> None:
        primary = client.currencies.primary.make_primary(
            code="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_make_primary(self, client: EmceesProdTesting5) -> None:
        response = client.currencies.primary.with_raw_response.make_primary(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        primary = response.parse()
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_make_primary(self, client: EmceesProdTesting5) -> None:
        with client.currencies.primary.with_streaming_response.make_primary(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            primary = response.parse()
            assert_matches_type(CurrencySingle, primary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_make_primary(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.primary.with_raw_response.make_primary(
                code="",
            )


class TestAsyncPrimary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        primary = await async_client.currencies.primary.retrieve()
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        primary = await async_client.currencies.primary.retrieve(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.currencies.primary.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        primary = await response.parse()
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.currencies.primary.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            primary = await response.parse()
            assert_matches_type(CurrencySingle, primary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_make_primary(self, async_client: AsyncEmceesProdTesting5) -> None:
        primary = await async_client.currencies.primary.make_primary(
            code="USD",
        )
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_make_primary_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        primary = await async_client.currencies.primary.make_primary(
            code="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_make_primary(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.currencies.primary.with_raw_response.make_primary(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        primary = await response.parse()
        assert_matches_type(CurrencySingle, primary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_make_primary(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.currencies.primary.with_streaming_response.make_primary(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            primary = await response.parse()
            assert_matches_type(CurrencySingle, primary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_make_primary(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.primary.with_raw_response.make_primary(
                code="",
            )
