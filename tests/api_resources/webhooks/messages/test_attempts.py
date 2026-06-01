# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types.webhooks.messages import AttemptListResponse, AttemptRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttempts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        attempt = client.webhooks.messages.attempts.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
        )
        assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        attempt = client.webhooks.messages.attempts.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.webhooks.messages.attempts.with_raw_response.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attempt = response.parse()
        assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.webhooks.messages.attempts.with_streaming_response.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attempt = response.parse()
            assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.messages.attempts.with_raw_response.retrieve(
                attempt_id=1,
                id="",
                message_id=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Firefly) -> None:
        attempt = client.webhooks.messages.attempts.list(
            message_id=1,
            id="123",
        )
        assert_matches_type(AttemptListResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Firefly) -> None:
        attempt = client.webhooks.messages.attempts.list(
            message_id=1,
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttemptListResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Firefly) -> None:
        response = client.webhooks.messages.attempts.with_raw_response.list(
            message_id=1,
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attempt = response.parse()
        assert_matches_type(AttemptListResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Firefly) -> None:
        with client.webhooks.messages.attempts.with_streaming_response.list(
            message_id=1,
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attempt = response.parse()
            assert_matches_type(AttemptListResponse, attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.messages.attempts.with_raw_response.list(
                message_id=1,
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Firefly) -> None:
        attempt = client.webhooks.messages.attempts.delete(
            attempt_id=1,
            id="123",
            message_id=1,
        )
        assert attempt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Firefly) -> None:
        attempt = client.webhooks.messages.attempts.delete(
            attempt_id=1,
            id="123",
            message_id=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert attempt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Firefly) -> None:
        response = client.webhooks.messages.attempts.with_raw_response.delete(
            attempt_id=1,
            id="123",
            message_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attempt = response.parse()
        assert attempt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Firefly) -> None:
        with client.webhooks.messages.attempts.with_streaming_response.delete(
            attempt_id=1,
            id="123",
            message_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attempt = response.parse()
            assert attempt is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.messages.attempts.with_raw_response.delete(
                attempt_id=1,
                id="",
                message_id=1,
            )


class TestAsyncAttempts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        attempt = await async_client.webhooks.messages.attempts.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
        )
        assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        attempt = await async_client.webhooks.messages.attempts.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.webhooks.messages.attempts.with_raw_response.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attempt = await response.parse()
        assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.webhooks.messages.attempts.with_streaming_response.retrieve(
            attempt_id=1,
            id="123",
            message_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attempt = await response.parse()
            assert_matches_type(AttemptRetrieveResponse, attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.messages.attempts.with_raw_response.retrieve(
                attempt_id=1,
                id="",
                message_id=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFirefly) -> None:
        attempt = await async_client.webhooks.messages.attempts.list(
            message_id=1,
            id="123",
        )
        assert_matches_type(AttemptListResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFirefly) -> None:
        attempt = await async_client.webhooks.messages.attempts.list(
            message_id=1,
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttemptListResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFirefly) -> None:
        response = await async_client.webhooks.messages.attempts.with_raw_response.list(
            message_id=1,
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attempt = await response.parse()
        assert_matches_type(AttemptListResponse, attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFirefly) -> None:
        async with async_client.webhooks.messages.attempts.with_streaming_response.list(
            message_id=1,
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attempt = await response.parse()
            assert_matches_type(AttemptListResponse, attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.messages.attempts.with_raw_response.list(
                message_id=1,
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFirefly) -> None:
        attempt = await async_client.webhooks.messages.attempts.delete(
            attempt_id=1,
            id="123",
            message_id=1,
        )
        assert attempt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncFirefly) -> None:
        attempt = await async_client.webhooks.messages.attempts.delete(
            attempt_id=1,
            id="123",
            message_id=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert attempt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFirefly) -> None:
        response = await async_client.webhooks.messages.attempts.with_raw_response.delete(
            attempt_id=1,
            id="123",
            message_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attempt = await response.parse()
        assert attempt is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFirefly) -> None:
        async with async_client.webhooks.messages.attempts.with_streaming_response.delete(
            attempt_id=1,
            id="123",
            message_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attempt = await response.parse()
            assert attempt is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.messages.attempts.with_raw_response.delete(
                attempt_id=1,
                id="",
                message_id=1,
            )
