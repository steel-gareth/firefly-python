# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5._utils import parse_date
from emcees_prod_testing_5.types.insight import (
    ExpenseGetTotalResponse,
    ExpenseListByTagResponse,
    ExpenseListByBillResponse,
    ExpenseListByBudgetResponse,
    ExpenseListByCategoryResponse,
    ExpenseListWithoutTagResponse,
    ExpenseListWithoutBillResponse,
    ExpenseListWithoutBudgetResponse,
    ExpenseListByAssetAccountResponse,
    ExpenseListWithoutCategoryResponse,
    ExpenseListByExpenseAccountResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExpense:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_total(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_total_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_total(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_total(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_asset_account(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_asset_account_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_asset_account(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_asset_account(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_bill(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_bill_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            bills=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_bill(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_bill(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_budget(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_budget_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            budgets=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_budget(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_budget(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_category(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_category_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            categories=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_category(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_category(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_expense_account(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_expense_account_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_expense_account(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_expense_account(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_tag(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_tag_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            tags=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_tag(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_tag(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_bill(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_bill_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_without_bill(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_without_bill(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_budget(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_budget_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_without_budget(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_without_budget(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_category(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_category_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_without_category(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_without_category(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_tag(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_without_tag_with_all_params(self, client: EmceesProdTesting5) -> None:
        expense = client.insight.expense.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_without_tag(self, client: EmceesProdTesting5) -> None:
        response = client.insight.expense.with_raw_response.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = response.parse()
        assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_without_tag(self, client: EmceesProdTesting5) -> None:
        with client.insight.expense.with_streaming_response.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = response.parse()
            assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExpense:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_total(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_total_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_total(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_total(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.get_total(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseGetTotalResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_asset_account(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_asset_account_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_asset_account(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_asset_account(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_by_asset_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListByAssetAccountResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_bill(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_bill_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            bills=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_bill(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_bill(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_by_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListByBillResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_budget_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            budgets=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_by_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListByBudgetResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_category(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_category_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            categories=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_category(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_category(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_by_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListByCategoryResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_expense_account(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_expense_account_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_expense_account(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_expense_account(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_by_expense_account(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListByExpenseAccountResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_tag(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_tag_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            tags=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_tag(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_tag(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_by_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListByTagResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_bill(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_bill_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_without_bill(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_without_bill(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_without_bill(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListWithoutBillResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_budget_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_without_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_without_budget(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_without_budget(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListWithoutBudgetResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_category(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_category_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_without_category(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_without_category(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_without_category(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListWithoutCategoryResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_tag(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_without_tag_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        expense = await async_client.insight.expense.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts=[1, 2, 3],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_without_tag(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.insight.expense.with_raw_response.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expense = await response.parse()
        assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_without_tag(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.insight.expense.with_streaming_response.list_without_tag(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expense = await response.parse()
            assert_matches_type(ExpenseListWithoutTagResponse, expense, path=["response"])

        assert cast(Any, response.is_closed) is True
