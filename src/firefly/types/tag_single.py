# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .tag_read import TagRead

__all__ = ["TagSingle"]


class TagSingle(BaseModel):
    data: TagRead
