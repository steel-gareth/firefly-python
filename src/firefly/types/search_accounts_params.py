# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .account_type_filter import AccountTypeFilter

__all__ = ["SearchAccountsParams"]


class SearchAccountsParams(TypedDict, total=False):
    field: Required[Literal["all", "iban", "name", "number", "id"]]
    """The account field(s) you want to search in."""

    query: Required[str]
    """The query you wish to search for."""

    limit: int
    """Number of items per page. The default pagination is per 50 items."""

    page: int
    """Page number. The default pagination is per 50 items."""

    type: AccountTypeFilter

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
