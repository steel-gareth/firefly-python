# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IncomeListByTagParams"]


class IncomeListByTagParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    start: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    accounts: Iterable[int]
    """The accounts to be included in the results.

    If you include ID's of asset accounts or liabilities, only deposits to those
    asset accounts / liabilities will be included. Other account ID's will be
    ignored.
    """

    tags: Iterable[int]
    """The tags to be included in the results."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
