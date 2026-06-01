# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .transaction_read import TransactionRead

__all__ = ["TransactionArray"]


class TransactionArray(BaseModel):
    data: List[TransactionRead]

    links: PageLink

    meta: Meta
