# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .account_role_property import AccountRoleProperty
from .liability_type_property import LiabilityTypeProperty
from .interest_period_property import InterestPeriodProperty
from .credit_card_type_property import CreditCardTypeProperty
from .short_account_type_property import ShortAccountTypeProperty
from .liability_direction_property import LiabilityDirectionProperty

__all__ = ["AccountRead", "Attributes"]


class Attributes(BaseModel):
    name: str

    type: ShortAccountTypeProperty
    """Can only be one one these account types.

    import, initial-balance and reconciliation cannot be set manually.
    """

    account_number: Optional[str] = None

    account_role: Optional[AccountRoleProperty] = None
    """Is only mandatory when the type is asset."""

    active: Optional[bool] = None

    balance_difference: Optional[str] = None
    """
    If you submit a start AND end date, this will be the difference between those
    two moments.
    """

    bic: Optional[str] = None

    created_at: Optional[datetime] = None

    credit_card_type: Optional[CreditCardTypeProperty] = None
    """Mandatory when the account_role is ccAsset. Can only be monthlyFull or null."""

    currency_code: Optional[str] = None
    """The currency code of the currency associated with this object."""

    currency_decimal_places: Optional[int] = None

    currency_id: Optional[str] = None
    """The currency ID of the currency associated with this object."""

    currency_name: Optional[str] = None
    """The currency name of the currency associated with this object."""

    currency_symbol: Optional[str] = None

    current_balance: Optional[str] = None
    """The current balance of the account in the account's currency.

    If the account has no currency, this is the balance in the administration's
    primary currency. Either way, the `currency_*` fields reflect the currency used.
    """

    current_balance_date: Optional[datetime] = None
    """
    The timestamp for this date is always 23:59:59, to indicate it's the balance at
    the very END of that particular day.
    """

    debt_amount: Optional[str] = None
    """
    In liability accounts (loans, debts and mortgages), this is the amount of debt
    in the account's currency (see the `currency_*` fields). In asset accounts, this
    is NULL.
    """

    iban: Optional[str] = None

    include_net_worth: Optional[bool] = None

    interest: Optional[str] = None
    """Mandatory when type is liability. Interest percentage."""

    interest_period: Optional[InterestPeriodProperty] = None
    """Mandatory when type is liability. Period over which the interest is calculated."""

    last_activity: Optional[datetime] = None
    """Last activity of the account."""

    latitude: Optional[float] = None
    """Latitude of the accounts's location, if applicable. Can be used to draw a map."""

    liability_direction: Optional[LiabilityDirectionProperty] = None
    """'credit' indicates somebody owes you the liability.

    'debit' Indicates you owe this debt yourself. Works only for liabilities.
    """

    liability_type: Optional[LiabilityTypeProperty] = None
    """Mandatory when type is liability. Specifies the exact type."""

    longitude: Optional[float] = None
    """Latitude of the accounts's location, if applicable. Can be used to draw a map."""

    monthly_payment_date: Optional[datetime] = None
    """Mandatory when the account_role is ccAsset.

    Moment at which CC payment installments are asked for by the bank.
    """

    notes: Optional[str] = None

    object_group_id: Optional[str] = None
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_order: Optional[int] = None
    """The order of the group. At least 1, for the highest sorting."""

    object_group_title: Optional[str] = None
    """The name of the group. NULL if no group."""

    object_has_currency_setting: Optional[bool] = None
    """Indicates whether the account has a currency setting.

    If false, the account uses the administration's primary currency. Asset accounts
    and liability accounts always have a currency setting, while expense and revenue
    accounts do not.
    """

    opening_balance: Optional[str] = None
    """
    Represents the opening balance, the initial amount this account holds in the
    currency of the account or the administration's primary currency if the account
    has no currency. Either way, the `currency_*` fields reflect the currency used.
    """

    opening_balance_date: Optional[datetime] = None
    """Represents the date of the opening balance."""

    order: Optional[int] = None
    """Order of the account. Is NULL if account is not asset or liability."""

    pc_balance_difference: Optional[str] = None
    """
    If you submit a start AND end date, this will be the difference in the currency
    of the account or the administration's primary currency between those two
    moments.
    """

    pc_current_balance: Optional[str] = None
    """The current balance of the account in the administration's primary currency.

    The `primary_currency_*` fields reflect the currency used. This field is NULL if
    the user does have 'convert to primary' set to true in their settings.
    """

    pc_debt_amount: Optional[str] = None
    """
    In liability accounts (loans, debts and mortgages), this is the amount of debt
    in the administration's primary currency (see the `currency_*` fields. In asset
    accounts, this is NULL.
    """

    pc_opening_balance: Optional[str] = None
    """The opening balance of the account in the administration's primary currency
    (pc).

    The `primary_currency_*` fields reflect the currency used. This field is NULL if
    the user does have 'convert to primary' set to true in their settings.
    """

    pc_virtual_balance: Optional[str] = None
    """The virtual balance of the account in the administration's primary currency
    (pc).

    The `primary_currency_*` fields reflect the currency used. This field is NULL if
    the user does have 'convert to primary' set to true in their settings.
    """

    primary_currency_code: Optional[str] = None
    """The currency code of the administration's primary currency."""

    primary_currency_decimal_places: Optional[int] = None
    """The currency decimal places of the administration's primary currency."""

    primary_currency_id: Optional[str] = None
    """The currency ID of the administration's primary currency."""

    primary_currency_name: Optional[str] = None
    """The currency name of the administration's primary currency."""

    primary_currency_symbol: Optional[str] = None
    """The currency symbol of the administration's primary currency."""

    updated_at: Optional[datetime] = None

    virtual_balance: Optional[str] = None
    """
    The virtual balance of the account in the account's currency or the
    administration's primary currency if the account has no currency.
    """

    zoom_level: Optional[int] = None
    """Zoom level for the map, if drawn.

    This to set the box right. Unfortunately this is a proprietary value because
    each map provider has different zoom levels.
    """


class AccountRead(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
