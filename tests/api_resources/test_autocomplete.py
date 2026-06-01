# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    AutocompleteListTagsResponse,
    AutocompleteListBillsResponse,
    AutocompleteListRulesResponse,
    AutocompleteListBudgetsResponse,
    AutocompleteListAccountsResponse,
    AutocompleteListCategoriesResponse,
    AutocompleteListCurrenciesResponse,
    AutocompleteListPiggyBanksResponse,
    AutocompleteListRuleGroupsResponse,
    AutocompleteListObjectGroupsResponse,
    AutocompleteListTransactionsResponse,
    AutocompleteListSubscriptionsResponse,
    AutocompleteListTransactionTypesResponse,
    AutocompleteListCurrenciesWithCodeResponse,
    AutocompleteListTransactionsWithIDResponse,
    AutocompleteListPiggyBanksWithBalanceResponse,
    AutocompleteListRecurringTransactionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutocomplete:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_accounts(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_accounts()
        assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_accounts_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_accounts(
            date="date",
            limit=0,
            query="query",
            types=["all"],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_accounts(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_accounts(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_bills(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_bills()
        assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_bills_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_bills(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_bills(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_bills()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_bills(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_bills() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_budgets(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_budgets()
        assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_budgets_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_budgets(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_budgets(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_budgets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_budgets(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_budgets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_categories(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_categories()
        assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_categories_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_categories(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_categories(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_categories(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_currencies(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_currencies()
        assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_currencies_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_currencies(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_currencies(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_currencies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_currencies(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_currencies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_currencies_with_code(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_currencies_with_code()
        assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_currencies_with_code_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_currencies_with_code(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_currencies_with_code(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_currencies_with_code()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_currencies_with_code(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_currencies_with_code() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_object_groups(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_object_groups()
        assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_object_groups_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_object_groups(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_object_groups(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_object_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_object_groups(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_object_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_banks(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_piggy_banks()
        assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_banks_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_piggy_banks(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_piggy_banks(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_piggy_banks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_piggy_banks(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_piggy_banks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_banks_with_balance(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_piggy_banks_with_balance()
        assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_banks_with_balance_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_piggy_banks_with_balance(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_piggy_banks_with_balance(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_piggy_banks_with_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_piggy_banks_with_balance(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_piggy_banks_with_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recurring_transactions(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_recurring_transactions()
        assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recurring_transactions_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_recurring_transactions(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_recurring_transactions(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_recurring_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_recurring_transactions(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_recurring_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rule_groups(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_rule_groups()
        assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rule_groups_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_rule_groups(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_rule_groups(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_rule_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_rule_groups(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_rule_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rules(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_rules()
        assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rules_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_rules(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_rules(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_rules()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_rules(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_rules() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscriptions(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_subscriptions()
        assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscriptions_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_subscriptions(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscriptions(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_tags(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_tags()
        assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_tags_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_tags(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_tags(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_tags(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transaction_types(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_transaction_types()
        assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transaction_types_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_transaction_types(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transaction_types(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_transaction_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transaction_types(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_transaction_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_transactions()
        assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_transactions(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_id(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_transactions_with_id()
        assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_id_with_all_params(self, client: EmceesProdTesting5) -> None:
        autocomplete = client.autocomplete.list_transactions_with_id(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions_with_id(self, client: EmceesProdTesting5) -> None:
        response = client.autocomplete.with_raw_response.list_transactions_with_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = response.parse()
        assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions_with_id(self, client: EmceesProdTesting5) -> None:
        with client.autocomplete.with_streaming_response.list_transactions_with_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = response.parse()
            assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutocomplete:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_accounts(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_accounts()
        assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_accounts_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_accounts(
            date="date",
            limit=0,
            query="query",
            types=["all"],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_accounts(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_accounts(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListAccountsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_bills(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_bills()
        assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_bills_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_bills(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_bills(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_bills()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_bills(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_bills() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListBillsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_budgets(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_budgets()
        assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_budgets_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_budgets(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_budgets(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_budgets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_budgets(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_budgets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListBudgetsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_categories(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_categories()
        assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_categories_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_categories(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_categories(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_categories(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListCategoriesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_currencies()
        assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_currencies_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_currencies(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_currencies()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_currencies() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListCurrenciesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_currencies_with_code(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_currencies_with_code()
        assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_currencies_with_code_with_all_params(
        self, async_client: AsyncEmceesProdTesting5
    ) -> None:
        autocomplete = await async_client.autocomplete.list_currencies_with_code(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_currencies_with_code(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_currencies_with_code()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_currencies_with_code(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_currencies_with_code() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListCurrenciesWithCodeResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_object_groups(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_object_groups()
        assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_object_groups_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_object_groups(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_object_groups(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_object_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_object_groups(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_object_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListObjectGroupsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_banks(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_piggy_banks()
        assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_banks_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_piggy_banks(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_piggy_banks(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_piggy_banks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_piggy_banks(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_piggy_banks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListPiggyBanksResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_banks_with_balance(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_piggy_banks_with_balance()
        assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_banks_with_balance_with_all_params(
        self, async_client: AsyncEmceesProdTesting5
    ) -> None:
        autocomplete = await async_client.autocomplete.list_piggy_banks_with_balance(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_piggy_banks_with_balance(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_piggy_banks_with_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_piggy_banks_with_balance(
        self, async_client: AsyncEmceesProdTesting5
    ) -> None:
        async with async_client.autocomplete.with_streaming_response.list_piggy_banks_with_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListPiggyBanksWithBalanceResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recurring_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_recurring_transactions()
        assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recurring_transactions_with_all_params(
        self, async_client: AsyncEmceesProdTesting5
    ) -> None:
        autocomplete = await async_client.autocomplete.list_recurring_transactions(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_recurring_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_recurring_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_recurring_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_recurring_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListRecurringTransactionsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rule_groups(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_rule_groups()
        assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rule_groups_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_rule_groups(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_rule_groups(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_rule_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_rule_groups(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_rule_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListRuleGroupsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_rules()
        assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rules_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_rules(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_rules()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_rules() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListRulesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_subscriptions()
        assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscriptions_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_subscriptions(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListSubscriptionsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_tags(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_tags()
        assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_tags_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_tags(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_tags(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_tags(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListTagsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transaction_types(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_transaction_types()
        assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transaction_types_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_transaction_types(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transaction_types(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_transaction_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transaction_types(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_transaction_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListTransactionTypesResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_transactions()
        assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_transactions(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListTransactionsResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_id(self, async_client: AsyncEmceesProdTesting5) -> None:
        autocomplete = await async_client.autocomplete.list_transactions_with_id()
        assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_id_with_all_params(
        self, async_client: AsyncEmceesProdTesting5
    ) -> None:
        autocomplete = await async_client.autocomplete.list_transactions_with_id(
            limit=0,
            query="query",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions_with_id(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.autocomplete.with_raw_response.list_transactions_with_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocomplete = await response.parse()
        assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions_with_id(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.autocomplete.with_streaming_response.list_transactions_with_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocomplete = await response.parse()
            assert_matches_type(AutocompleteListTransactionsWithIDResponse, autocomplete, path=["response"])

        assert cast(Any, response.is_closed) is True
