# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AccountTypeFilter"]

AccountTypeFilter: TypeAlias = Literal[
    "all",
    "asset",
    "cash",
    "expense",
    "revenue",
    "special",
    "hidden",
    "liability",
    "liabilities",
    "Default account",
    "Cash account",
    "Asset account",
    "Expense account",
    "Revenue account",
    "Initial balance account",
    "Beneficiary account",
    "Import account",
    "Reconciliation account",
    "Loan",
    "Debt",
    "Mortgage",
]
