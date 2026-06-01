# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .budget_read import BudgetRead

__all__ = ["BudgetListResponse"]


class BudgetListResponse(BaseModel):
    data: List[BudgetRead]

    meta: Meta
