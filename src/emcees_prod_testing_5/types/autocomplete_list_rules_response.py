# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListRulesResponse", "AutocompleteListRulesResponseItem"]


class AutocompleteListRulesResponseItem(BaseModel):
    id: str

    name: str
    """Name of the rule found by an auto-complete search."""

    active: Optional[bool] = None
    """Is the bill active or not?"""

    description: Optional[str] = None
    """Description of the rule found by auto-complete."""


AutocompleteListRulesResponse: TypeAlias = List[AutocompleteListRulesResponseItem]
