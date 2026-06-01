# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListPiggyBanksWithBalanceResponse", "AutocompleteListPiggyBanksWithBalanceResponseItem"]


class AutocompleteListPiggyBanksWithBalanceResponseItem(BaseModel):
    id: str

    name: str
    """Name of the piggy bank found by an auto-complete search."""

    currency_code: Optional[str] = None
    """Currency code for the currency used by this piggy bank.

    This will always be the piggy bank's currency, never the primary currency.
    """

    currency_decimal_places: Optional[int] = None
    """Currency decimal places for the currency used by this piggy bank.

    This will always be the piggy bank's currency, never the primary currency.
    """

    currency_id: Optional[str] = None
    """Currency ID for the currency used by this piggy bank.

    This will always be the piggy bank's currency, never the primary currency.
    """

    currency_symbol: Optional[str] = None
    """Currency symbol for the currency used by this piggy bank.

    This will always be the piggy bank's currency, never the primary currency.
    """

    name_with_balance: Optional[str] = None
    """
    Name of the piggy bank found by an auto-complete search, including the currently
    saved amount and the target amount.
    """

    object_group_id: Optional[str] = None
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_title: Optional[str] = None
    """The name of the group. NULL if no group."""


AutocompleteListPiggyBanksWithBalanceResponse: TypeAlias = List[AutocompleteListPiggyBanksWithBalanceResponseItem]
