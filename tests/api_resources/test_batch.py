# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_finish(self, client: Firefly) -> None:
        batch = client.batch.finish()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_finish_with_all_params(self, client: Firefly) -> None:
        batch = client.batch.finish(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_finish(self, client: Firefly) -> None:
        response = client.batch.with_raw_response.finish()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_finish(self, client: Firefly) -> None:
        with client.batch.with_streaming_response.finish() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_finish(self, async_client: AsyncFirefly) -> None:
        batch = await async_client.batch.finish()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_finish_with_all_params(self, async_client: AsyncFirefly) -> None:
        batch = await async_client.batch.finish(
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_finish(self, async_client: AsyncFirefly) -> None:
        response = await async_client.batch.with_raw_response.finish()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_finish(self, async_client: AsyncFirefly) -> None:
        async with async_client.batch.with_streaming_response.finish() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True
