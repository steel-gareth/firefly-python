# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .account_role_property import AccountRoleProperty
from .liability_type_property import LiabilityTypeProperty
from .interest_period_property import InterestPeriodProperty
from .credit_card_type_property import CreditCardTypeProperty

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    name: Required[str]

    type: Required[object]

    account_number: Optional[str]

    account_role: Optional[AccountRoleProperty]
    """Is only mandatory when the type is asset."""

    active: bool
    """If omitted, defaults to true."""

    bic: Optional[str]

    credit_card_type: Optional[CreditCardTypeProperty]
    """Mandatory when the account_role is ccAsset. Can only be monthlyFull or null."""

    currency_code: str
    """Use either currency_id or currency_code.

    Defaults to the user's financial administration's currency.
    """

    currency_id: str
    """Use either currency_id or currency_code.

    Defaults to the user's financial administration's currency.
    """

    iban: Optional[str]

    include_net_worth: bool
    """If omitted, defaults to true."""

    interest: Optional[str]
    """Mandatory when type is liability. Interest percentage."""

    interest_period: Optional[InterestPeriodProperty]
    """Mandatory when type is liability. Period over which the interest is calculated."""

    latitude: Optional[float]
    """Latitude of the account's location, if applicable.

    Can be used to draw a map. If omitted, the existing location will be kept. If
    submitted as NULL, the current location will be removed.
    """

    liability_type: Optional[LiabilityTypeProperty]
    """Mandatory when type is liability. Specifies the exact type."""

    longitude: Optional[float]
    """Latitude of the account's location, if applicable.

    Can be used to draw a map. If omitted, the existing location will be kept. If
    submitted as NULL, the current location will be removed.
    """

    monthly_payment_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Mandatory when the account_role is ccAsset.

    Moment at which CC payment installments are asked for by the bank.
    """

    notes: Optional[str]

    opening_balance: str

    opening_balance_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    order: int
    """Order of the account"""

    virtual_balance: str

    zoom_level: Optional[int]
    """Zoom level for the map, if drawn.

    This to set the box right. Unfortunately this is a proprietary value because
    each map provider has different zoom levels. If omitted, the existing location
    will be kept. If submitted as NULL, the current location will be removed.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
