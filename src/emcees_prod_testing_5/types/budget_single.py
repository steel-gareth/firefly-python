# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .budget_read import BudgetRead

__all__ = ["BudgetSingle"]


class BudgetSingle(BaseModel):
    data: BudgetRead
