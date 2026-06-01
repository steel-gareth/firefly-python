# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .array_entry_with_currency_and_sum import ArrayEntryWithCurrencyAndSum

__all__ = ["AvailableBudgetRead", "Attributes"]


class Attributes(BaseModel):
    amount: Optional[str] = None
    """The amount of this available budget in the currency of this available budget."""

    created_at: Optional[datetime] = None

    currency_code: Optional[str] = None
    """The currency code of the currency associated with this object."""

    currency_decimal_places: Optional[int] = None

    currency_id: Optional[str] = None
    """The currency ID of the currency associated with this object."""

    currency_name: Optional[str] = None
    """The currency name of the currency associated with this object."""

    currency_symbol: Optional[str] = None

    end: Optional[datetime] = None
    """End date of the available budget."""

    object_has_currency_setting: Optional[bool] = None
    """Indicates whether the object has a currency setting.

    If false, the object uses the administration's primary currency.
    """

    pc_amount: Optional[str] = None
    """
    The amount of this available budget in the primary currency (pc) of this
    administration.
    """

    pc_spent_in_budgets: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """
    The amount spent in budgets in the primary currency (pc) of this administration.
    """

    pc_spent_outside_budgets: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """
    The amount spent outside of budgets in the primary currency (pc) of this
    administration.
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

    spent_in_budgets: Optional[List[ArrayEntryWithCurrencyAndSum]] = None

    spent_outside_budgets: Optional[List[ArrayEntryWithCurrencyAndSum]] = None

    start: Optional[datetime] = None
    """Start date of the available budget."""

    updated_at: Optional[datetime] = None


class AvailableBudgetRead(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
