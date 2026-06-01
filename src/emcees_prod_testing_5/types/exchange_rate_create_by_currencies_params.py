# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeRateCreateByCurrenciesParams"]


class ExchangeRateCreateByCurrenciesParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]

    body: Required[Dict[str, str]]
    """The actual entries for this data set.

    They 'key' value is the date in YYYY-MM-DD. The value is the exchange rate.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
