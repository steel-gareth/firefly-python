# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PiggyBankUpdateParams", "Account"]


class PiggyBankUpdateParams(TypedDict, total=False):
    accounts: Iterable[Account]

    name: str

    notes: Optional[str]

    object_group_id: Optional[str]
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_title: Optional[str]
    """The name of the group. NULL if no group."""

    order: int

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The date you started with this piggy bank."""

    target_amount: Optional[str]

    target_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The date you intend to finish saving money."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]


class Account(TypedDict, total=False):
    id: Required[object]

    account_id: Optional[str]
    """The ID of the account."""

    current_amount: Optional[str]
    """The amount saved currently."""

    name: Optional[str]
    """The name of the account."""
