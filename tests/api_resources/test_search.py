# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    AccountArray,
    TransactionArray,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accounts(self, client: EmceesProdTesting5) -> None:
        search = client.search.accounts(
            field="all",
            query="checking",
        )
        assert_matches_type(AccountArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_accounts_with_all_params(self, client: EmceesProdTesting5) -> None:
        search = client.search.accounts(
            field="all",
            query="checking",
            limit=10,
            page=1,
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_accounts(self, client: EmceesProdTesting5) -> None:
        response = client.search.with_raw_response.accounts(
            field="all",
            query="checking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(AccountArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_accounts(self, client: EmceesProdTesting5) -> None:
        with client.search.with_streaming_response.accounts(
            field="all",
            query="checking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(AccountArray, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transactions(self, client: EmceesProdTesting5) -> None:
        search = client.search.transactions(
            query="groceries",
        )
        assert_matches_type(TransactionArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transactions_with_all_params(self, client: EmceesProdTesting5) -> None:
        search = client.search.transactions(
            query="groceries",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transactions(self, client: EmceesProdTesting5) -> None:
        response = client.search.with_raw_response.transactions(
            query="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(TransactionArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_transactions(self, client: EmceesProdTesting5) -> None:
        with client.search.with_streaming_response.transactions(
            query="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(TransactionArray, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accounts(self, async_client: AsyncEmceesProdTesting5) -> None:
        search = await async_client.search.accounts(
            field="all",
            query="checking",
        )
        assert_matches_type(AccountArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_accounts_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        search = await async_client.search.accounts(
            field="all",
            query="checking",
            limit=10,
            page=1,
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_accounts(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.search.with_raw_response.accounts(
            field="all",
            query="checking",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(AccountArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_accounts(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.search.with_streaming_response.accounts(
            field="all",
            query="checking",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(AccountArray, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        search = await async_client.search.transactions(
            query="groceries",
        )
        assert_matches_type(TransactionArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transactions_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        search = await async_client.search.transactions(
            query="groceries",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.search.with_raw_response.transactions(
            query="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(TransactionArray, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.search.with_streaming_response.transactions(
            query="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(TransactionArray, search, path=["response"])

        assert cast(Any, response.is_closed) is True
