# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    RuleArray,
    RuleGroupSingle,
    TransactionArray,
    RuleGroupListAllResponse,
)
from emcees_prod_testing_5._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuleGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.create(
            title="Default rule group",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.create(
            title="Default rule group",
            active=True,
            description="Description of this rule group",
            order=4,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.create(
            title="Default rule group",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.create(
            title="Default rule group",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.retrieve(
            id="123",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rule_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.update(
            id="123",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.update(
            id="123",
            active=True,
            description="Description of this rule group",
            order=4,
            title="Default rule group",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rule_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.delete(
            id="123",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert rule_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rule_groups.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.list_all()
        assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.list_all(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_all(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.list_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_all(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.list_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rules(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.list_rules(
            id="123",
        )
        assert_matches_type(RuleArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_rules_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.list_rules(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_rules(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.list_rules(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert_matches_type(RuleArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_rules(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.list_rules(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert_matches_type(RuleArray, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_rules(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rule_groups.with_raw_response.list_rules(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_transactions(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.test_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_transactions_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.test_transactions(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            search_limit=0,
            start=parse_date("2026-04-01"),
            triggered_limit=0,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test_transactions(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.test_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert_matches_type(TransactionArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test_transactions(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.test_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert_matches_type(TransactionArray, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test_transactions(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rule_groups.with_raw_response.test_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_rules(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.trigger_rules(
            id="123",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_rules_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule_group = client.rule_groups.trigger_rules(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger_rules(self, client: EmceesProdTesting5) -> None:
        response = client.rule_groups.with_raw_response.trigger_rules(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = response.parse()
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger_rules(self, client: EmceesProdTesting5) -> None:
        with client.rule_groups.with_streaming_response.trigger_rules(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = response.parse()
            assert rule_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_trigger_rules(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rule_groups.with_raw_response.trigger_rules(
                id="",
            )


class TestAsyncRuleGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.create(
            title="Default rule group",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.create(
            title="Default rule group",
            active=True,
            description="Description of this rule group",
            order=4,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.create(
            title="Default rule group",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.create(
            title="Default rule group",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.retrieve(
            id="123",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rule_groups.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.update(
            id="123",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.update(
            id="123",
            active=True,
            description="Description of this rule group",
            order=4,
            title="Default rule group",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert_matches_type(RuleGroupSingle, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rule_groups.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.delete(
            id="123",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert rule_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rule_groups.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.list_all()
        assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.list_all(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_all(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.list_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_all(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.list_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert_matches_type(RuleGroupListAllResponse, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.list_rules(
            id="123",
        )
        assert_matches_type(RuleArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_rules_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.list_rules(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.list_rules(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert_matches_type(RuleArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.list_rules(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert_matches_type(RuleArray, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rule_groups.with_raw_response.list_rules(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.test_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_transactions_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.test_transactions(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            search_limit=0,
            start=parse_date("2026-04-01"),
            triggered_limit=0,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.test_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert_matches_type(TransactionArray, rule_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.test_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert_matches_type(TransactionArray, rule_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rule_groups.with_raw_response.test_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.trigger_rules(
            id="123",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_rules_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule_group = await async_client.rule_groups.trigger_rules(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rule_groups.with_raw_response.trigger_rules(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule_group = await response.parse()
        assert rule_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rule_groups.with_streaming_response.trigger_rules(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule_group = await response.parse()
            assert rule_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_trigger_rules(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rule_groups.with_raw_response.trigger_rules(
                id="",
            )
