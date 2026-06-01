# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    email: str
    """The new users email address."""

    blocked: Optional[bool] = None
    """Boolean to indicate if the user is blocked."""

    blocked_code: Optional[Literal["email_changed"]] = None
    """If you say the user must be blocked, this will be the reason code."""

    created_at: Optional[datetime] = None

    role: Optional[Literal["owner", "demo"]] = None
    """Role for the user. Can be empty or omitted."""

    updated_at: Optional[datetime] = None
