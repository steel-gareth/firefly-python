# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TransactionTypeFilter"]

TransactionTypeFilter: TypeAlias = Literal[
    "all",
    "withdrawal",
    "withdrawals",
    "expense",
    "deposit",
    "deposits",
    "income",
    "transfer",
    "transfers",
    "opening_balance",
    "reconciliation",
    "special",
    "specials",
    "default",
]
