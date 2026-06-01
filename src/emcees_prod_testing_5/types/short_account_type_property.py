# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ShortAccountTypeProperty"]

ShortAccountTypeProperty: TypeAlias = Literal[
    "asset", "expense", "import", "revenue", "cash", "liability", "liabilities", "initial-balance", "reconciliation"
]
