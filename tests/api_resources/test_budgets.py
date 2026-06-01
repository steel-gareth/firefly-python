# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    BudgetSingle,
    AttachmentArray,
    TransactionArray,
    BudgetListResponse,
)
from emcees_prod_testing_5._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBudgets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.create(
            name="Bills",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.create(
            name="Bills",
            active=False,
            auto_budget_amount="-1012.12",
            auto_budget_currency_code="EUR",
            auto_budget_currency_id="12",
            auto_budget_period="monthly",
            auto_budget_type="reset",
            fire_webhooks=True,
            notes="Some notes",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.create(
            name="Bills",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.create(
            name="Bills",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetSingle, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.retrieve(
            id="123",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.retrieve(
            id="123",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetSingle, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.update(
            id="123",
            name="Bills",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.update(
            id="123",
            name="Bills",
            active=False,
            auto_budget_amount="-1012.12",
            auto_budget_currency_code="EUR",
            auto_budget_currency_id="12",
            auto_budget_period="monthly",
            auto_budget_type="reset",
            fire_webhooks=True,
            notes="Some notes",
            order=5,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.update(
            id="123",
            name="Bills",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.update(
            id="123",
            name="Bills",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetSingle, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.with_raw_response.update(
                id="",
                name="Bills",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list(
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetListResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.delete(
            id="123",
        )
        assert budget is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert budget is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert budget is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert budget is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_attachments(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(AttachmentArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_attachments(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(AttachmentArray, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_attachments(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list_transactions(
            id="123",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.list_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.list_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(TransactionArray, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_transactions(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.budgets.with_raw_response.list_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_without_budget(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list_transactions_without_budget()
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_without_budget_with_all_params(self, client: EmceesProdTesting5) -> None:
        budget = client.budgets.list_transactions_without_budget(
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions_without_budget(self, client: EmceesProdTesting5) -> None:
        response = client.budgets.with_raw_response.list_transactions_without_budget()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions_without_budget(self, client: EmceesProdTesting5) -> None:
        with client.budgets.with_streaming_response.list_transactions_without_budget() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(TransactionArray, budget, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBudgets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.create(
            name="Bills",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.create(
            name="Bills",
            active=False,
            auto_budget_amount="-1012.12",
            auto_budget_currency_code="EUR",
            auto_budget_currency_id="12",
            auto_budget_period="monthly",
            auto_budget_type="reset",
            fire_webhooks=True,
            notes="Some notes",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.create(
            name="Bills",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.budgets.with_streaming_response.create(
            name="Bills",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetSingle, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.retrieve(
            id="123",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.retrieve(
            id="123",
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.budgets.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetSingle, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.update(
            id="123",
            name="Bills",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.update(
            id="123",
            name="Bills",
            active=False,
            auto_budget_amount="-1012.12",
            auto_budget_currency_code="EUR",
            auto_budget_currency_id="12",
            auto_budget_period="monthly",
            auto_budget_type="reset",
            fire_webhooks=True,
            notes="Some notes",
            order=5,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.update(
            id="123",
            name="Bills",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetSingle, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.budgets.with_streaming_response.update(
            id="123",
            name="Bills",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetSingle, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.with_raw_response.update(
                id="",
                name="Bills",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.list()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.list(
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.budgets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetListResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.delete(
            id="123",
        )
        assert budget is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert budget is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert budget is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.budgets.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert budget is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(AttachmentArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.budgets.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(AttachmentArray, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.list_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.list_transactions(
            id="123",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.list_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.budgets.with_streaming_response.list_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(TransactionArray, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.budgets.with_raw_response.list_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_without_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        budget = await async_client.budgets.list_transactions_without_budget()
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_without_budget_with_all_params(
        self, async_client: AsyncEmceesProdTesting5
    ) -> None:
        budget = await async_client.budgets.list_transactions_without_budget(
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions_without_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.budgets.with_raw_response.list_transactions_without_budget()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(TransactionArray, budget, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions_without_budget(
        self, async_client: AsyncEmceesProdTesting5
    ) -> None:
        async with async_client.budgets.with_streaming_response.list_transactions_without_budget() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(TransactionArray, budget, path=["response"])

        assert cast(Any, response.is_closed) is True
