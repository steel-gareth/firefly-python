# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeRateUpdateParams"]


class ExchangeRateUpdateParams(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]
    """The date to which the exchange rate is applicable."""

    rate: Required[str]
    """The exchange rate from the base currency to the destination currency."""

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]
    """The base currency code."""

    to: Optional[str]
    """The destination currency code."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
