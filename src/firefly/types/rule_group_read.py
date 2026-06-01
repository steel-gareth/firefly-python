# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .object_link import ObjectLink

__all__ = ["RuleGroupRead", "Attributes"]


class Attributes(BaseModel):
    title: str

    active: Optional[bool] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    order: Optional[int] = None

    updated_at: Optional[datetime] = None


class RuleGroupRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
