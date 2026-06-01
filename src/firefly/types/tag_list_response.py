# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .tag_read import TagRead
from .page_link import PageLink

__all__ = ["TagListResponse"]


class TagListResponse(BaseModel):
    data: List[TagRead]

    links: PageLink

    meta: Meta
