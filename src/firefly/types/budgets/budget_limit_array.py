# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..meta import Meta
from ..._models import BaseModel
from .budget_limit_read import BudgetLimitRead

__all__ = ["BudgetLimitArray"]


class BudgetLimitArray(BaseModel):
    data: List[BudgetLimitRead]

    meta: Meta
