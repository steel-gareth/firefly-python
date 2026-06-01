# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListCurrenciesWithCodeResponse", "AutocompleteListCurrenciesWithCodeResponseItem"]


class AutocompleteListCurrenciesWithCodeResponseItem(BaseModel):
    id: str

    code: str
    """Currency code."""

    decimal_places: int

    name: str
    """Currency name with the code between brackets."""

    symbol: str


AutocompleteListCurrenciesWithCodeResponse: TypeAlias = List[AutocompleteListCurrenciesWithCodeResponseItem]
