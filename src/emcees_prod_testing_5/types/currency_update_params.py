# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CurrencyUpdateParams"]


class CurrencyUpdateParams(TypedDict, total=False):
    body_code: Annotated[str, PropertyInfo(alias="code")]
    """The currency code"""

    decimal_places: int
    """How many decimals to use when displaying this currency. Between 0 and 16."""

    enabled: bool
    """If the currency is enabled"""

    name: str
    """The currency name"""

    primary: Literal[True]
    """If the currency must be the primary for the user.

    You can only submit TRUE. Submitting FALSE will not drop this currency as the
    primary currency, because then the system would be without one.
    """

    symbol: str
    """The currency symbol"""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
