# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeRateCreateByDateParams"]


class ExchangeRateCreateByDateParams(TypedDict, total=False):
    body_date: Required[Annotated[object, PropertyInfo(alias="date")]]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """The 'from'-currency"""

    rates: Required[Dict[str, str]]
    """The actual entries for this data set.

    They 'key' value is 'to' currency. The value is the exchange rate.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
