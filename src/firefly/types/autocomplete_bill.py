# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AutocompleteBill"]


class AutocompleteBill(BaseModel):
    id: str

    name: str
    """Name of the bill found by an auto-complete search."""

    active: Optional[bool] = None
    """Is the bill active or not?"""
