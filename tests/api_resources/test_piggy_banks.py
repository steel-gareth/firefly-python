# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types import (
    PiggyBankArray,
    AttachmentArray,
    PiggyBankSingle,
    PiggyBankEventArray,
)
from firefly._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPiggyBanks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
            accounts=[
                {
                    "id": "3",
                    "current_amount": "123.45",
                    "name": "Checking account",
                }
            ],
            current_amount="123.45",
            notes="Some notes",
            object_group_id="5",
            object_group_title="Example Group",
            order=5,
            target_date=parse_date("2026-04-30"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Firefly) -> None:
        response = client.piggy_banks.with_raw_response.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = response.parse()
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Firefly) -> None:
        with client.piggy_banks.with_streaming_response.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = response.parse()
            assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.retrieve(
            id="123",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.piggy_banks.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = response.parse()
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.piggy_banks.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = response.parse()
            assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.piggy_banks.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.update(
            id="123",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.update(
            id="123",
            accounts=[
                {
                    "id": {},
                    "account_id": "3",
                    "current_amount": "123.45",
                    "name": "Checking account",
                }
            ],
            name="New digital camera",
            notes="Some notes",
            object_group_id="5",
            object_group_title="Example Group",
            order=5,
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
            target_date=parse_date("2026-04-30"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Firefly) -> None:
        response = client.piggy_banks.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = response.parse()
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Firefly) -> None:
        with client.piggy_banks.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = response.parse()
            assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.piggy_banks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.list()
        assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Firefly) -> None:
        response = client.piggy_banks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = response.parse()
        assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Firefly) -> None:
        with client.piggy_banks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = response.parse()
            assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.delete(
            id="123",
        )
        assert piggy_bank is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert piggy_bank is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Firefly) -> None:
        response = client.piggy_banks.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = response.parse()
        assert piggy_bank is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Firefly) -> None:
        with client.piggy_banks.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = response.parse()
            assert piggy_bank is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.piggy_banks.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments_with_all_params(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_attachments(self, client: Firefly) -> None:
        response = client.piggy_banks.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = response.parse()
        assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_attachments(self, client: Firefly) -> None:
        with client.piggy_banks.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = response.parse()
            assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_attachments(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.piggy_banks.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.list_events(
            id="123",
        )
        assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: Firefly) -> None:
        piggy_bank = client.piggy_banks.list_events(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: Firefly) -> None:
        response = client.piggy_banks.with_raw_response.list_events(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = response.parse()
        assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: Firefly) -> None:
        with client.piggy_banks.with_streaming_response.list_events(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = response.parse()
            assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_events(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.piggy_banks.with_raw_response.list_events(
                id="",
            )


class TestAsyncPiggyBanks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
            accounts=[
                {
                    "id": "3",
                    "current_amount": "123.45",
                    "name": "Checking account",
                }
            ],
            current_amount="123.45",
            notes="Some notes",
            object_group_id="5",
            object_group_title="Example Group",
            order=5,
            target_date=parse_date("2026-04-30"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFirefly) -> None:
        response = await async_client.piggy_banks.with_raw_response.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = await response.parse()
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFirefly) -> None:
        async with async_client.piggy_banks.with_streaming_response.create(
            account_id={},
            name="New digital camera",
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = await response.parse()
            assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.retrieve(
            id="123",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.piggy_banks.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = await response.parse()
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.piggy_banks.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = await response.parse()
            assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.piggy_banks.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.update(
            id="123",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.update(
            id="123",
            accounts=[
                {
                    "id": {},
                    "account_id": "3",
                    "current_amount": "123.45",
                    "name": "Checking account",
                }
            ],
            name="New digital camera",
            notes="Some notes",
            object_group_id="5",
            object_group_title="Example Group",
            order=5,
            start_date=parse_date("2026-04-01"),
            target_amount="123.45",
            target_date=parse_date("2026-04-30"),
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFirefly) -> None:
        response = await async_client.piggy_banks.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = await response.parse()
        assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFirefly) -> None:
        async with async_client.piggy_banks.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = await response.parse()
            assert_matches_type(PiggyBankSingle, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.piggy_banks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.list()
        assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFirefly) -> None:
        response = await async_client.piggy_banks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = await response.parse()
        assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFirefly) -> None:
        async with async_client.piggy_banks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = await response.parse()
            assert_matches_type(PiggyBankArray, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.delete(
            id="123",
        )
        assert piggy_bank is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert piggy_bank is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFirefly) -> None:
        response = await async_client.piggy_banks.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = await response.parse()
        assert piggy_bank is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFirefly) -> None:
        async with async_client.piggy_banks.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = await response.parse()
            assert piggy_bank is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.piggy_banks.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.list_attachments(
            id="123",
        )
        assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments_with_all_params(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.list_attachments(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_attachments(self, async_client: AsyncFirefly) -> None:
        response = await async_client.piggy_banks.with_raw_response.list_attachments(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = await response.parse()
        assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_attachments(self, async_client: AsyncFirefly) -> None:
        async with async_client.piggy_banks.with_streaming_response.list_attachments(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = await response.parse()
            assert_matches_type(AttachmentArray, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_attachments(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.piggy_banks.with_raw_response.list_attachments(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.list_events(
            id="123",
        )
        assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncFirefly) -> None:
        piggy_bank = await async_client.piggy_banks.list_events(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncFirefly) -> None:
        response = await async_client.piggy_banks.with_raw_response.list_events(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        piggy_bank = await response.parse()
        assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncFirefly) -> None:
        async with async_client.piggy_banks.with_streaming_response.list_events(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            piggy_bank = await response.parse()
            assert_matches_type(PiggyBankEventArray, piggy_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.piggy_banks.with_raw_response.list_events(
                id="",
            )
