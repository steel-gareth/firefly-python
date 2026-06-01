# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types import (
    RecurrenceArray,
    RecurrenceSingle,
    TransactionArray,
)
from firefly._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecurrences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Firefly) -> None:
        recurrence = client.recurrences.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                }
            ],
            type="withdrawal",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Firefly) -> None:
        recurrence = client.recurrences.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                    "skip": 0,
                    "weekend": 1,
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                    "bill_id": "123",
                    "budget_id": "4",
                    "category_id": "211",
                    "currency_code": "EUR",
                    "currency_id": "3",
                    "foreign_amount": "123.45",
                    "foreign_currency_code": "GBP",
                    "foreign_currency_id": "17",
                    "piggy_bank_id": "123",
                    "tags": ["Barbecue preparation"],
                }
            ],
            type="withdrawal",
            active=True,
            apply_rules=True,
            description="Recurring transaction for the monthly rent",
            notes="Some notes",
            nr_of_repetitions=5,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Firefly) -> None:
        response = client.recurrences.with_raw_response.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                }
            ],
            type="withdrawal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = response.parse()
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Firefly) -> None:
        with client.recurrences.with_streaming_response.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                }
            ],
            type="withdrawal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = response.parse()
            assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        recurrence = client.recurrences.retrieve(
            id="123",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        recurrence = client.recurrences.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.recurrences.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = response.parse()
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.recurrences.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = response.parse()
            assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.recurrences.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Firefly) -> None:
        recurrence = client.recurrences.update(
            id="123",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Firefly) -> None:
        recurrence = client.recurrences.update(
            id="123",
            active=True,
            apply_rules=True,
            description="Recurring transaction for the monthly rent",
            first_date=parse_date("2026-04-30"),
            notes="Some notes",
            nr_of_repetitions=5,
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "skip": 0,
                    "type": "weekly",
                    "weekend": 1,
                }
            ],
            title="Rent",
            transactions=[
                {
                    "id": "ID of the recurring transaction. Not to be confused with the ID of the recurrence itself. Is marked as REQUIRED but can be skipped when there is only ONE transaction.",
                    "amount": "123.45",
                    "bill_id": "123",
                    "budget_id": "4",
                    "category_id": "211",
                    "currency_code": "EUR",
                    "currency_id": "3",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "foreign_amount": "123.45",
                    "foreign_currency_id": "17",
                    "piggy_bank_id": "123",
                    "source_id": "913",
                    "tags": ["Barbecue preparation"],
                }
            ],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Firefly) -> None:
        response = client.recurrences.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = response.parse()
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Firefly) -> None:
        with client.recurrences.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = response.parse()
            assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.recurrences.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Firefly) -> None:
        recurrence = client.recurrences.list()
        assert_matches_type(RecurrenceArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Firefly) -> None:
        recurrence = client.recurrences.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Firefly) -> None:
        response = client.recurrences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = response.parse()
        assert_matches_type(RecurrenceArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Firefly) -> None:
        with client.recurrences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = response.parse()
            assert_matches_type(RecurrenceArray, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Firefly) -> None:
        recurrence = client.recurrences.delete(
            id="123",
        )
        assert recurrence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Firefly) -> None:
        recurrence = client.recurrences.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert recurrence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Firefly) -> None:
        response = client.recurrences.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = response.parse()
        assert recurrence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Firefly) -> None:
        with client.recurrences.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = response.parse()
            assert recurrence is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.recurrences.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: Firefly) -> None:
        recurrence = client.recurrences.list_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: Firefly) -> None:
        recurrence = client.recurrences.list_transactions(
            id="123",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: Firefly) -> None:
        response = client.recurrences.with_raw_response.list_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = response.parse()
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: Firefly) -> None:
        with client.recurrences.with_streaming_response.list_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = response.parse()
            assert_matches_type(TransactionArray, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_transactions(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.recurrences.with_raw_response.list_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_transaction(self, client: Firefly) -> None:
        recurrence = client.recurrences.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_transaction_with_all_params(self, client: Firefly) -> None:
        recurrence = client.recurrences.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger_transaction(self, client: Firefly) -> None:
        response = client.recurrences.with_raw_response.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = response.parse()
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger_transaction(self, client: Firefly) -> None:
        with client.recurrences.with_streaming_response.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = response.parse()
            assert_matches_type(TransactionArray, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_trigger_transaction(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.recurrences.with_raw_response.trigger_transaction(
                id="",
                date=parse_date("2019-12-27"),
            )


class TestAsyncRecurrences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                }
            ],
            type="withdrawal",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                    "skip": 0,
                    "weekend": 1,
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                    "bill_id": "123",
                    "budget_id": "4",
                    "category_id": "211",
                    "currency_code": "EUR",
                    "currency_id": "3",
                    "foreign_amount": "123.45",
                    "foreign_currency_code": "GBP",
                    "foreign_currency_id": "17",
                    "piggy_bank_id": "123",
                    "tags": ["Barbecue preparation"],
                }
            ],
            type="withdrawal",
            active=True,
            apply_rules=True,
            description="Recurring transaction for the monthly rent",
            notes="Some notes",
            nr_of_repetitions=5,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFirefly) -> None:
        response = await async_client.recurrences.with_raw_response.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                }
            ],
            type="withdrawal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = await response.parse()
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFirefly) -> None:
        async with async_client.recurrences.with_streaming_response.create(
            first_date=parse_date("2026-04-30"),
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "type": "weekly",
                }
            ],
            title="Rent",
            transactions=[
                {
                    "amount": "123.45",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "source_id": "913",
                }
            ],
            type="withdrawal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = await response.parse()
            assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.retrieve(
            id="123",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.recurrences.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = await response.parse()
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.recurrences.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = await response.parse()
            assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.recurrences.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.update(
            id="123",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.update(
            id="123",
            active=True,
            apply_rules=True,
            description="Recurring transaction for the monthly rent",
            first_date=parse_date("2026-04-30"),
            notes="Some notes",
            nr_of_repetitions=5,
            repeat_until=parse_date("2026-04-30"),
            repetitions=[
                {
                    "moment": "3",
                    "skip": 0,
                    "type": "weekly",
                    "weekend": 1,
                }
            ],
            title="Rent",
            transactions=[
                {
                    "id": "ID of the recurring transaction. Not to be confused with the ID of the recurrence itself. Is marked as REQUIRED but can be skipped when there is only ONE transaction.",
                    "amount": "123.45",
                    "bill_id": "123",
                    "budget_id": "4",
                    "category_id": "211",
                    "currency_code": "EUR",
                    "currency_id": "3",
                    "description": "Rent for the current month",
                    "destination_id": "258",
                    "foreign_amount": "123.45",
                    "foreign_currency_id": "17",
                    "piggy_bank_id": "123",
                    "source_id": "913",
                    "tags": ["Barbecue preparation"],
                }
            ],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFirefly) -> None:
        response = await async_client.recurrences.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = await response.parse()
        assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFirefly) -> None:
        async with async_client.recurrences.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = await response.parse()
            assert_matches_type(RecurrenceSingle, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.recurrences.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.list()
        assert_matches_type(RecurrenceArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(RecurrenceArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFirefly) -> None:
        response = await async_client.recurrences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = await response.parse()
        assert_matches_type(RecurrenceArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFirefly) -> None:
        async with async_client.recurrences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = await response.parse()
            assert_matches_type(RecurrenceArray, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.delete(
            id="123",
        )
        assert recurrence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert recurrence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFirefly) -> None:
        response = await async_client.recurrences.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = await response.parse()
        assert recurrence is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFirefly) -> None:
        async with async_client.recurrences.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = await response.parse()
            assert recurrence is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.recurrences.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.list_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.list_transactions(
            id="123",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        response = await async_client.recurrences.with_raw_response.list_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = await response.parse()
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        async with async_client.recurrences.with_streaming_response.list_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = await response.parse()
            assert_matches_type(TransactionArray, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.recurrences.with_raw_response.list_transactions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_transaction(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_transaction_with_all_params(self, async_client: AsyncFirefly) -> None:
        recurrence = await async_client.recurrences.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger_transaction(self, async_client: AsyncFirefly) -> None:
        response = await async_client.recurrences.with_raw_response.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurrence = await response.parse()
        assert_matches_type(TransactionArray, recurrence, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_transaction(self, async_client: AsyncFirefly) -> None:
        async with async_client.recurrences.with_streaming_response.trigger_transaction(
            id="123",
            date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurrence = await response.parse()
            assert_matches_type(TransactionArray, recurrence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_trigger_transaction(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.recurrences.with_raw_response.trigger_transaction(
                id="",
                date=parse_date("2019-12-27"),
            )
