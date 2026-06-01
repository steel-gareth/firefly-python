# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .insight_total_entry import InsightTotalEntry

__all__ = ["ExpenseListWithoutCategoryResponse"]

ExpenseListWithoutCategoryResponse: TypeAlias = List[InsightTotalEntry]
