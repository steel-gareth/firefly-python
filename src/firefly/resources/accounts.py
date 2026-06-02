# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date, datetime

import httpx

from ..types import (
    AccountTypeFilter,
    AccountRoleProperty,
    LiabilityTypeProperty,
    TransactionTypeFilter,
    CreditCardTypeProperty,
    InterestPeriodProperty,
    ShortAccountTypeProperty,
    LiabilityDirectionProperty,
    account_list_params,
    account_create_params,
    account_update_params,
    account_retrieve_params,
    account_list_attachments_params,
    account_list_piggy_banks_params,
    account_list_transactions_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.account_array import AccountArray
from ..types.account_single import AccountSingle
from ..types.attachment_array import AttachmentArray
from ..types.piggy_bank_array import PiggyBankArray
from ..types.transaction_array import TransactionArray
from ..types.account_type_filter import AccountTypeFilter
from ..types.account_role_property import AccountRoleProperty
from ..types.liability_type_property import LiabilityTypeProperty
from ..types.transaction_type_filter import TransactionTypeFilter
from ..types.interest_period_property import InterestPeriodProperty
from ..types.credit_card_type_property import CreditCardTypeProperty
from ..types.short_account_type_property import ShortAccountTypeProperty
from ..types.liability_direction_property import LiabilityDirectionProperty

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    """
    Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
    """

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: ShortAccountTypeProperty,
        account_number: Optional[str] | Omit = omit,
        account_role: Optional[AccountRoleProperty] | Omit = omit,
        active: bool | Omit = omit,
        bic: Optional[str] | Omit = omit,
        credit_card_type: Optional[CreditCardTypeProperty] | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        iban: Optional[str] | Omit = omit,
        include_net_worth: bool | Omit = omit,
        interest: Optional[str] | Omit = omit,
        interest_period: Optional[InterestPeriodProperty] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        liability_direction: Optional[LiabilityDirectionProperty] | Omit = omit,
        liability_type: Optional[LiabilityTypeProperty] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        monthly_payment_date: Union[str, datetime, None] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        opening_balance: str | Omit = omit,
        opening_balance_date: Union[str, datetime, None] | Omit = omit,
        order: int | Omit = omit,
        virtual_balance: str | Omit = omit,
        zoom_level: Optional[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSingle:
        """Creates a new account.

        The data required can be submitted as a JSON body or as a
        list of parameters (in key=value pairs, like a webform).

        Args:
          type: Can only be one one these account types. import, initial-balance and
              reconciliation cannot be set manually.

          account_role: Is only mandatory when the type is asset.

          active: If omitted, defaults to true.

          credit_card_type: Mandatory when the account_role is ccAsset. Can only be monthlyFull or null.

          currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          include_net_worth: If omitted, defaults to true.

          interest: Mandatory when type is liability. Interest percentage.

          interest_period: Mandatory when type is liability. Period over which the interest is calculated.

          latitude: Latitude of the accounts's location, if applicable. Can be used to draw a map.

          liability_direction: 'credit' indicates somebody owes you the liability. 'debit' Indicates you owe
              this debt yourself. Works only for liabilities.

          liability_type: Mandatory when type is liability. Specifies the exact type.

          longitude: Latitude of the accounts's location, if applicable. Can be used to draw a map.

          monthly_payment_date: Mandatory when the account_role is ccAsset. Moment at which CC payment
              installments are asked for by the bank.

          opening_balance: Represents the opening balance, the initial amount this account holds.

          opening_balance_date: Represents the date of the opening balance.

          order: Order of the account

          zoom_level: Zoom level for the map, if drawn. This to set the box right. Unfortunately this
              is a proprietary value because each map provider has different zoom levels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._post(
            "/v1/accounts",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "account_number": account_number,
                    "account_role": account_role,
                    "active": active,
                    "bic": bic,
                    "credit_card_type": credit_card_type,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "iban": iban,
                    "include_net_worth": include_net_worth,
                    "interest": interest,
                    "interest_period": interest_period,
                    "latitude": latitude,
                    "liability_direction": liability_direction,
                    "liability_type": liability_type,
                    "longitude": longitude,
                    "monthly_payment_date": monthly_payment_date,
                    "notes": notes,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "order": order,
                    "virtual_balance": virtual_balance,
                    "zoom_level": zoom_level,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSingle,
        )

    def retrieve(
        self,
        id: str,
        *,
        date: Union[str, date] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSingle:
        """Returns a single account by its ID.

        Args:
          date: A date formatted YYYY-MM-DD.

        When added to the request, Firefly III will show
              the account's balance on that day.

          end: A date formatted YYYY-MM-DD. Must be after "start". Can not be the same as
              "start". May be omitted.

          start: A date formatted YYYY-MM-DD. May be omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "end": end,
                        "start": start,
                    },
                    account_retrieve_params.AccountRetrieveParams,
                ),
            ),
            cast_to=AccountSingle,
        )

    def update(
        self,
        id: str,
        *,
        name: str,
        type: object,
        account_number: Optional[str] | Omit = omit,
        account_role: Optional[AccountRoleProperty] | Omit = omit,
        active: bool | Omit = omit,
        bic: Optional[str] | Omit = omit,
        credit_card_type: Optional[CreditCardTypeProperty] | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        iban: Optional[str] | Omit = omit,
        include_net_worth: bool | Omit = omit,
        interest: Optional[str] | Omit = omit,
        interest_period: Optional[InterestPeriodProperty] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        liability_type: Optional[LiabilityTypeProperty] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        monthly_payment_date: Union[str, datetime, None] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        opening_balance: str | Omit = omit,
        opening_balance_date: Union[str, datetime, None] | Omit = omit,
        order: int | Omit = omit,
        virtual_balance: str | Omit = omit,
        zoom_level: Optional[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSingle:
        """Used to update a single account.

        All fields that are not submitted will be
        cleared (set to NULL). The model will tell you which fields are mandatory.

        Args:
          account_role: Is only mandatory when the type is asset.

          active: If omitted, defaults to true.

          credit_card_type: Mandatory when the account_role is ccAsset. Can only be monthlyFull or null.

          currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          include_net_worth: If omitted, defaults to true.

          interest: Mandatory when type is liability. Interest percentage.

          interest_period: Mandatory when type is liability. Period over which the interest is calculated.

          latitude: Latitude of the account's location, if applicable. Can be used to draw a map. If
              omitted, the existing location will be kept. If submitted as NULL, the current
              location will be removed.

          liability_type: Mandatory when type is liability. Specifies the exact type.

          longitude: Latitude of the account's location, if applicable. Can be used to draw a map. If
              omitted, the existing location will be kept. If submitted as NULL, the current
              location will be removed.

          monthly_payment_date: Mandatory when the account_role is ccAsset. Moment at which CC payment
              installments are asked for by the bank.

          order: Order of the account

          zoom_level: Zoom level for the map, if drawn. This to set the box right. Unfortunately this
              is a proprietary value because each map provider has different zoom levels. If
              omitted, the existing location will be kept. If submitted as NULL, the current
              location will be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._put(
            path_template("/v1/accounts/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "account_number": account_number,
                    "account_role": account_role,
                    "active": active,
                    "bic": bic,
                    "credit_card_type": credit_card_type,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "iban": iban,
                    "include_net_worth": include_net_worth,
                    "interest": interest,
                    "interest_period": interest_period,
                    "latitude": latitude,
                    "liability_type": liability_type,
                    "longitude": longitude,
                    "monthly_payment_date": monthly_payment_date,
                    "notes": notes,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "order": order,
                    "virtual_balance": virtual_balance,
                    "zoom_level": zoom_level,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSingle,
        )

    def list(
        self,
        *,
        date: Union[str, date] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: AccountTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountArray:
        """
        This endpoint returns a list of all the accounts owned by the authenticated
        user.

        Args:
          date: A date formatted YYYY-MM-DD. When added to the request, Firefly III will show
              the account's balance on that day.

          end: A date formatted YYYY-MM-DD. Must be after "start". Can not be the same as
              "start". May be omitted.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD. May be omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                        "type": type,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountArray,
        )

    def delete(
        self,
        id: str,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Will permanently delete an account.

        Any associated transactions and piggy banks
        are ALSO deleted. Cannot be recovered from.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_attachments(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentArray:
        """Lists all attachments.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/accounts/{id}/attachments", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    account_list_attachments_params.AccountListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    def list_piggy_banks(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiggyBankArray:
        """
        This endpoint returns a list of all the piggy banks connected to the account.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/accounts/{id}/piggy-banks", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    account_list_piggy_banks_params.AccountListPiggyBanksParams,
                ),
            ),
            cast_to=PiggyBankArray,
        )

    def list_transactions(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        This endpoint returns a list of all the transactions connected to the account.

        Args:
          end: A date formatted YYYY-MM-DD.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/accounts/{id}/transactions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                        "type": type,
                    },
                    account_list_transactions_params.AccountListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AsyncAccountsResource(AsyncAPIResource):
    """
    Endpoints that deliver all of the user&#039;s asset, expense and other accounts (and the metadata) together with related transactions, piggy banks and other objects. Also delivers endpoints for CRUD operations for accounts.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/steel-gareth/firefly-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/steel-gareth/firefly-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: ShortAccountTypeProperty,
        account_number: Optional[str] | Omit = omit,
        account_role: Optional[AccountRoleProperty] | Omit = omit,
        active: bool | Omit = omit,
        bic: Optional[str] | Omit = omit,
        credit_card_type: Optional[CreditCardTypeProperty] | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        iban: Optional[str] | Omit = omit,
        include_net_worth: bool | Omit = omit,
        interest: Optional[str] | Omit = omit,
        interest_period: Optional[InterestPeriodProperty] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        liability_direction: Optional[LiabilityDirectionProperty] | Omit = omit,
        liability_type: Optional[LiabilityTypeProperty] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        monthly_payment_date: Union[str, datetime, None] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        opening_balance: str | Omit = omit,
        opening_balance_date: Union[str, datetime, None] | Omit = omit,
        order: int | Omit = omit,
        virtual_balance: str | Omit = omit,
        zoom_level: Optional[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSingle:
        """Creates a new account.

        The data required can be submitted as a JSON body or as a
        list of parameters (in key=value pairs, like a webform).

        Args:
          type: Can only be one one these account types. import, initial-balance and
              reconciliation cannot be set manually.

          account_role: Is only mandatory when the type is asset.

          active: If omitted, defaults to true.

          credit_card_type: Mandatory when the account_role is ccAsset. Can only be monthlyFull or null.

          currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          include_net_worth: If omitted, defaults to true.

          interest: Mandatory when type is liability. Interest percentage.

          interest_period: Mandatory when type is liability. Period over which the interest is calculated.

          latitude: Latitude of the accounts's location, if applicable. Can be used to draw a map.

          liability_direction: 'credit' indicates somebody owes you the liability. 'debit' Indicates you owe
              this debt yourself. Works only for liabilities.

          liability_type: Mandatory when type is liability. Specifies the exact type.

          longitude: Latitude of the accounts's location, if applicable. Can be used to draw a map.

          monthly_payment_date: Mandatory when the account_role is ccAsset. Moment at which CC payment
              installments are asked for by the bank.

          opening_balance: Represents the opening balance, the initial amount this account holds.

          opening_balance_date: Represents the date of the opening balance.

          order: Order of the account

          zoom_level: Zoom level for the map, if drawn. This to set the box right. Unfortunately this
              is a proprietary value because each map provider has different zoom levels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/accounts",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "account_number": account_number,
                    "account_role": account_role,
                    "active": active,
                    "bic": bic,
                    "credit_card_type": credit_card_type,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "iban": iban,
                    "include_net_worth": include_net_worth,
                    "interest": interest,
                    "interest_period": interest_period,
                    "latitude": latitude,
                    "liability_direction": liability_direction,
                    "liability_type": liability_type,
                    "longitude": longitude,
                    "monthly_payment_date": monthly_payment_date,
                    "notes": notes,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "order": order,
                    "virtual_balance": virtual_balance,
                    "zoom_level": zoom_level,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSingle,
        )

    async def retrieve(
        self,
        id: str,
        *,
        date: Union[str, date] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSingle:
        """Returns a single account by its ID.

        Args:
          date: A date formatted YYYY-MM-DD.

        When added to the request, Firefly III will show
              the account's balance on that day.

          end: A date formatted YYYY-MM-DD. Must be after "start". Can not be the same as
              "start". May be omitted.

          start: A date formatted YYYY-MM-DD. May be omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "end": end,
                        "start": start,
                    },
                    account_retrieve_params.AccountRetrieveParams,
                ),
            ),
            cast_to=AccountSingle,
        )

    async def update(
        self,
        id: str,
        *,
        name: str,
        type: object,
        account_number: Optional[str] | Omit = omit,
        account_role: Optional[AccountRoleProperty] | Omit = omit,
        active: bool | Omit = omit,
        bic: Optional[str] | Omit = omit,
        credit_card_type: Optional[CreditCardTypeProperty] | Omit = omit,
        currency_code: str | Omit = omit,
        currency_id: str | Omit = omit,
        iban: Optional[str] | Omit = omit,
        include_net_worth: bool | Omit = omit,
        interest: Optional[str] | Omit = omit,
        interest_period: Optional[InterestPeriodProperty] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        liability_type: Optional[LiabilityTypeProperty] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        monthly_payment_date: Union[str, datetime, None] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        opening_balance: str | Omit = omit,
        opening_balance_date: Union[str, datetime, None] | Omit = omit,
        order: int | Omit = omit,
        virtual_balance: str | Omit = omit,
        zoom_level: Optional[int] | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSingle:
        """Used to update a single account.

        All fields that are not submitted will be
        cleared (set to NULL). The model will tell you which fields are mandatory.

        Args:
          account_role: Is only mandatory when the type is asset.

          active: If omitted, defaults to true.

          credit_card_type: Mandatory when the account_role is ccAsset. Can only be monthlyFull or null.

          currency_code: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          currency_id: Use either currency_id or currency_code. Defaults to the user's financial
              administration's currency.

          include_net_worth: If omitted, defaults to true.

          interest: Mandatory when type is liability. Interest percentage.

          interest_period: Mandatory when type is liability. Period over which the interest is calculated.

          latitude: Latitude of the account's location, if applicable. Can be used to draw a map. If
              omitted, the existing location will be kept. If submitted as NULL, the current
              location will be removed.

          liability_type: Mandatory when type is liability. Specifies the exact type.

          longitude: Latitude of the account's location, if applicable. Can be used to draw a map. If
              omitted, the existing location will be kept. If submitted as NULL, the current
              location will be removed.

          monthly_payment_date: Mandatory when the account_role is ccAsset. Moment at which CC payment
              installments are asked for by the bank.

          order: Order of the account

          zoom_level: Zoom level for the map, if drawn. This to set the box right. Unfortunately this
              is a proprietary value because each map provider has different zoom levels. If
              omitted, the existing location will be kept. If submitted as NULL, the current
              location will be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._put(
            path_template("/v1/accounts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "account_number": account_number,
                    "account_role": account_role,
                    "active": active,
                    "bic": bic,
                    "credit_card_type": credit_card_type,
                    "currency_code": currency_code,
                    "currency_id": currency_id,
                    "iban": iban,
                    "include_net_worth": include_net_worth,
                    "interest": interest,
                    "interest_period": interest_period,
                    "latitude": latitude,
                    "liability_type": liability_type,
                    "longitude": longitude,
                    "monthly_payment_date": monthly_payment_date,
                    "notes": notes,
                    "opening_balance": opening_balance,
                    "opening_balance_date": opening_balance_date,
                    "order": order,
                    "virtual_balance": virtual_balance,
                    "zoom_level": zoom_level,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSingle,
        )

    async def list(
        self,
        *,
        date: Union[str, date] | Omit = omit,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: AccountTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountArray:
        """
        This endpoint returns a list of all the accounts owned by the authenticated
        user.

        Args:
          date: A date formatted YYYY-MM-DD. When added to the request, Firefly III will show
              the account's balance on that day.

          end: A date formatted YYYY-MM-DD. Must be after "start". Can not be the same as
              "start". May be omitted.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD. May be omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                        "type": type,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountArray,
        )

    async def delete(
        self,
        id: str,
        *,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Will permanently delete an account.

        Any associated transactions and piggy banks
        are ALSO deleted. Cannot be recovered from.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/accounts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_attachments(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttachmentArray:
        """Lists all attachments.

        Args:
          limit: Number of items per page.

        The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/accounts/{id}/attachments", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    account_list_attachments_params.AccountListAttachmentsParams,
                ),
            ),
            cast_to=AttachmentArray,
        )

    async def list_piggy_banks(
        self,
        id: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiggyBankArray:
        """
        This endpoint returns a list of all the piggy banks connected to the account.

        Args:
          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/accounts/{id}/piggy-banks", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    account_list_piggy_banks_params.AccountListPiggyBanksParams,
                ),
            ),
            cast_to=PiggyBankArray,
        )

    async def list_transactions(
        self,
        id: str,
        *,
        end: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        start: Union[str, date] | Omit = omit,
        type: TransactionTypeFilter | Omit = omit,
        x_trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionArray:
        """
        This endpoint returns a list of all the transactions connected to the account.

        Args:
          end: A date formatted YYYY-MM-DD.

          limit: Number of items per page. The default pagination is per 50 items.

          page: Page number. The default pagination is per 50 items.

          start: A date formatted YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/vnd.api+json", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"X-Trace-Id": x_trace_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/accounts/{id}/transactions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "limit": limit,
                        "page": page,
                        "start": start,
                        "type": type,
                    },
                    account_list_transactions_params.AccountListTransactionsParams,
                ),
            ),
            cast_to=TransactionArray,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            accounts.delete,
        )
        self.list_attachments = to_raw_response_wrapper(
            accounts.list_attachments,
        )
        self.list_piggy_banks = to_raw_response_wrapper(
            accounts.list_piggy_banks,
        )
        self.list_transactions = to_raw_response_wrapper(
            accounts.list_transactions,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            accounts.delete,
        )
        self.list_attachments = async_to_raw_response_wrapper(
            accounts.list_attachments,
        )
        self.list_piggy_banks = async_to_raw_response_wrapper(
            accounts.list_piggy_banks,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            accounts.list_transactions,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            accounts.delete,
        )
        self.list_attachments = to_streamed_response_wrapper(
            accounts.list_attachments,
        )
        self.list_piggy_banks = to_streamed_response_wrapper(
            accounts.list_piggy_banks,
        )
        self.list_transactions = to_streamed_response_wrapper(
            accounts.list_transactions,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            accounts.delete,
        )
        self.list_attachments = async_to_streamed_response_wrapper(
            accounts.list_attachments,
        )
        self.list_piggy_banks = async_to_streamed_response_wrapper(
            accounts.list_piggy_banks,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            accounts.list_transactions,
        )
