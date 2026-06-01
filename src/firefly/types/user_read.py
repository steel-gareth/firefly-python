# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .user import User
from .._models import BaseModel
from .object_link import ObjectLink

__all__ = ["UserRead"]


class UserRead(BaseModel):
    id: str

    attributes: User

    links: ObjectLink

    type: str
    """Immutable value"""
