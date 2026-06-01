# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ArrayEntryWithCurrencyAndSum"]


class ArrayEntryWithCurrencyAndSum(BaseModel):
    currency_code: Optional[str] = None

    currency_decimal_places: Optional[int] = None
    """Number of decimals supported by the currency"""

    currency_id: Optional[str] = None

    currency_symbol: Optional[str] = None

    sum: Optional[str] = None
    """The amount earned, spent or transferred."""
