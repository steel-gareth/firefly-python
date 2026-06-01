# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types import (
    BillArray,
    RuleArray,
    AccountArray,
    CurrencySingle,
    RecurrenceArray,
    TransactionArray,
    AvailableBudgetArray,
    CurrencyListResponse,
)
from firefly._utils import parse_date
from firefly.types.budgets import BudgetLimitArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrencies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Firefly) -> None:
        currency = client.currencies.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
            decimal_places=2,
            enabled=True,
            primary=True,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        currency = client.currencies.retrieve(
            code="USD",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.retrieve(
            code="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.retrieve(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.retrieve(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.retrieve(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Firefly) -> None:
        currency = client.currencies.update(
            path_code="EUR",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.update(
            path_code="EUR",
            body_code="AMS",
            decimal_places=2,
            enabled=True,
            name="Ankh-Morpork dollar",
            primary=True,
            symbol="AM$",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.update(
            path_code="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.update(
            path_code="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_code` but received ''"):
            client.currencies.with_raw_response.update(
                path_code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Firefly) -> None:
        currency = client.currencies.list()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyListResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Firefly) -> None:
        currency = client.currencies.delete(
            code="GBP",
        )
        assert currency is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.delete(
            code="GBP",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert currency is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.delete(
            code="GBP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert currency is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.delete(
            code="GBP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert currency is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.delete(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable(self, client: Firefly) -> None:
        currency = client.currencies.disable(
            code="GBP",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.disable(
            code="GBP",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.disable(
            code="GBP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.disable(
            code="GBP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disable(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.disable(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable(self, client: Firefly) -> None:
        currency = client.currencies.enable(
            code="USD",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.enable(
            code="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.enable(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.enable(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_enable(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.enable(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_accounts(self, client: Firefly) -> None:
        currency = client.currencies.list_accounts(
            code="USD",
        )
        assert_matches_type(AccountArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_accounts_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list_accounts(
            code="USD",
            date=parse_date("2019-12-27"),
            limit=10,
            page=1,
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_accounts(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list_accounts(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(AccountArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_accounts(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list_accounts(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(AccountArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_accounts(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.list_accounts(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_available_budgets(self, client: Firefly) -> None:
        currency = client.currencies.list_available_budgets(
            code="EUR",
        )
        assert_matches_type(AvailableBudgetArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_available_budgets_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list_available_budgets(
            code="EUR",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AvailableBudgetArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_available_budgets(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list_available_budgets(
            code="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(AvailableBudgetArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_available_budgets(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list_available_budgets(
            code="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(AvailableBudgetArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_available_budgets(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.list_available_budgets(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_bills(self, client: Firefly) -> None:
        currency = client.currencies.list_bills(
            code="USD",
        )
        assert_matches_type(BillArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_bills_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list_bills(
            code="USD",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BillArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_bills(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list_bills(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(BillArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_bills(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list_bills(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(BillArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_bills(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.list_bills(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_budget_limits(self, client: Firefly) -> None:
        currency = client.currencies.list_budget_limits(
            code="USD",
        )
        assert_matches_type(BudgetLimitArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_budget_limits_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list_budget_limits(
            code="USD",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_budget_limits(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list_budget_limits(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(BudgetLimitArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_budget_limits(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list_budget_limits(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(BudgetLimitArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_budget_limits(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.list_budget_limits(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recurrences(self, client: Firefly) -> None:
        currency = client.currencies.list_recurrences(
            code="EUR",
        )
        assert_matches_type(RecurrenceArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recurrences_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list_recurrences(
            code="EUR",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_recurrences(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list_recurrences(
            code="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(RecurrenceArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_recurrences(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list_recurrences(
            code="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(RecurrenceArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_recurrences(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.list_recurrences(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rules(self, client: Firefly) -> None:
        currency = client.currencies.list_rules(
            code="USD",
        )
        assert_matches_type(RuleArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rules_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list_rules(
            code="USD",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_rules(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list_rules(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(RuleArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_rules(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list_rules(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(RuleArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_rules(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.list_rules(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: Firefly) -> None:
        currency = client.currencies.list_transactions(
            code="USD",
        )
        assert_matches_type(TransactionArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: Firefly) -> None:
        currency = client.currencies.list_transactions(
            code="USD",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: Firefly) -> None:
        response = client.currencies.with_raw_response.list_transactions(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(TransactionArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: Firefly) -> None:
        with client.currencies.with_streaming_response.list_transactions(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(TransactionArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_transactions(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.currencies.with_raw_response.list_transactions(
                code="",
            )


class TestAsyncCurrencies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
            decimal_places=2,
            enabled=True,
            primary=True,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.create(
            code="AMS",
            name="Ankh-Morpork dollar",
            symbol="AM$",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.retrieve(
            code="USD",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.retrieve(
            code="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.retrieve(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.retrieve(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.retrieve(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.update(
            path_code="EUR",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.update(
            path_code="EUR",
            body_code="AMS",
            decimal_places=2,
            enabled=True,
            name="Ankh-Morpork dollar",
            primary=True,
            symbol="AM$",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.update(
            path_code="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.update(
            path_code="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_code` but received ''"):
            await async_client.currencies.with_raw_response.update(
                path_code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyListResponse, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyListResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.delete(
            code="GBP",
        )
        assert currency is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.delete(
            code="GBP",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert currency is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.delete(
            code="GBP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert currency is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.delete(
            code="GBP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert currency is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.delete(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.disable(
            code="GBP",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.disable(
            code="GBP",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.disable(
            code="GBP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.disable(
            code="GBP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.disable(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.enable(
            code="USD",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.enable(
            code="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.enable(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencySingle, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.enable(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencySingle, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.enable(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_accounts(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_accounts(
            code="USD",
        )
        assert_matches_type(AccountArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_accounts_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_accounts(
            code="USD",
            date=parse_date("2019-12-27"),
            limit=10,
            page=1,
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_accounts(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list_accounts(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(AccountArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_accounts(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list_accounts(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(AccountArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_accounts(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.list_accounts(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_available_budgets(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_available_budgets(
            code="EUR",
        )
        assert_matches_type(AvailableBudgetArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_available_budgets_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_available_budgets(
            code="EUR",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AvailableBudgetArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_available_budgets(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list_available_budgets(
            code="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(AvailableBudgetArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_available_budgets(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list_available_budgets(
            code="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(AvailableBudgetArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_available_budgets(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.list_available_budgets(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_bills(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_bills(
            code="USD",
        )
        assert_matches_type(BillArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_bills_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_bills(
            code="USD",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BillArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_bills(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list_bills(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(BillArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_bills(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list_bills(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(BillArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_bills(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.list_bills(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_budget_limits(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_budget_limits(
            code="USD",
        )
        assert_matches_type(BudgetLimitArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_budget_limits_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_budget_limits(
            code="USD",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(BudgetLimitArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_budget_limits(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list_budget_limits(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(BudgetLimitArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_budget_limits(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list_budget_limits(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(BudgetLimitArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_budget_limits(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.list_budget_limits(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recurrences(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_recurrences(
            code="EUR",
        )
        assert_matches_type(RecurrenceArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recurrences_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_recurrences(
            code="EUR",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_recurrences(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list_recurrences(
            code="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(RecurrenceArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_recurrences(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list_recurrences(
            code="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(RecurrenceArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_recurrences(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.list_recurrences(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rules(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_rules(
            code="USD",
        )
        assert_matches_type(RuleArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rules_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_rules(
            code="USD",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_rules(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list_rules(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(RuleArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_rules(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list_rules(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(RuleArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_rules(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.list_rules(
                code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_transactions(
            code="USD",
        )
        assert_matches_type(TransactionArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncFirefly) -> None:
        currency = await async_client.currencies.list_transactions(
            code="USD",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        response = await async_client.currencies.with_raw_response.list_transactions(
            code="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(TransactionArray, currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        async with async_client.currencies.with_streaming_response.list_transactions(
            code="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(TransactionArray, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.currencies.with_raw_response.list_transactions(
                code="",
            )
