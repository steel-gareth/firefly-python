# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types import (
    AttachmentArray,
    TransactionArray,
    TransactionSingle,
    PiggyBankEventArray,
)
from firefly._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Firefly) -> None:
        transaction = client.transactions.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                }
            ],
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Firefly) -> None:
        transaction = client.transactions.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                    "bill_id": "112",
                    "bill_name": "Monthly rent",
                    "book_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "budget_id": "4",
                    "budget_name": "Groceries",
                    "category_id": "43",
                    "category_name": "Groceries",
                    "currency_code": "EUR",
                    "currency_id": "12",
                    "destination_id": "2",
                    "destination_name": "Buy and Large",
                    "due_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_id": "external_id",
                    "external_url": "external_url",
                    "foreign_amount": "123.45",
                    "foreign_currency_code": "USD",
                    "foreign_currency_id": "17",
                    "interest_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "internal_reference": "internal_reference",
                    "invoice_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "notes": "Some example notes",
                    "order": 0,
                    "payment_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "piggy_bank_id": 0,
                    "piggy_bank_name": "piggy_bank_name",
                    "process_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "reconciled": False,
                    "sepa_batch_id": "sepa_batch_id",
                    "sepa_cc": "sepa_cc",
                    "sepa_ci": "sepa_ci",
                    "sepa_country": "sepa_country",
                    "sepa_ct_id": "sepa_ct_id",
                    "sepa_ct_op": "sepa_ct_op",
                    "sepa_db": "sepa_db",
                    "sepa_ep": "sepa_ep",
                    "source_id": "2",
                    "source_name": "Checking account",
                    "tags": ["Barbecue preparation"],
                }
            ],
            apply_rules=False,
            error_if_duplicate_hash=False,
            fire_webhooks=True,
            group_title="Split transaction title.",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Firefly) -> None:
        response = client.transactions.with_raw_response.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Firefly) -> None:
        with client.transactions.with_streaming_response.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionSingle, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        transaction = client.transactions.retrieve(
            id="123",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        transaction = client.transactions.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.transactions.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.transactions.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionSingle, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transactions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Firefly) -> None:
        transaction = client.transactions.update(
            id="123",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Firefly) -> None:
        transaction = client.transactions.update(
            id="123",
            apply_rules=False,
            fire_webhooks=True,
            group_title="Split transaction title.",
            transactions=[
                {
                    "amount": "123.45",
                    "bill_id": "111",
                    "bill_name": "Monthly rent",
                    "book_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "budget_id": "4",
                    "category_id": "43",
                    "category_name": "Groceries",
                    "currency_code": "EUR",
                    "currency_id": "12",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "destination_iban": "NL02ABNA0123456789",
                    "destination_id": "2",
                    "destination_name": "Buy and Large",
                    "due_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_id": "external_id",
                    "external_url": "external_url",
                    "foreign_amount": "123.45",
                    "foreign_currency_code": "USD",
                    "foreign_currency_id": "17",
                    "interest_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "internal_reference": "internal_reference",
                    "invoice_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "notes": "Some example notes",
                    "order": 0,
                    "payment_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "process_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "reconciled": False,
                    "sepa_batch_id": "sepa_batch_id",
                    "sepa_cc": "sepa_cc",
                    "sepa_ci": "sepa_ci",
                    "sepa_country": "sepa_country",
                    "sepa_ct_id": "sepa_ct_id",
                    "sepa_ct_op": "sepa_ct_op",
                    "sepa_db": "sepa_db",
                    "sepa_ep": "sepa_ep",
                    "source_iban": "NL02ABNA0123456789",
                    "source_id": "2",
                    "source_name": "Checking account",
                    "tags": ["Barbecue preparation"],
                    "transaction_journal_id": "123",
                    "type": "withdrawal",
                }
            ],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Firefly) -> None:
        response = client.transactions.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Firefly) -> None:
        with client.transactions.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionSingle, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transactions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Firefly) -> None:
        transaction = client.transactions.list()
        assert_matches_type(TransactionArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Firefly) -> None:
        transaction = client.transactions.list(
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Firefly) -> None:
        response = client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Firefly) -> None:
        with client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionArray, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Firefly) -> None:
        transaction = client.transactions.delete(
            id="123",
        )
        assert transaction is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Firefly) -> None:
        transaction = client.transactions.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert transaction is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Firefly) -> None:
        response = client.transactions.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Firefly) -> None:
        with client.transactions.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transactions.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments(self, client: Firefly) -> None:
        transaction = client.transactions.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments_with_all_params(self, client: Firefly) -> None:
        transaction = client.transactions.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_attachments(self, client: Firefly) -> None:
        response = client.transactions.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(AttachmentArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_attachments(self, client: Firefly) -> None:
        with client.transactions.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(AttachmentArray, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_attachments(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transactions.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_bank_events(self, client: Firefly) -> None:
        transaction = client.transactions.list_piggy_bank_events(
            id="123",
        )
        assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_bank_events_with_all_params(self, client: Firefly) -> None:
        transaction = client.transactions.list_piggy_bank_events(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_piggy_bank_events(self, client: Firefly) -> None:
        response = client.transactions.with_raw_response.list_piggy_bank_events(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_piggy_bank_events(self, client: Firefly) -> None:
        with client.transactions.with_streaming_response.list_piggy_bank_events(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_piggy_bank_events(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transactions.with_raw_response.list_piggy_bank_events(
                id="",
            )


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                }
            ],
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                    "bill_id": "112",
                    "bill_name": "Monthly rent",
                    "book_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "budget_id": "4",
                    "budget_name": "Groceries",
                    "category_id": "43",
                    "category_name": "Groceries",
                    "currency_code": "EUR",
                    "currency_id": "12",
                    "destination_id": "2",
                    "destination_name": "Buy and Large",
                    "due_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_id": "external_id",
                    "external_url": "external_url",
                    "foreign_amount": "123.45",
                    "foreign_currency_code": "USD",
                    "foreign_currency_id": "17",
                    "interest_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "internal_reference": "internal_reference",
                    "invoice_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "notes": "Some example notes",
                    "order": 0,
                    "payment_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "piggy_bank_id": 0,
                    "piggy_bank_name": "piggy_bank_name",
                    "process_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "reconciled": False,
                    "sepa_batch_id": "sepa_batch_id",
                    "sepa_cc": "sepa_cc",
                    "sepa_ci": "sepa_ci",
                    "sepa_country": "sepa_country",
                    "sepa_ct_id": "sepa_ct_id",
                    "sepa_ct_op": "sepa_ct_op",
                    "sepa_db": "sepa_db",
                    "sepa_ep": "sepa_ep",
                    "source_id": "2",
                    "source_name": "Checking account",
                    "tags": ["Barbecue preparation"],
                }
            ],
            apply_rules=False,
            error_if_duplicate_hash=False,
            fire_webhooks=True,
            group_title="Split transaction title.",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFirefly) -> None:
        response = await async_client.transactions.with_raw_response.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFirefly) -> None:
        async with async_client.transactions.with_streaming_response.create(
            transactions=[
                {
                    "amount": "123.45",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "type": "withdrawal",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionSingle, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.retrieve(
            id="123",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.transactions.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.transactions.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionSingle, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transactions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.update(
            id="123",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.update(
            id="123",
            apply_rules=False,
            fire_webhooks=True,
            group_title="Split transaction title.",
            transactions=[
                {
                    "amount": "123.45",
                    "bill_id": "111",
                    "bill_name": "Monthly rent",
                    "book_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "budget_id": "4",
                    "category_id": "43",
                    "category_name": "Groceries",
                    "currency_code": "EUR",
                    "currency_id": "12",
                    "date": parse_datetime("2026-04-01T00:00:00+00:00"),
                    "description": "Vegetables",
                    "destination_iban": "NL02ABNA0123456789",
                    "destination_id": "2",
                    "destination_name": "Buy and Large",
                    "due_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "external_id": "external_id",
                    "external_url": "external_url",
                    "foreign_amount": "123.45",
                    "foreign_currency_code": "USD",
                    "foreign_currency_id": "17",
                    "interest_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "internal_reference": "internal_reference",
                    "invoice_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "notes": "Some example notes",
                    "order": 0,
                    "payment_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "process_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "reconciled": False,
                    "sepa_batch_id": "sepa_batch_id",
                    "sepa_cc": "sepa_cc",
                    "sepa_ci": "sepa_ci",
                    "sepa_country": "sepa_country",
                    "sepa_ct_id": "sepa_ct_id",
                    "sepa_ct_op": "sepa_ct_op",
                    "sepa_db": "sepa_db",
                    "sepa_ep": "sepa_ep",
                    "source_iban": "NL02ABNA0123456789",
                    "source_id": "2",
                    "source_name": "Checking account",
                    "tags": ["Barbecue preparation"],
                    "transaction_journal_id": "123",
                    "type": "withdrawal",
                }
            ],
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFirefly) -> None:
        response = await async_client.transactions.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionSingle, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFirefly) -> None:
        async with async_client.transactions.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionSingle, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transactions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.list()
        assert_matches_type(TransactionArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.list(
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFirefly) -> None:
        response = await async_client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFirefly) -> None:
        async with async_client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionArray, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.delete(
            id="123",
        )
        assert transaction is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert transaction is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFirefly) -> None:
        response = await async_client.transactions.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFirefly) -> None:
        async with async_client.transactions.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transactions.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments_with_all_params(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_attachments(self, async_client: AsyncFirefly) -> None:
        response = await async_client.transactions.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(AttachmentArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_attachments(self, async_client: AsyncFirefly) -> None:
        async with async_client.transactions.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(AttachmentArray, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_attachments(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transactions.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_bank_events(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.list_piggy_bank_events(
            id="123",
        )
        assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_bank_events_with_all_params(self, async_client: AsyncFirefly) -> None:
        transaction = await async_client.transactions.list_piggy_bank_events(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_piggy_bank_events(self, async_client: AsyncFirefly) -> None:
        response = await async_client.transactions.with_raw_response.list_piggy_bank_events(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_piggy_bank_events(self, async_client: AsyncFirefly) -> None:
        async with async_client.transactions.with_streaming_response.list_piggy_bank_events(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(PiggyBankEventArray, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_piggy_bank_events(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transactions.with_raw_response.list_piggy_bank_events(
                id="",
            )
