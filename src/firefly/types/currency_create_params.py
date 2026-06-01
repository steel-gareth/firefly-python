# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CurrencyCreateParams"]


class CurrencyCreateParams(TypedDict, total=False):
    code: Required[str]

    name: Required[str]

    symbol: Required[str]

    decimal_places: int
    """Supports 0-16 decimals."""

    enabled: bool
    """Defaults to true"""

    primary: bool
    """Make this currency the primary currency for the current administration.

    You can set this value to FALSE, in which case nothing will change to the
    primary currency. If you set it to TRUE, the current primary currency will no
    longer be the primary currency.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
