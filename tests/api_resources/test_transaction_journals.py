# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import TransactionSingle, TransactionLinkArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactionJournals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        transaction_journal = client.transaction_journals.retrieve(
            id="123",
        )
        assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        transaction_journal = client.transaction_journals.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.transaction_journals.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_journal = response.parse()
        assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.transaction_journals.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_journal = response.parse()
            assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transaction_journals.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: EmceesProdTesting5) -> None:
        transaction_journal = client.transaction_journals.delete(
            id="123",
        )
        assert transaction_journal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: EmceesProdTesting5) -> None:
        transaction_journal = client.transaction_journals.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert transaction_journal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: EmceesProdTesting5) -> None:
        response = client.transaction_journals.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_journal = response.parse()
        assert transaction_journal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: EmceesProdTesting5) -> None:
        with client.transaction_journals.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_journal = response.parse()
            assert transaction_journal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transaction_journals.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_links(self, client: EmceesProdTesting5) -> None:
        transaction_journal = client.transaction_journals.list_links(
            id="123",
        )
        assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_links_with_all_params(self, client: EmceesProdTesting5) -> None:
        transaction_journal = client.transaction_journals.list_links(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_links(self, client: EmceesProdTesting5) -> None:
        response = client.transaction_journals.with_raw_response.list_links(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_journal = response.parse()
        assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_links(self, client: EmceesProdTesting5) -> None:
        with client.transaction_journals.with_streaming_response.list_links(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_journal = response.parse()
            assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_links(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transaction_journals.with_raw_response.list_links(
                id="",
            )


class TestAsyncTransactionJournals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        transaction_journal = await async_client.transaction_journals.retrieve(
            id="123",
        )
        assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        transaction_journal = await async_client.transaction_journals.retrieve(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.transaction_journals.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_journal = await response.parse()
        assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.transaction_journals.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_journal = await response.parse()
            assert_matches_type(TransactionSingle, transaction_journal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transaction_journals.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        transaction_journal = await async_client.transaction_journals.delete(
            id="123",
        )
        assert transaction_journal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        transaction_journal = await async_client.transaction_journals.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert transaction_journal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.transaction_journals.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_journal = await response.parse()
        assert transaction_journal is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.transaction_journals.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_journal = await response.parse()
            assert transaction_journal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transaction_journals.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_links(self, async_client: AsyncEmceesProdTesting5) -> None:
        transaction_journal = await async_client.transaction_journals.list_links(
            id="123",
        )
        assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_links_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        transaction_journal = await async_client.transaction_journals.list_links(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_links(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.transaction_journals.with_raw_response.list_links(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction_journal = await response.parse()
        assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_links(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.transaction_journals.with_streaming_response.list_links(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction_journal = await response.parse()
            assert_matches_type(TransactionLinkArray, transaction_journal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_links(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transaction_journals.with_raw_response.list_links(
                id="",
            )
