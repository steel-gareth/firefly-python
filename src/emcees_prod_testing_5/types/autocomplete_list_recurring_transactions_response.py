# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListRecurringTransactionsResponse", "AutocompleteListRecurringTransactionsResponseItem"]


class AutocompleteListRecurringTransactionsResponseItem(BaseModel):
    id: str

    name: str
    """Name of the recurrence found by an auto-complete search."""

    active: Optional[bool] = None
    """Is the recurring transaction active or not?"""

    description: Optional[str] = None
    """Description of the recurrence found by auto-complete."""


AutocompleteListRecurringTransactionsResponse: TypeAlias = List[AutocompleteListRecurringTransactionsResponseItem]
