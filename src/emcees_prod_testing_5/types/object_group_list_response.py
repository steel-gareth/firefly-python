# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .object_group_read import ObjectGroupRead

__all__ = ["ObjectGroupListResponse"]


class ObjectGroupListResponse(BaseModel):
    data: List[ObjectGroupRead]

    meta: Meta
