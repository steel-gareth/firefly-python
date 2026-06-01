# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .auto_budget_type import AutoBudgetType
from .auto_budget_period import AutoBudgetPeriod
from .array_entry_with_currency_and_sum import ArrayEntryWithCurrencyAndSum

__all__ = ["BudgetRead", "Attributes"]


class Attributes(BaseModel):
    name: str

    active: Optional[bool] = None

    auto_budget_amount: Optional[str] = None
    """The amount for the auto-budget, if set."""

    auto_budget_period: Optional[AutoBudgetPeriod] = None
    """Period for the auto budget"""

    auto_budget_type: Optional[AutoBudgetType] = None
    """The type of auto-budget that Firefly III must create."""

    created_at: Optional[datetime] = None

    currency_code: Optional[str] = None
    """The currency code of the currency associated with this object."""

    currency_decimal_places: Optional[int] = None

    currency_id: Optional[str] = None
    """The currency ID of the currency associated with this object."""

    currency_name: Optional[str] = None
    """The currency name of the currency associated with this object."""

    currency_symbol: Optional[str] = None

    notes: Optional[str] = None

    object_group_id: Optional[str] = None
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_order: Optional[int] = None
    """The order of the group. At least 1, for the highest sorting."""

    object_group_title: Optional[str] = None
    """The name of the group. NULL if no group."""

    object_has_currency_setting: Optional[bool] = None
    """Indicates whether the object has a currency setting.

    If false, the object uses the administration's primary currency.
    """

    order: Optional[int] = None

    pc_auto_budget_amount: Optional[str] = None
    """
    The amount for the auto-budget, if set in the primary currency of the
    administration.
    """

    pc_spent: Optional[List[ArrayEntryWithCurrencyAndSum]] = None
    """Information on how much was spent in this budget.

    Is only filled in when the start and end date are submitted. It is converted to
    the primary currency of the administration.
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
    """Information on how much was spent in this budget.

    Is only filled in when the start and end date are submitted.
    """

    updated_at: Optional[datetime] = None


class BudgetRead(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
