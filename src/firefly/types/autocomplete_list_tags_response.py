# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListTagsResponse", "AutocompleteListTagsResponseItem"]


class AutocompleteListTagsResponseItem(BaseModel):
    id: str

    name: str
    """Name of the tag found by an auto-complete search."""

    tag: str
    """Name of the tag found by an auto-complete search."""


AutocompleteListTagsResponse: TypeAlias = List[AutocompleteListTagsResponseItem]
