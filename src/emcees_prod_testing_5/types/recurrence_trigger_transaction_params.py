# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecurrenceTriggerTransactionParams"]


class RecurrenceTriggerTransactionParams(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD.

    This is the date for which you want the recurrence to fire. You can take the
    date from the list of occurrences in the recurring transaction.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
