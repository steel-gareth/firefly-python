# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CurrencyRead", "Attributes"]


class Attributes(BaseModel):
    code: str

    name: str

    symbol: str

    created_at: Optional[datetime] = None

    decimal_places: Optional[int] = None
    """Supports 0-16 decimals."""

    enabled: Optional[bool] = None
    """Defaults to true"""

    primary: Optional[bool] = None
    """Is the primary currency?"""

    updated_at: Optional[datetime] = None


class CurrencyRead(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
