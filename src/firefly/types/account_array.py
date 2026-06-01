# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .account_read import AccountRead

__all__ = ["AccountArray"]


class AccountArray(BaseModel):
    data: List[AccountRead]

    meta: Meta
