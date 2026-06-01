# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import UserSingle, AboutRetrieveInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAbout:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info(self, client: EmceesProdTesting5) -> None:
        about = client.about.retrieve_info()
        assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info_with_all_params(self, client: EmceesProdTesting5) -> None:
        about = client.about.retrieve_info(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_info(self, client: EmceesProdTesting5) -> None:
        response = client.about.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        about = response.parse()
        assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_info(self, client: EmceesProdTesting5) -> None:
        with client.about.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            about = response.parse()
            assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_user(self, client: EmceesProdTesting5) -> None:
        about = client.about.retrieve_user()
        assert_matches_type(UserSingle, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_user_with_all_params(self, client: EmceesProdTesting5) -> None:
        about = client.about.retrieve_user(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserSingle, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_user(self, client: EmceesProdTesting5) -> None:
        response = client.about.with_raw_response.retrieve_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        about = response.parse()
        assert_matches_type(UserSingle, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_user(self, client: EmceesProdTesting5) -> None:
        with client.about.with_streaming_response.retrieve_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            about = response.parse()
            assert_matches_type(UserSingle, about, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAbout:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info(self, async_client: AsyncEmceesProdTesting5) -> None:
        about = await async_client.about.retrieve_info()
        assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        about = await async_client.about.retrieve_info(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_info(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.about.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        about = await response.parse()
        assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_info(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.about.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            about = await response.parse()
            assert_matches_type(AboutRetrieveInfoResponse, about, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_user(self, async_client: AsyncEmceesProdTesting5) -> None:
        about = await async_client.about.retrieve_user()
        assert_matches_type(UserSingle, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_user_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        about = await async_client.about.retrieve_user(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserSingle, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_user(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.about.with_raw_response.retrieve_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        about = await response.parse()
        assert_matches_type(UserSingle, about, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_user(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.about.with_streaming_response.retrieve_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            about = await response.parse()
            assert_matches_type(UserSingle, about, path=["response"])

        assert cast(Any, response.is_closed) is True
