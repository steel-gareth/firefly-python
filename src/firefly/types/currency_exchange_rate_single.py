# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .currency_exchange_rate_read import CurrencyExchangeRateRead

__all__ = ["CurrencyExchangeRateSingle"]


class CurrencyExchangeRateSingle(BaseModel):
    data: CurrencyExchangeRateRead
