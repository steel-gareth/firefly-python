# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    email: Required[str]
    """The new users email address."""

    blocked: bool
    """Boolean to indicate if the user is blocked."""

    blocked_code: Optional[Literal["email_changed"]]
    """If you say the user must be blocked, this will be the reason code."""

    role: Optional[Literal["owner", "demo"]]
    """Role for the user. Can be empty or omitted."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
