# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListTransactionTypesResponse", "AutocompleteListTransactionTypesResponseItem"]


class AutocompleteListTransactionTypesResponseItem(BaseModel):
    id: str

    name: str
    """Type of the object found by an auto-complete search."""

    type: str
    """Name of the object found by an auto-complete search."""


AutocompleteListTransactionTypesResponse: TypeAlias = List[AutocompleteListTransactionTypesResponseItem]
