# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeRateListParams"]


class ExchangeRateListParams(TypedDict, total=False):
    limit: int
    """Number of items per page. The default pagination is per 50 items."""

    page: int
    """Page number. The default pagination is per 50 items."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
