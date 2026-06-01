# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    AccountArray,
    AccountSingle,
    PiggyBankArray,
    AttachmentArray,
    TransactionArray,
)
from emcees_prod_testing_5._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.create(
            name="My checking account",
            type="asset",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.create(
            name="My checking account",
            type="asset",
            account_number="7009312345678",
            account_role="defaultAsset",
            active=False,
            bic="BOFAUS3N",
            credit_card_type="monthlyFull",
            currency_code="EUR",
            currency_id="12",
            iban="GB98MIDL07009312345678",
            include_net_worth=True,
            interest="5.3",
            interest_period="monthly",
            latitude=51.983333,
            liability_direction="credit",
            liability_type="loan",
            longitude=5.916667,
            monthly_payment_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            notes="Some example notes",
            opening_balance="-1012.12",
            opening_balance_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            order=1,
            virtual_balance="123.45",
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.create(
            name="My checking account",
            type="asset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.create(
            name="My checking account",
            type="asset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountSingle, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.retrieve(
            id="123",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.retrieve(
            id="123",
            date=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountSingle, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.update(
            id="123",
            name="My checking account",
            type={},
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.update(
            id="123",
            name="My checking account",
            type={},
            account_number="7009312345678",
            account_role="defaultAsset",
            active=False,
            bic="BOFAUS3N",
            credit_card_type="monthlyFull",
            currency_code="EUR",
            currency_id="12",
            iban="GB98MIDL07009312345678",
            include_net_worth=True,
            interest="5.3",
            interest_period="monthly",
            latitude=51.983333,
            liability_type="loan",
            longitude=5.916667,
            monthly_payment_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            notes="Some example notes",
            opening_balance="-1012.12",
            opening_balance_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            order=1,
            virtual_balance="123.45",
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.update(
            id="123",
            name="My checking account",
            type={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.update(
            id="123",
            name="My checking account",
            type={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountSingle, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.with_raw_response.update(
                id="",
                name="My checking account",
                type={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list()
        assert_matches_type(AccountArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list(
            date=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            limit=10,
            page=1,
            start=parse_date("2019-12-27"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.delete(
            id="123",
        )
        assert account is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert account is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert account is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_attachments(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AttachmentArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_attachments(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AttachmentArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_attachments(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_banks(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list_piggy_banks(
            id="123",
        )
        assert_matches_type(PiggyBankArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_piggy_banks_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list_piggy_banks(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_piggy_banks(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.list_piggy_banks(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(PiggyBankArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_piggy_banks(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.list_piggy_banks(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(PiggyBankArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_piggy_banks(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.with_raw_response.list_piggy_banks(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: EmceesProdTesting5) -> None:
        account = client.accounts.list_transactions(
            id="123",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: EmceesProdTesting5) -> None:
        response = client.accounts.with_raw_response.list_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(TransactionArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: EmceesProdTesting5) -> None:
        with client.accounts.with_streaming_response.list_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(TransactionArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_transactions(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.with_raw_response.list_transactions(
                id="",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.create(
            name="My checking account",
            type="asset",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.create(
            name="My checking account",
            type="asset",
            account_number="7009312345678",
            account_role="defaultAsset",
            active=False,
            bic="BOFAUS3N",
            credit_card_type="monthlyFull",
            currency_code="EUR",
            currency_id="12",
            iban="GB98MIDL07009312345678",
            include_net_worth=True,
            interest="5.3",
            interest_period="monthly",
            latitude=51.983333,
            liability_direction="credit",
            liability_type="loan",
            longitude=5.916667,
            monthly_payment_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            notes="Some example notes",
            opening_balance="-1012.12",
            opening_balance_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            order=1,
            virtual_balance="123.45",
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.create(
            name="My checking account",
            type="asset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.create(
            name="My checking account",
            type="asset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountSingle, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.retrieve(
            id="123",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.retrieve(
            id="123",
            date=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountSingle, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.update(
            id="123",
            name="My checking account",
            type={},
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.update(
            id="123",
            name="My checking account",
            type={},
            account_number="7009312345678",
            account_role="defaultAsset",
            active=False,
            bic="BOFAUS3N",
            credit_card_type="monthlyFull",
            currency_code="EUR",
            currency_id="12",
            iban="GB98MIDL07009312345678",
            include_net_worth=True,
            interest="5.3",
            interest_period="monthly",
            latitude=51.983333,
            liability_type="loan",
            longitude=5.916667,
            monthly_payment_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            notes="Some example notes",
            opening_balance="-1012.12",
            opening_balance_date=parse_datetime("2026-04-01T00:00:00+00:00"),
            order=1,
            virtual_balance="123.45",
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.update(
            id="123",
            name="My checking account",
            type={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountSingle, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.update(
            id="123",
            name="My checking account",
            type={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountSingle, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.with_raw_response.update(
                id="",
                name="My checking account",
                type={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AccountArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list(
            date=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            limit=10,
            page=1,
            start=parse_date("2019-12-27"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AccountArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.delete(
            id="123",
        )
        assert account is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert account is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert account is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AttachmentArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AttachmentArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_attachments(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_banks(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list_piggy_banks(
            id="123",
        )
        assert_matches_type(PiggyBankArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_piggy_banks_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list_piggy_banks(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_piggy_banks(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.list_piggy_banks(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(PiggyBankArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_piggy_banks(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.list_piggy_banks(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(PiggyBankArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_piggy_banks(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.with_raw_response.list_piggy_banks(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list_transactions(
            id="123",
        )
        assert_matches_type(TransactionArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        account = await async_client.accounts.list_transactions(
            id="123",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.accounts.with_raw_response.list_transactions(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(TransactionArray, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.accounts.with_streaming_response.list_transactions(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(TransactionArray, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.with_raw_response.list_transactions(
                id="",
            )
