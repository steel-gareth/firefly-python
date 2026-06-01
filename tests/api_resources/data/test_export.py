# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from firefly import Firefly, AsyncFirefly
from firefly._utils import parse_date
from firefly._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_accounts(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_accounts()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_accounts_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_accounts(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_accounts(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_accounts()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_accounts(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_accounts() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_bills(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_bills()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_bills_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_bills(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_bills(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_bills()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_bills(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_bills() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_budgets(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_budgets()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_budgets_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_budgets(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_budgets(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_budgets()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_budgets(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_budgets() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_categories(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_categories()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_categories_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_categories(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_categories(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_categories()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_categories(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_categories() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_piggy_banks(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_piggy_banks()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_piggy_banks_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_piggy_banks(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_piggy_banks(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_piggy_banks()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_piggy_banks(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_piggy_banks() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_recurring(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_recurring()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_recurring_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_recurring(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_recurring(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_recurring()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_recurring(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_recurring() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_rules(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_rules()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_rules_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_rules(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_rules(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_rules()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_rules(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_rules() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_tags(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_tags()
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_tags_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_tags(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_tags(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_tags()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_tags(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_tags() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_transactions(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_transactions_with_all_params(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = client.data.export.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts="accounts",
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_transactions(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = client.data.export.with_raw_response.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_transactions(self, client: Firefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.data.export.with_streaming_response.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True


class TestAsyncExport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_accounts(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_accounts()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_accounts_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_accounts(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_accounts(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_accounts()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_accounts(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/accounts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_accounts() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_bills(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_bills()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_bills_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_bills(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_bills(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_bills()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_bills(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/bills").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_bills() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_budgets(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_budgets()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_budgets_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_budgets(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_budgets(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_budgets()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_budgets(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/budgets").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_budgets() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_categories(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_categories()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_categories_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_categories(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_categories(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_categories()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_categories(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/categories").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_categories() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_piggy_banks(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_piggy_banks()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_piggy_banks_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_piggy_banks(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_piggy_banks(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_piggy_banks()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_piggy_banks(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/piggy-banks").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_piggy_banks() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_recurring(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_recurring()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_recurring_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_recurring(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_recurring(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_recurring()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_recurring(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/recurring").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_recurring() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_rules(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_rules()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_rules_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_rules(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_rules(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_rules()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_rules(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/rules").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_rules() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_tags(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_tags()
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_tags_with_all_params(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_tags(
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_tags(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_tags()

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_tags(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_tags() as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_transactions(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_transactions_with_all_params(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        export = await async_client.data.export.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
            accounts="accounts",
            type="csv",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_transactions(self, async_client: AsyncFirefly, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        export = await async_client.data.export.with_raw_response.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_transactions(
        self, async_client: AsyncFirefly, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/v1/data/export/transactions").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.data.export.with_streaming_response.export_transactions(
            end=parse_date("2019-12-27"),
            start=parse_date("2019-12-27"),
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True
