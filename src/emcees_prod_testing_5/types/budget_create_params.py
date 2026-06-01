# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .auto_budget_type import AutoBudgetType
from .auto_budget_period import AutoBudgetPeriod

__all__ = ["BudgetCreateParams"]


class BudgetCreateParams(TypedDict, total=False):
    name: Required[str]

    active: bool

    auto_budget_amount: Optional[str]

    auto_budget_currency_code: Optional[str]
    """Use either currency_id or currency_code.

    Defaults to the user's financial administration's currency.
    """

    auto_budget_currency_id: Optional[str]
    """Use either currency_id or currency_code.

    Defaults to the user's financial administration's currency.
    """

    auto_budget_period: Optional[AutoBudgetPeriod]
    """Period for the auto budget"""

    auto_budget_type: Optional[AutoBudgetType]
    """The type of auto-budget that Firefly III must create."""

    fire_webhooks: bool
    """Whether or not to fire the webhooks that are related to this event."""

    notes: Optional[str]

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
