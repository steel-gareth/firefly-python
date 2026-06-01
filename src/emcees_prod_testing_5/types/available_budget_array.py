# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .available_budget_read import AvailableBudgetRead

__all__ = ["AvailableBudgetArray"]


class AvailableBudgetArray(BaseModel):
    data: List[AvailableBudgetRead]

    meta: Meta
