# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .user_read import UserRead

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    data: List[UserRead]

    links: PageLink

    meta: Meta
