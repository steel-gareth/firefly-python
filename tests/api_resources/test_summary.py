# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import SummaryRetrieveBasicResponse
from emcees_prod_testing_5._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_basic(self, client: EmceesProdTesting5) -> None:
        summary = client.summary.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_basic_with_all_params(self, client: EmceesProdTesting5) -> None:
        summary = client.summary.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            currency_code="currency_code",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_basic(self, client: EmceesProdTesting5) -> None:
        response = client.summary.with_raw_response.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_basic(self, client: EmceesProdTesting5) -> None:
        with client.summary.with_streaming_response.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_basic(self, async_client: AsyncEmceesProdTesting5) -> None:
        summary = await async_client.summary.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_basic_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        summary = await async_client.summary.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            currency_code="currency_code",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_basic(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.summary.with_raw_response.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_basic(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.summary.with_streaming_response.retrieve_basic(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryRetrieveBasicResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
