# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types import UserGroupSingle, UserGroupListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        user_group = client.user_groups.retrieve(
            id="123",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        user_group = client.user_groups.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.user_groups.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.user_groups.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(UserGroupSingle, user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.user_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Firefly) -> None:
        user_group = client.user_groups.update(
            id="1",
            title="New user group title",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Firefly) -> None:
        user_group = client.user_groups.update(
            id="1",
            title="New user group title",
            primary_currency_code="EUR",
            primary_currency_id="1",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Firefly) -> None:
        response = client.user_groups.with_raw_response.update(
            id="1",
            title="New user group title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Firefly) -> None:
        with client.user_groups.with_streaming_response.update(
            id="1",
            title="New user group title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(UserGroupSingle, user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.user_groups.with_raw_response.update(
                id="",
                title="New user group title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Firefly) -> None:
        user_group = client.user_groups.list()
        assert_matches_type(UserGroupListResponse, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Firefly) -> None:
        user_group = client.user_groups.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserGroupListResponse, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Firefly) -> None:
        response = client.user_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(UserGroupListResponse, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Firefly) -> None:
        with client.user_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(UserGroupListResponse, user_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        user_group = await async_client.user_groups.retrieve(
            id="123",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        user_group = await async_client.user_groups.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.user_groups.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.user_groups.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(UserGroupSingle, user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.user_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFirefly) -> None:
        user_group = await async_client.user_groups.update(
            id="1",
            title="New user group title",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFirefly) -> None:
        user_group = await async_client.user_groups.update(
            id="1",
            title="New user group title",
            primary_currency_code="EUR",
            primary_currency_id="1",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFirefly) -> None:
        response = await async_client.user_groups.with_raw_response.update(
            id="1",
            title="New user group title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(UserGroupSingle, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFirefly) -> None:
        async with async_client.user_groups.with_streaming_response.update(
            id="1",
            title="New user group title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(UserGroupSingle, user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.user_groups.with_raw_response.update(
                id="",
                title="New user group title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFirefly) -> None:
        user_group = await async_client.user_groups.list()
        assert_matches_type(UserGroupListResponse, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFirefly) -> None:
        user_group = await async_client.user_groups.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(UserGroupListResponse, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFirefly) -> None:
        response = await async_client.user_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(UserGroupListResponse, user_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFirefly) -> None:
        async with async_client.user_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(UserGroupListResponse, user_group, path=["response"])

        assert cast(Any, response.is_closed) is True
