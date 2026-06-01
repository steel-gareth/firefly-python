# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExpenseListByExpenseAccountParams"]


class ExpenseListByExpenseAccountParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    start: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    accounts: Iterable[int]
    """The accounts to be included in the results.

    If you add the accounts ID's of expense accounts, only those accounts are
    included in the results. If you include ID's of asset accounts or liabilities,
    only withdrawals from those asset accounts / liabilities will be included. You
    can combine both asset / liability and expense account ID's. Other account ID's
    will be ignored.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
