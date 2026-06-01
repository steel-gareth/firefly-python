# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .piggy_bank_read import PiggyBankRead

__all__ = ["PiggyBankArray"]


class PiggyBankArray(BaseModel):
    data: List[PiggyBankRead]

    links: PageLink

    meta: Meta
