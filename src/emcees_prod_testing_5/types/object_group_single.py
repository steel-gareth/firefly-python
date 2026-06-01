# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .object_group_read import ObjectGroupRead

__all__ = ["ObjectGroupSingle"]


class ObjectGroupSingle(BaseModel):
    data: ObjectGroupRead
