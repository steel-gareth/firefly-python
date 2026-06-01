# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Meta", "Pagination"]


class Pagination(BaseModel):
    count: Optional[int] = None

    current_page: Optional[int] = None

    per_page: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class Meta(BaseModel):
    pagination: Optional[Pagination] = None
