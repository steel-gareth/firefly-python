# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .category_read import CategoryRead

__all__ = ["CategorySingle"]


class CategorySingle(BaseModel):
    data: CategoryRead
