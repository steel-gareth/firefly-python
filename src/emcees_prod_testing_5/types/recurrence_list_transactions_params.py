# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .transaction_type_filter import TransactionTypeFilter

__all__ = ["RecurrenceListTransactionsParams"]


class RecurrenceListTransactionsParams(TypedDict, total=False):
    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD. Both the start and end date must be present."""

    limit: int
    """Number of items per page. The default pagination is per 50 items."""

    page: int
    """Page number. The default pagination is per 50 items."""

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD. Both the start and end date must be present."""

    type: TransactionTypeFilter

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
