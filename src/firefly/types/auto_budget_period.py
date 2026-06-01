# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["AutoBudgetPeriod"]

AutoBudgetPeriod: TypeAlias = Optional[Literal["daily", "weekly", "monthly", "quarterly", "half-year", "yearly"]]
