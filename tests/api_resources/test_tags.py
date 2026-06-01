# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from firefly import Firefly, AsyncFirefly
from tests.utils import assert_matches_type
from firefly.types import (
    TagSingle,
    AttachmentArray,
    TagListResponse,
    TransactionArray,
)
from firefly._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Firefly) -> None:
        tag = client.tags.create(
            tag="expensive",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Firefly) -> None:
        tag = client.tags.create(
            tag="expensive",
            date=parse_date("2026-04-01"),
            description="Tag for expensive stuff",
            latitude=51.983333,
            longitude=5.916667,
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Firefly) -> None:
        response = client.tags.with_raw_response.create(
            tag="expensive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Firefly) -> None:
        with client.tags.with_streaming_response.create(
            tag="expensive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagSingle, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Firefly) -> None:
        tag = client.tags.retrieve(
            tag="groceries",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Firefly) -> None:
        tag = client.tags.retrieve(
            tag="groceries",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Firefly) -> None:
        response = client.tags.with_raw_response.retrieve(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Firefly) -> None:
        with client.tags.with_streaming_response.retrieve(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagSingle, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            client.tags.with_raw_response.retrieve(
                tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Firefly) -> None:
        tag = client.tags.update(
            path_tag="groceries",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Firefly) -> None:
        tag = client.tags.update(
            path_tag="groceries",
            date=parse_date("2026-04-01"),
            description="Tag for expensive stuff",
            latitude=51.983333,
            longitude=5.916667,
            body_tag="expensive",
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Firefly) -> None:
        response = client.tags.with_raw_response.update(
            path_tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Firefly) -> None:
        with client.tags.with_streaming_response.update(
            path_tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagSingle, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_tag` but received ''"):
            client.tags.with_raw_response.update(
                path_tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Firefly) -> None:
        tag = client.tags.list()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Firefly) -> None:
        tag = client.tags.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Firefly) -> None:
        response = client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Firefly) -> None:
        with client.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Firefly) -> None:
        tag = client.tags.delete(
            tag="groceries",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Firefly) -> None:
        tag = client.tags.delete(
            tag="groceries",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Firefly) -> None:
        response = client.tags.with_raw_response.delete(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Firefly) -> None:
        with client.tags.with_streaming_response.delete(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            client.tags.with_raw_response.delete(
                tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments(self, client: Firefly) -> None:
        tag = client.tags.list_attachments(
            tag="groceries",
        )
        assert_matches_type(AttachmentArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attachments_with_all_params(self, client: Firefly) -> None:
        tag = client.tags.list_attachments(
            tag="groceries",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_attachments(self, client: Firefly) -> None:
        response = client.tags.with_raw_response.list_attachments(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(AttachmentArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_attachments(self, client: Firefly) -> None:
        with client.tags.with_streaming_response.list_attachments(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(AttachmentArray, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_attachments(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            client.tags.with_raw_response.list_attachments(
                tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: Firefly) -> None:
        tag = client.tags.list_transactions(
            tag="groceries",
        )
        assert_matches_type(TransactionArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: Firefly) -> None:
        tag = client.tags.list_transactions(
            tag="groceries",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: Firefly) -> None:
        response = client.tags.with_raw_response.list_transactions(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TransactionArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: Firefly) -> None:
        with client.tags.with_streaming_response.list_transactions(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TransactionArray, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_transactions(self, client: Firefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            client.tags.with_raw_response.list_transactions(
                tag="",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.create(
            tag="expensive",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.create(
            tag="expensive",
            date=parse_date("2026-04-01"),
            description="Tag for expensive stuff",
            latitude=51.983333,
            longitude=5.916667,
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncFirefly) -> None:
        response = await async_client.tags.with_raw_response.create(
            tag="expensive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncFirefly) -> None:
        async with async_client.tags.with_streaming_response.create(
            tag="expensive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagSingle, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.retrieve(
            tag="groceries",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.retrieve(
            tag="groceries",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncFirefly) -> None:
        response = await async_client.tags.with_raw_response.retrieve(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncFirefly) -> None:
        async with async_client.tags.with_streaming_response.retrieve(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagSingle, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            await async_client.tags.with_raw_response.retrieve(
                tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.update(
            path_tag="groceries",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.update(
            path_tag="groceries",
            date=parse_date("2026-04-01"),
            description="Tag for expensive stuff",
            latitude=51.983333,
            longitude=5.916667,
            body_tag="expensive",
            zoom_level=6,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncFirefly) -> None:
        response = await async_client.tags.with_raw_response.update(
            path_tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagSingle, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncFirefly) -> None:
        async with async_client.tags.with_streaming_response.update(
            path_tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagSingle, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_tag` but received ''"):
            await async_client.tags.with_raw_response.update(
                path_tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.list()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncFirefly) -> None:
        response = await async_client.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncFirefly) -> None:
        async with async_client.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.delete(
            tag="groceries",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.delete(
            tag="groceries",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncFirefly) -> None:
        response = await async_client.tags.with_raw_response.delete(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncFirefly) -> None:
        async with async_client.tags.with_streaming_response.delete(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            await async_client.tags.with_raw_response.delete(
                tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.list_attachments(
            tag="groceries",
        )
        assert_matches_type(AttachmentArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attachments_with_all_params(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.list_attachments(
            tag="groceries",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(AttachmentArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_attachments(self, async_client: AsyncFirefly) -> None:
        response = await async_client.tags.with_raw_response.list_attachments(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(AttachmentArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_attachments(self, async_client: AsyncFirefly) -> None:
        async with async_client.tags.with_streaming_response.list_attachments(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(AttachmentArray, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_attachments(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            await async_client.tags.with_raw_response.list_attachments(
                tag="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.list_transactions(
            tag="groceries",
        )
        assert_matches_type(TransactionArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncFirefly) -> None:
        tag = await async_client.tags.list_transactions(
            tag="groceries",
            end=parse_date("2026-04-30"),
            limit=10,
            page=1,
            start=parse_date("2026-04-01"),
            type="all",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(TransactionArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        response = await async_client.tags.with_raw_response.list_transactions(
            tag="groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TransactionArray, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncFirefly) -> None:
        async with async_client.tags.with_streaming_response.list_transactions(
            tag="groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TransactionArray, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncFirefly) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            await async_client.tags.with_raw_response.list_transactions(
                tag="",
            )
