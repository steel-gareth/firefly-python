# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    RuleArray,
    RuleSingle,
    TransactionArray,
)
from emcees_prod_testing_5._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                    "active": True,
                    "order": 5,
                    "stop_processing": False,
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                    "active": True,
                    "order": 5,
                    "prohibited": False,
                    "stop_processing": False,
                }
            ],
            active=True,
            description="First rule description",
            order=5,
            rule_group_title="New rule group",
            stop_processing=False,
            strict=True,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: EmceesProdTesting5) -> None:
        response = client.rules.with_raw_response.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: EmceesProdTesting5) -> None:
        with client.rules.with_streaming_response.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleSingle, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.retrieve(
            id="123",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.rules.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.rules.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleSingle, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rules.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.update(
            id="123",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.update(
            id="123",
            actions=[
                {
                    "active": True,
                    "order": 5,
                    "stop_processing": False,
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            active=True,
            description="First rule description",
            order=5,
            rule_group_id="81",
            stop_processing=False,
            strict=True,
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "active": True,
                    "order": 5,
                    "stop_processing": False,
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: EmceesProdTesting5) -> None:
        response = client.rules.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: EmceesProdTesting5) -> None:
        with client.rules.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleSingle, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rules.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.list()
        assert_matches_type(RuleArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: EmceesProdTesting5) -> None:
        response = client.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: EmceesProdTesting5) -> None:
        with client.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleArray, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.delete(
            id="123",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: EmceesProdTesting5) -> None:
        response = client.rules.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: EmceesProdTesting5) -> None:
        with client.rules.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rules.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.test(
            id="123",
        )
        assert_matches_type(TransactionArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.test(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: EmceesProdTesting5) -> None:
        response = client.rules.with_raw_response.test(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(TransactionArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: EmceesProdTesting5) -> None:
        with client.rules.with_streaming_response.test(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(TransactionArray, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rules.with_raw_response.test(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.trigger(
            id="123",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_with_all_params(self, client: EmceesProdTesting5) -> None:
        rule = client.rules.trigger(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger(self, client: EmceesProdTesting5) -> None:
        response = client.rules.with_raw_response.trigger(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger(self, client: EmceesProdTesting5) -> None:
        with client.rules.with_streaming_response.trigger(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_trigger(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rules.with_raw_response.trigger(
                id="",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                    "active": True,
                    "order": 5,
                    "stop_processing": False,
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                    "active": True,
                    "order": 5,
                    "prohibited": False,
                    "stop_processing": False,
                }
            ],
            active=True,
            description="First rule description",
            order=5,
            rule_group_title="New rule group",
            stop_processing=False,
            strict=True,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rules.with_raw_response.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rules.with_streaming_response.create(
            actions=[
                {
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            rule_group_id="81",
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleSingle, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.retrieve(
            id="123",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rules.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rules.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleSingle, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rules.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.update(
            id="123",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.update(
            id="123",
            actions=[
                {
                    "active": True,
                    "order": 5,
                    "stop_processing": False,
                    "type": "set_category",
                    "value": "Daily groceries",
                }
            ],
            active=True,
            description="First rule description",
            order=5,
            rule_group_id="81",
            stop_processing=False,
            strict=True,
            title="First rule title.",
            trigger="store-journal",
            triggers=[
                {
                    "active": True,
                    "order": 5,
                    "stop_processing": False,
                    "type": "from_account_starts",
                    "value": "tag1",
                }
            ],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rules.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleSingle, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rules.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleSingle, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rules.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.list()
        assert_matches_type(RuleArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RuleArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleArray, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.delete(
            id="123",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rules.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rules.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rules.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.test(
            id="123",
        )
        assert_matches_type(TransactionArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.test(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rules.with_raw_response.test(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(TransactionArray, rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rules.with_streaming_response.test(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(TransactionArray, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rules.with_raw_response.test(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.trigger(
            id="123",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        rule = await async_client.rules.trigger(
            id="123",
            accounts=[1, 2, 3],
            end=parse_date("2026-04-30"),
            start=parse_date("2026-04-01"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.rules.with_raw_response.trigger(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.rules.with_streaming_response.trigger(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rules.with_raw_response.trigger(
                id="",
            )
