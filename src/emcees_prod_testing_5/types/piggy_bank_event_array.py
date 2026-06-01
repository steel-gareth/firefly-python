# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .object_link import ObjectLink

__all__ = ["PiggyBankEventArray", "Data", "DataAttributes"]


class DataAttributes(BaseModel):
    amount: Optional[str] = None

    created_at: Optional[datetime] = None

    currency_code: Optional[str] = None
    """The currency code of the currency associated with this object."""

    currency_decimal_places: Optional[int] = None

    currency_id: Optional[str] = None
    """The currency ID of the currency associated with this object."""

    currency_name: Optional[str] = None
    """The currency name of the currency associated with this object."""

    currency_symbol: Optional[str] = None

    object_has_currency_setting: Optional[bool] = None
    """Indicates whether the object has a currency setting.

    If false, the object uses the administration's primary currency.
    """

    pc_amount: Optional[str] = None

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

    transaction_group_id: Optional[str] = None
    """The transaction group associated with the event."""

    transaction_journal_id: Optional[str] = None
    """The journal associated with the event."""

    updated_at: Optional[datetime] = None


class Data(BaseModel):
    id: str

    attributes: DataAttributes

    links: ObjectLink

    type: str
    """Immutable value"""


class PiggyBankEventArray(BaseModel):
    data: List[Data]

    links: PageLink

    meta: Meta
