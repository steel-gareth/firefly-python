# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .insight_group_entry import InsightGroupEntry

__all__ = ["ExpenseListByBudgetResponse"]

ExpenseListByBudgetResponse: TypeAlias = List[InsightGroupEntry]
