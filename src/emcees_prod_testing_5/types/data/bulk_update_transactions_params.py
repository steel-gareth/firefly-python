# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BulkUpdateTransactionsParams"]


class BulkUpdateTransactionsParams(TypedDict, total=False):
    query: Required[str]
    """The JSON query."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
