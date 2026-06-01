# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListCategoriesResponse", "AutocompleteListCategoriesResponseItem"]


class AutocompleteListCategoriesResponseItem(BaseModel):
    id: str

    name: str
    """Name of the category found by an auto-complete search."""


AutocompleteListCategoriesResponse: TypeAlias = List[AutocompleteListCategoriesResponseItem]
