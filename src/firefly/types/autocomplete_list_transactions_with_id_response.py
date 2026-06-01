# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListTransactionsWithIDResponse", "AutocompleteListTransactionsWithIDResponseItem"]


class AutocompleteListTransactionsWithIDResponseItem(BaseModel):
    id: str
    """The ID of a transaction journal (basically a single split)."""

    description: str
    """Transaction description with ID in the name."""

    name: str
    """Transaction description with ID in the name."""

    transaction_group_id: Optional[str] = None
    """The ID of the underlying transaction group."""


AutocompleteListTransactionsWithIDResponse: TypeAlias = List[AutocompleteListTransactionsWithIDResponseItem]
