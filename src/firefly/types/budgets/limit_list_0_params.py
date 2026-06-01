# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LimitList0Params"]


class LimitList0Params(TypedDict, total=False):
    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD."""

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
