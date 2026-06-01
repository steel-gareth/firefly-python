# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AccountTypeProperty"]

AccountTypeProperty: TypeAlias = Literal[
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
