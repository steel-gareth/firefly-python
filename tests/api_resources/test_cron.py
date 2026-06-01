# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import CronRunResponse
from emcees_prod_testing_5._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCron:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: EmceesProdTesting5) -> None:
        cron = client.cron.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
        )
        assert_matches_type(CronRunResponse, cron, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: EmceesProdTesting5) -> None:
        cron = client.cron.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
            date=parse_date("2026-04-01"),
            force=False,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CronRunResponse, cron, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: EmceesProdTesting5) -> None:
        response = client.cron.with_raw_response.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron = response.parse()
        assert_matches_type(CronRunResponse, cron, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: EmceesProdTesting5) -> None:
        with client.cron.with_streaming_response.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron = response.parse()
            assert_matches_type(CronRunResponse, cron, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_run(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cli_token` but received ''"):
            client.cron.with_raw_response.run(
                cli_token="",
            )


class TestAsyncCron:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncEmceesProdTesting5) -> None:
        cron = await async_client.cron.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
        )
        assert_matches_type(CronRunResponse, cron, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        cron = await async_client.cron.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
            date=parse_date("2026-04-01"),
            force=False,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CronRunResponse, cron, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.cron.with_raw_response.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron = await response.parse()
        assert_matches_type(CronRunResponse, cron, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.cron.with_streaming_response.run(
            cli_token="d5ea6b5fb774618dd6ad6ba6e0a7f55c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron = await response.parse()
            assert_matches_type(CronRunResponse, cron, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_run(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `cli_token` but received ''"):
            await async_client.cron.with_raw_response.run(
                cli_token="",
            )
