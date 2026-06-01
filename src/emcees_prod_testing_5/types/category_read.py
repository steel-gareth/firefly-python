# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .array_entry_with_currency_and_sum import ArrayEntryWithCurrencyAndSum

__all__ = ["CategoryRead", "Attributes"]


class Attributes(BaseModel):
    name: str

    created_at: Optional[datetime] = None

    earned: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """Amount(s) earned in the currencies in the database for this category.

    ONLY present when start and date are set.
    """

    notes: Optional[str] = None

    object_has_currency_setting: Optional[bool] = None
    """This object never has its own currency setting, so this value is always false."""

    pc_earned: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """Amount(s) earned in the primary currency in the database for this category.

    ONLY present when start and date are set.
    """

    pc_spent: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """Amount(s) spent in the primary currency in the database for this category.

    ONLY present when start and date are set.
    """

    pc_transferred: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """Amount(s) transferred in primary currency in the database for this category.

    ONLY present when start and date are set.
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

    spent: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """Amount(s) spent in the currencies in the database for this category.

    ONLY present when start and date are set.
    """

    transferred: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """Amount(s) transferred in the currencies in the database for this category.

    ONLY present when start and date are set.
    """

    updated_at: Optional[datetime] = None


class CategoryRead(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
