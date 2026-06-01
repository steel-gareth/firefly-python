# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .object_link import ObjectLink

__all__ = ["CurrencyExchangeRateRead", "Attributes"]


class Attributes(BaseModel):
    created_at: Optional[datetime] = None

    date: Optional[datetime] = None
    """Date and time of the exchange rate."""

    from_currency_code: Optional[str] = None
    """Base currency code for this exchange rate entry."""

    from_currency_decimal_places: Optional[int] = None
    """Base currency decimal places for this exchange rate entry."""

    from_currency_id: Optional[str] = None
    """Base currency ID for this exchange rate entry."""

    from_currency_name: Optional[str] = None
    """Base currency name for this exchange rate entry."""

    from_currency_symbol: Optional[str] = None
    """Base currency symbol for this exchange rate entry."""

    rate: Optional[str] = None
    """The actual exchange rate.

    How many 'to' currency will you get for 1 'from' currency?
    """

    to_currency_code: Optional[str] = None
    """Destination currency code for this exchange rate entry."""

    to_currency_decimal_places: Optional[int] = None
    """Destination currency decimal places for this exchange rate entry."""

    to_currency_id: Optional[str] = None
    """Destination currency ID for this exchange rate entry."""

    to_currency_name: Optional[str] = None
    """Destination currency name for this exchange rate entry."""

    to_currency_symbol: Optional[str] = None
    """Destination currency symbol for this exchange rate entry."""

    updated_at: Optional[datetime] = None


class CurrencyExchangeRateRead(BaseModel):
    id: Optional[str] = None

    attributes: Optional[Attributes] = None

    links: Optional[ObjectLink] = None

    type: Optional[str] = None
    """Immutable value"""
