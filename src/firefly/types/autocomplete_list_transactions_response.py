# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListTransactionsResponse", "AutocompleteListTransactionsResponseItem"]


class AutocompleteListTransactionsResponseItem(BaseModel):
    id: str
    """The ID of a transaction journal (basically a single split)."""

    description: str
    """Transaction description"""

    name: str
    """Transaction description"""

    transaction_group_id: Optional[str] = None
    """The ID of the underlying transaction group."""


AutocompleteListTransactionsResponse: TypeAlias = List[AutocompleteListTransactionsResponseItem]
