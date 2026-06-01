# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .user_group_read import UserGroupRead

__all__ = ["UserGroupListResponse"]


class UserGroupListResponse(BaseModel):
    data: List[UserGroupRead]

    links: PageLink

    meta: Meta
