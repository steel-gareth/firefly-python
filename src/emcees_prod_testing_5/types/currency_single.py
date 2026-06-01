# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .currency_read import CurrencyRead

__all__ = ["CurrencySingle"]


class CurrencySingle(BaseModel):
    data: CurrencyRead
