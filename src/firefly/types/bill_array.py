# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .bill_read import BillRead

__all__ = ["BillArray"]


class BillArray(BaseModel):
    data: List[BillRead]

    meta: Meta
