# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BillListParams"]


class BillListParams(TypedDict, total=False):
    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD.

    If it is added to the request, Firefly III will calculate the appropriate
    payment and paid dates.
    """

    limit: int
    """Number of items per page. The default pagination is per 50 items."""

    page: int
    """Page number. The default pagination is per 50 items."""

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD.

    If it is are added to the request, Firefly III will calculate the appropriate
    payment and paid dates.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
