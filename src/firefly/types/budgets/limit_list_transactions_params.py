# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..transaction_type_filter import TransactionTypeFilter

__all__ = ["LimitListTransactionsParams"]


class LimitListTransactionsParams(TypedDict, total=False):
    id: Required[str]

    limit: int
    """Number of items per page. The default pagination is per 50 items."""

    page: int
    """Page number. The default pagination is per 50 items."""

    type: TransactionTypeFilter

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
