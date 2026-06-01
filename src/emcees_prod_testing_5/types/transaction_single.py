# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .transaction_read import TransactionRead

__all__ = ["TransactionSingle"]


class TransactionSingle(BaseModel):
    data: TransactionRead
