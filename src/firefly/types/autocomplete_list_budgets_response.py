# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListBudgetsResponse", "AutocompleteListBudgetsResponseItem"]


class AutocompleteListBudgetsResponseItem(BaseModel):
    id: str

    name: str
    """Name of the budget found by an auto-complete search."""

    active: Optional[bool] = None
    """Is the budget active or not?"""


AutocompleteListBudgetsResponse: TypeAlias = List[AutocompleteListBudgetsResponseItem]
