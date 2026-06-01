# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .currency_exchange_rate_read import CurrencyExchangeRateRead

__all__ = ["CurrencyExchangeRateArray"]


class CurrencyExchangeRateArray(BaseModel):
    data: List[CurrencyExchangeRateRead]

    links: PageLink

    meta: Meta
