# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PageLink"]


class PageLink(BaseModel):
    first: Optional[str] = None

    last: Optional[str] = None

    next: Optional[str] = None

    prev: Optional[str] = None

    self: Optional[str] = None
