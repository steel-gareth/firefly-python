# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .currency_read import CurrencyRead

__all__ = ["CurrencyListResponse"]


class CurrencyListResponse(BaseModel):
    data: List[CurrencyRead]

    links: PageLink

    meta: Meta
