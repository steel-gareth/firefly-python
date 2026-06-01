# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly._utils import parse_date
from firefly.types.chart import BalanceRetrieveBalanceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_balance(self, client: Firefly) -> None:
        balance = client.chart.balance.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_balance_with_all_params(self, client: Firefly) -> None:
        balance = client.chart.balance.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            period="1M",
            preselected="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balance(self, client: Firefly) -> None:
        response = client.chart.balance.with_raw_response.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: Firefly) -> None:
        with client.chart.balance.with_streaming_response.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBalance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncFirefly) -> None:
        balance = await async_client.chart.balance.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_balance_with_all_params(self, async_client: AsyncFirefly) -> None:
        balance = await async_client.chart.balance.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            period="1M",
            preselected="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncFirefly) -> None:
        response = await async_client.chart.balance.with_raw_response.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncFirefly) -> None:
        async with async_client.chart.balance.with_streaming_response.retrieve_balance(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceRetrieveBalanceResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True
