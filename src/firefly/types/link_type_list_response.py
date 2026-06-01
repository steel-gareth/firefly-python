# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .link_type_read import LinkTypeRead

__all__ = ["LinkTypeListResponse"]


class LinkTypeListResponse(BaseModel):
    data: List[LinkTypeRead]

    links: PageLink

    meta: Meta
