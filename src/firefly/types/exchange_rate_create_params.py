# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeRateCreateParams"]


class ExchangeRateCreateParams(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]
    """The date to which the exchange rate is applicable."""

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """The base currency code."""

    rates: Required[object]

    to: Required[str]
    """The destination currency code."""

    rate: str
    """The exchange rate from the base currency to the destination currency."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
