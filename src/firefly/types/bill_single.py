# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .bill_read import BillRead

__all__ = ["BillSingle"]


class BillSingle(BaseModel):
    data: BillRead
