# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from emcees_prod_testing_5 import EmceesProdTesting5, AsyncEmceesProdTesting5
from emcees_prod_testing_5.types import (
    CurrencyExchangeRateArray,
    CurrencyExchangeRateSingle,
)
from emcees_prod_testing_5._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExchangeRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
            rate="2.3456",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.retrieve(
            id="123",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.retrieve(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.exchange_rates.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
            from_="USD",
            to="EUR",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.exchange_rates.with_raw_response.update(
                id="",
                date=parse_date("2026-04-01"),
                rate="2.3456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.list()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.delete(
            id="123",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.exchange_rates.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_by_currencies(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_by_currencies_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_by_currencies(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_by_currencies(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_by_currencies(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            client.exchange_rates.with_raw_response.create_by_currencies(
                to="USD",
                from_="",
                body={
                    "2025-08-01": "1.2345",
                    "2025-08-02": "6.3456",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            client.exchange_rates.with_raw_response.create_by_currencies(
                to="",
                from_="EUR",
                body={
                    "2025-08-01": "1.2345",
                    "2025-08-02": "6.3456",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_by_date(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_by_date_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_by_date(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_by_date(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_by_date(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_date` but received ''"):
            client.exchange_rates.with_raw_response.create_by_date(
                path_date="",
                body_date={},
                from_="EUR",
                rates={
                    "USD": "1.2345",
                    "GBP": "6.3456",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all_by_currencies(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.delete_all_by_currencies(
            to="USD",
            from_="EUR",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all_by_currencies_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.delete_all_by_currencies(
            to="USD",
            from_="EUR",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all_by_currencies(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.delete_all_by_currencies(
            to="USD",
            from_="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all_by_currencies(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.delete_all_by_currencies(
            to="USD",
            from_="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all_by_currencies(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            client.exchange_rates.with_raw_response.delete_all_by_currencies(
                to="USD",
                from_="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            client.exchange_rates.with_raw_response.delete_all_by_currencies(
                to="",
                from_="EUR",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_date(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_date_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_by_date(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_date(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_by_date(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            client.exchange_rates.with_raw_response.delete_by_date(
                date="2026-04-01",
                from_="",
                to="USD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            client.exchange_rates.with_raw_response.delete_by_date(
                date="2026-04-01",
                from_="EUR",
                to="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            client.exchange_rates.with_raw_response.delete_by_date(
                date="",
                from_="EUR",
                to="USD",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_currencies(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.list_by_currencies(
            to="USD",
            from_="EUR",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_by_currencies_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.list_by_currencies(
            to="USD",
            from_="EUR",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_by_currencies(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.list_by_currencies(
            to="USD",
            from_="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_by_currencies(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.list_by_currencies(
            to="USD",
            from_="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_by_currencies(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            client.exchange_rates.with_raw_response.list_by_currencies(
                to="USD",
                from_="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            client.exchange_rates.with_raw_response.list_by_currencies(
                to="",
                from_="EUR",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_date(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_date_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_date(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_date(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_date(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            client.exchange_rates.with_raw_response.retrieve_by_date(
                date="2026-04-01",
                from_="",
                to="USD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            client.exchange_rates.with_raw_response.retrieve_by_date(
                date="2026-04-01",
                from_="EUR",
                to="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            client.exchange_rates.with_raw_response.retrieve_by_date(
                date="",
                from_="EUR",
                to="USD",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_date(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_by_date_with_all_params(self, client: EmceesProdTesting5) -> None:
        exchange_rate = client.exchange_rates.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_by_date(self, client: EmceesProdTesting5) -> None:
        response = client.exchange_rates.with_raw_response.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_by_date(self, client: EmceesProdTesting5) -> None:
        with client.exchange_rates.with_streaming_response.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_by_date(self, client: EmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            client.exchange_rates.with_raw_response.update_by_date(
                date="2026-04-01",
                from_="",
                to="USD",
                rate="2.3456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            client.exchange_rates.with_raw_response.update_by_date(
                date="2026-04-01",
                from_="EUR",
                to="",
                rate="2.3456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            client.exchange_rates.with_raw_response.update_by_date(
                date="",
                from_="EUR",
                to="USD",
                rate="2.3456",
            )


class TestAsyncExchangeRates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
            rate="2.3456",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.create(
            date=parse_date("2026-04-01"),
            from_="USD",
            rates={},
            to="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.retrieve(
            id="123",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.retrieve(
            id="123",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.retrieve(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.retrieve(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.exchange_rates.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
            from_="USD",
            to="EUR",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.update(
            id="123",
            date=parse_date("2026-04-01"),
            rate="2.3456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.exchange_rates.with_raw_response.update(
                id="",
                date=parse_date("2026-04-01"),
                rate="2.3456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.list()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.list(
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.delete(
            id="123",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.delete(
            id="123",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.delete(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.delete(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.exchange_rates.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_by_currencies_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.create_by_currencies(
            to="USD",
            from_="EUR",
            body={
                "2025-08-01": "1.2345",
                "2025-08-02": "6.3456",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            await async_client.exchange_rates.with_raw_response.create_by_currencies(
                to="USD",
                from_="",
                body={
                    "2025-08-01": "1.2345",
                    "2025-08-02": "6.3456",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            await async_client.exchange_rates.with_raw_response.create_by_currencies(
                to="",
                from_="EUR",
                body={
                    "2025-08-01": "1.2345",
                    "2025-08-02": "6.3456",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_by_date_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.create_by_date(
            path_date="2026-04-01",
            body_date={},
            from_="EUR",
            rates={
                "USD": "1.2345",
                "GBP": "6.3456",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_date` but received ''"):
            await async_client.exchange_rates.with_raw_response.create_by_date(
                path_date="",
                body_date={},
                from_="EUR",
                rates={
                    "USD": "1.2345",
                    "GBP": "6.3456",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.delete_all_by_currencies(
            to="USD",
            from_="EUR",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all_by_currencies_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.delete_all_by_currencies(
            to="USD",
            from_="EUR",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.delete_all_by_currencies(
            to="USD",
            from_="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.delete_all_by_currencies(
            to="USD",
            from_="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            await async_client.exchange_rates.with_raw_response.delete_all_by_currencies(
                to="USD",
                from_="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            await async_client.exchange_rates.with_raw_response.delete_all_by_currencies(
                to="",
                from_="EUR",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_date_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert exchange_rate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.delete_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert exchange_rate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            await async_client.exchange_rates.with_raw_response.delete_by_date(
                date="2026-04-01",
                from_="",
                to="USD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            await async_client.exchange_rates.with_raw_response.delete_by_date(
                date="2026-04-01",
                from_="EUR",
                to="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            await async_client.exchange_rates.with_raw_response.delete_by_date(
                date="",
                from_="EUR",
                to="USD",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.list_by_currencies(
            to="USD",
            from_="EUR",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_by_currencies_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.list_by_currencies(
            to="USD",
            from_="EUR",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.list_by_currencies(
            to="USD",
            from_="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.list_by_currencies(
            to="USD",
            from_="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_by_currencies(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            await async_client.exchange_rates.with_raw_response.list_by_currencies(
                to="USD",
                from_="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            await async_client.exchange_rates.with_raw_response.list_by_currencies(
                to="",
                from_="EUR",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_date_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            limit=10,
            page=1,
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.retrieve_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateArray, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            await async_client.exchange_rates.with_raw_response.retrieve_by_date(
                date="2026-04-01",
                from_="",
                to="USD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            await async_client.exchange_rates.with_raw_response.retrieve_by_date(
                date="2026-04-01",
                from_="EUR",
                to="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            await async_client.exchange_rates.with_raw_response.retrieve_by_date(
                date="",
                from_="EUR",
                to="USD",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_by_date_with_all_params(self, async_client: AsyncEmceesProdTesting5) -> None:
        exchange_rate = await async_client.exchange_rates.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
            x_trace_id="40c71bbb-c676-4f24-83cf-cc725d7d7a00",
        )
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        response = await async_client.exchange_rates.with_raw_response.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        async with async_client.exchange_rates.with_streaming_response.update_by_date(
            date="2026-04-01",
            from_="EUR",
            to="USD",
            rate="2.3456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(CurrencyExchangeRateSingle, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_by_date(self, async_client: AsyncEmceesProdTesting5) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_` but received ''"):
            await async_client.exchange_rates.with_raw_response.update_by_date(
                date="2026-04-01",
                from_="",
                to="USD",
                rate="2.3456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to` but received ''"):
            await async_client.exchange_rates.with_raw_response.update_by_date(
                date="2026-04-01",
                from_="EUR",
                to="",
                rate="2.3456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            await async_client.exchange_rates.with_raw_response.update_by_date(
                date="",
                from_="EUR",
                to="USD",
                rate="2.3456",
            )
