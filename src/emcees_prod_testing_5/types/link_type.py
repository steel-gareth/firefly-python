# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LinkType"]


class LinkType(BaseModel):
    inward: str

    name: str

    outward: str

    editable: Optional[bool] = None
