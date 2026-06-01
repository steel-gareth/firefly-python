# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListObjectGroupsResponse", "AutocompleteListObjectGroupsResponseItem"]


class AutocompleteListObjectGroupsResponseItem(BaseModel):
    id: str

    name: str
    """Title of the object group found by an auto-complete search."""

    title: str
    """Title of the object group found by an auto-complete search."""


AutocompleteListObjectGroupsResponse: TypeAlias = List[AutocompleteListObjectGroupsResponseItem]
