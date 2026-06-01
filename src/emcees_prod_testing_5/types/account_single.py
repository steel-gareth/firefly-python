# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .account_read import AccountRead

__all__ = ["AccountSingle"]


class AccountSingle(BaseModel):
    data: AccountRead
