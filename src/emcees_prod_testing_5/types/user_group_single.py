# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .user_group_read import UserGroupRead

__all__ = ["UserGroupSingle"]


class UserGroupSingle(BaseModel):
    data: UserGroupRead
