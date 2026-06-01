# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .category_read import CategoryRead

__all__ = ["CategoryListResponse"]


class CategoryListResponse(BaseModel):
    data: List[CategoryRead]

    meta: Meta
