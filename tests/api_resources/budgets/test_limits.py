# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types import TransactionArray
from firefly._utils import parse_date, parse_datetime
from firefly.types.budgets import (
    BudgetLimitArray,
    BudgetLimitSingle,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Firefly) -> None:
        limit = client.budgets.limits.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Firefly) -> None:
        limit = client.budgets.limits.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            currency_code="EUR",
            currency_id="5",
            fire_webhooks=True,
            notes="Some example notes",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Firefly) -> None:
        response = client.budgets.limits.with_raw_response.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Firefly) -> None:
        with client.budgets.limits.with_streaming_response.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(BudgetLimitSingle, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.limits.with_raw_response.create(
                id="",
                amount="123.45",
                end=parse_date("2026-04-30"),
                start=parse_date("2026-04-01"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        limit = client.budgets.limits.retrieve(
            limit_id=1,
            id="123",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        limit = client.budgets.limits.retrieve(
            limit_id=1,
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.budgets.limits.with_raw_response.retrieve(
            limit_id=1,
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.budgets.limits.with_streaming_response.retrieve(
            limit_id=1,
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(BudgetLimitSingle, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.limits.with_raw_response.retrieve(
                limit_id=1,
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Firefly) -> None:
        limit = client.budgets.limits.update(
            limit_id="123",
            id="123",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Firefly) -> None:
        limit = client.budgets.limits.update(
            limit_id="123",
            id="123",
            amount="123.45",
            currency_code="EUR",
            currency_id="5",
            currency_name="Euro",
            end=parse_datetime("2026-04-30T23:59:59+00:00"),
            fire_webhooks=True,
            notes="Some example notes",
            start=parse_datetime("2026-04-01T00:00:00+00:00"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Firefly) -> None:
        response = client.budgets.limits.with_raw_response.update(
            limit_id="123",
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Firefly) -> None:
        with client.budgets.limits.with_streaming_response.update(
            limit_id="123",
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(BudgetLimitSingle, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.limits.with_raw_response.update(
                limit_id="123",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `limit_id` but received ''"):
            client.budgets.limits.with_raw_response.update(
                limit_id="",
                id="123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Firefly) -> None:
        limit = client.budgets.limits.delete(
            limit_id="123",
            id="123",
        )
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Firefly) -> None:
        limit = client.budgets.limits.delete(
            limit_id="123",
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Firefly) -> None:
        response = client.budgets.limits.with_raw_response.delete(
            limit_id="123",
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Firefly) -> None:
        with client.budgets.limits.with_streaming_response.delete(
            limit_id="123",
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert limit is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.limits.with_raw_response.delete(
                limit_id="123",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `limit_id` but received ''"):
            client.budgets.limits.with_raw_response.delete(
                limit_id="",
                id="123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_0(self, client: Firefly) -> None:
        limit = client.budgets.limits.list_0(
            id="123",
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_0_with_all_params(self, client: Firefly) -> None:
        limit = client.budgets.limits.list_0(
            id="123",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_0(self, client: Firefly) -> None:
        response = client.budgets.limits.with_raw_response.list_0(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_0(self, client: Firefly) -> None:
        with client.budgets.limits.with_streaming_response.list_0(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(BudgetLimitArray, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_0(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.limits.with_raw_response.list_0(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_1(self, client: Firefly) -> None:
        limit = client.budgets.limits.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_1_with_all_params(self, client: Firefly) -> None:
        limit = client.budgets.limits.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_1(self, client: Firefly) -> None:
        response = client.budgets.limits.with_raw_response.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_1(self, client: Firefly) -> None:
        with client.budgets.limits.with_streaming_response.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(BudgetLimitArray, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: Firefly) -> None:
        limit = client.budgets.limits.list_transactions(
            limit_id="123",
            id="123",
        )
        assert_matches_type(TransactionArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: Firefly) -> None:
        limit = client.budgets.limits.list_transactions(
            limit_id="123",
            id="123",
            limit=10,
            page=1,
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: Firefly) -> None:
        response = client.budgets.limits.with_raw_response.list_transactions(
            limit_id="123",
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(TransactionArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: Firefly) -> None:
        with client.budgets.limits.with_streaming_response.list_transactions(
            limit_id="123",
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(TransactionArray, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_transactions(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.limits.with_raw_response.list_transactions(
                limit_id="123",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `limit_id` but received ''"):
            client.budgets.limits.with_raw_response.list_transactions(
                limit_id="",
                id="123",
            )


class TestAsyncLimits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            currency_code="EUR",
            currency_id="5",
            fire_webhooks=True,
            notes="Some example notes",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFirefly) -> None:
        response = await async_client.budgets.limits.with_raw_response.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFirefly) -> None:
        async with async_client.budgets.limits.with_streaming_response.create(
            id="123",
            amount="123.45",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(BudgetLimitSingle, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.limits.with_raw_response.create(
                id="",
                amount="123.45",
                end=parse_date("2026-04-30"),
                start=parse_date("2026-04-01"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.retrieve(
            limit_id=1,
            id="123",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.retrieve(
            limit_id=1,
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.budgets.limits.with_raw_response.retrieve(
            limit_id=1,
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.budgets.limits.with_streaming_response.retrieve(
            limit_id=1,
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(BudgetLimitSingle, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.limits.with_raw_response.retrieve(
                limit_id=1,
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.update(
            limit_id="123",
            id="123",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.update(
            limit_id="123",
            id="123",
            amount="123.45",
            currency_code="EUR",
            currency_id="5",
            currency_name="Euro",
            end=parse_datetime("2026-04-30T23:59:59+00:00"),
            fire_webhooks=True,
            notes="Some example notes",
            start=parse_datetime("2026-04-01T00:00:00+00:00"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFirefly) -> None:
        response = await async_client.budgets.limits.with_raw_response.update(
            limit_id="123",
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(BudgetLimitSingle, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFirefly) -> None:
        async with async_client.budgets.limits.with_streaming_response.update(
            limit_id="123",
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(BudgetLimitSingle, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.limits.with_raw_response.update(
                limit_id="123",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `limit_id` but received ''"):
            await async_client.budgets.limits.with_raw_response.update(
                limit_id="",
                id="123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.delete(
            limit_id="123",
            id="123",
        )
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.delete(
            limit_id="123",
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFirefly) -> None:
        response = await async_client.budgets.limits.with_raw_response.delete(
            limit_id="123",
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert limit is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFirefly) -> None:
        async with async_client.budgets.limits.with_streaming_response.delete(
            limit_id="123",
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert limit is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.limits.with_raw_response.delete(
                limit_id="123",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `limit_id` but received ''"):
            await async_client.budgets.limits.with_raw_response.delete(
                limit_id="",
                id="123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_0(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.list_0(
            id="123",
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_0_with_all_params(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.list_0(
            id="123",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_0(self, async_client: AsyncFirefly) -> None:
        response = await async_client.budgets.limits.with_raw_response.list_0(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_0(self, async_client: AsyncFirefly) -> None:
        async with async_client.budgets.limits.with_streaming_response.list_0(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(BudgetLimitArray, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_0(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.limits.with_raw_response.list_0(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_1(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_1_with_all_params(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_1(self, async_client: AsyncFirefly) -> None:
        response = await async_client.budgets.limits.with_raw_response.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(BudgetLimitArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_1(self, async_client: AsyncFirefly) -> None:
        async with async_client.budgets.limits.with_streaming_response.list_1(
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(BudgetLimitArray, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.list_transactions(
            limit_id="123",
            id="123",
        )
        assert_matches_type(TransactionArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncFirefly) -> None:
        limit = await async_client.budgets.limits.list_transactions(
            limit_id="123",
            id="123",
            limit=10,
            page=1,
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        response = await async_client.budgets.limits.with_raw_response.list_transactions(
            limit_id="123",
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(TransactionArray, limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        async with async_client.budgets.limits.with_streaming_response.list_transactions(
            limit_id="123",
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(TransactionArray, limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.limits.with_raw_response.list_transactions(
                limit_id="123",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `limit_id` but received ''"):
            await async_client.budgets.limits.with_raw_response.list_transactions(
                limit_id="",
                id="123",
            )
