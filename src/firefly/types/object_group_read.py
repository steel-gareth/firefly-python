# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ObjectGroupRead", "Attributes"]


class Attributes(BaseModel):
    order: int
    """Order of the object group"""

    title: str

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class ObjectGroupRead(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
