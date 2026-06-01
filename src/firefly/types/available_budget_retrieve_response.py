# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .available_budget_read import AvailableBudgetRead

__all__ = ["AvailableBudgetRetrieveResponse"]


class AvailableBudgetRetrieveResponse(BaseModel):
    data: AvailableBudgetRead
