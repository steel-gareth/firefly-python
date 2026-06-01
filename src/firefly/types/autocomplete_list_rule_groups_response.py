# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListRuleGroupsResponse", "AutocompleteListRuleGroupsResponseItem"]


class AutocompleteListRuleGroupsResponseItem(BaseModel):
    id: str

    name: str
    """Name of the rule group found by an auto-complete search."""

    active: Optional[bool] = None
    """Is the bill active or not?"""

    description: Optional[str] = None
    """Description of the rule group found by auto-complete."""


AutocompleteListRuleGroupsResponse: TypeAlias = List[AutocompleteListRuleGroupsResponseItem]
