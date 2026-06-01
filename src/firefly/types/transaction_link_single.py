# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .transaction_link_read import TransactionLinkRead

__all__ = ["TransactionLinkSingle"]


class TransactionLinkSingle(BaseModel):
    data: TransactionLinkRead
