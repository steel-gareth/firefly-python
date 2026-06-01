# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DataDestroyParams"]


class DataDestroyParams(TypedDict, total=False):
    objects: Required[
        Literal[
            "not_assets_liabilities",
            "budgets",
            "bills",
            "piggy_banks",
            "rules",
            "recurring",
            "categories",
            "tags",
            "object_groups",
            "accounts",
            "asset_accounts",
            "expense_accounts",
            "revenue_accounts",
            "liabilities",
            "transactions",
            "withdrawals",
            "deposits",
            "transfers",
        ]
    ]
    """The type of data that you wish to destroy. You can only use one at a time."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
