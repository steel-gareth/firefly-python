# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListPiggyBanksResponse", "AutocompleteListPiggyBanksResponseItem"]


class AutocompleteListPiggyBanksResponseItem(BaseModel):
    id: str

    name: str
    """Name of the piggy bank found by an auto-complete search."""

    currency_code: Optional[str] = None
    """Currency code for this piggy bank.

    This will always be the currency of the piggy bank, never the user's primary
    currency.
    """

    currency_decimal_places: Optional[int] = None
    """Number of decimal places for the currency used by this piggy bank.

    This will always be the currency of the piggy bank, never the user's primary
    currency.
    """

    currency_id: Optional[str] = None
    """Currency ID for this piggy bank.

    This will always be the currency of the piggy bank, never the user's primary
    currency.
    """

    currency_name: Optional[str] = None
    """Currency name for the currency used by this piggy bank.

    This will always be the currency of the piggy bank, never the user's primary
    currency.
    """

    currency_symbol: Optional[str] = None

    object_group_id: Optional[str] = None
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_title: Optional[str] = None
    """The name of the group. NULL if no group."""


AutocompleteListPiggyBanksResponse: TypeAlias = List[AutocompleteListPiggyBanksResponseItem]
