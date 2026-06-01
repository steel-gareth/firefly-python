# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .user_read import UserRead

__all__ = ["UserSingle"]


class UserSingle(BaseModel):
    data: UserRead
