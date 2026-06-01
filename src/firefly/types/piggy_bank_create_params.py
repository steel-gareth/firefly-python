# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PiggyBankCreateParams", "Account"]


class PiggyBankCreateParams(TypedDict, total=False):
    account_id: Required[object]

    name: Required[str]

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The date you started with this piggy bank."""

    target_amount: Required[Optional[str]]

    accounts: Iterable[Account]

    current_amount: str

    notes: Optional[str]

    object_group_id: Optional[str]
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_title: Optional[str]
    """The name of the group. NULL if no group."""

    order: int

    target_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The date you intend to finish saving money."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]


class Account(TypedDict, total=False):
    id: Required[Optional[str]]
    """The ID of the account."""

    current_amount: str
    """The amount saved currently."""

    name: Optional[str]
    """The name of the account."""
