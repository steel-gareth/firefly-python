# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .account_type_filter import AccountTypeFilter

__all__ = ["AutocompleteListAccountsParams"]


class AutocompleteListAccountsParams(TypedDict, total=False):
    date: str
    """
    If the account is an asset account or a liability, the autocomplete will also
    return the balance of the account on this date.
    """

    limit: int
    """The number of items returned."""

    query: str
    """The autocomplete search query."""

    types: List[AccountTypeFilter]
    """Optional filter on the account type(s) used in the autocomplete."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
