# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetListParams"]


class BudgetListParams(TypedDict, total=False):
    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD, to get info on how much the user has spent.

    You must submit both start and end.
    """

    limit: int
    """Number of items per page. The default pagination is per 50 items."""

    page: int
    """Page number. The default pagination is per 50 items."""

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD, to get info on how much the user has spent.

    You must submit both start and end.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
