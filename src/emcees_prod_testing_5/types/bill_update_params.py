# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .bill_repeat_frequency import BillRepeatFrequency

__all__ = ["BillUpdateParams"]


class BillUpdateParams(TypedDict, total=False):
    name: Required[str]

    active: bool
    """If the bill is active."""

    amount_max: str

    amount_min: str

    currency_code: str
    """Use either currency_id or currency_code"""

    currency_id: str
    """Use either currency_id or currency_code"""

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date after which this bill is no longer valid or applicable"""

    extension_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date before which the bill must be renewed (or cancelled)"""

    notes: Optional[str]

    object_group_id: Optional[str]
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_title: Optional[str]
    """The name of the group. NULL if no group."""

    repeat_freq: BillRepeatFrequency
    """How often the bill must be paid."""

    skip: int
    """How often the bill must be skipped. 1 means a bi-monthly bill."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
