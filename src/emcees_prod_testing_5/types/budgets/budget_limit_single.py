# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .budget_limit_read import BudgetLimitRead

__all__ = ["BudgetLimitSingle"]


class BudgetLimitSingle(BaseModel):
    data: BudgetLimitRead
