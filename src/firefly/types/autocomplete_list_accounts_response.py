# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AutocompleteListAccountsResponse", "AutocompleteListAccountsResponseItem"]


class AutocompleteListAccountsResponseItem(BaseModel):
    id: str

    currency_code: str
    """Currency code for the currency used by this account.

    If the user prefers amounts converted to their primary currency, this primary
    currency is used instead.
    """

    currency_decimal_places: int
    """Number of decimal places for the currency used by this account.

    If the user prefers amounts converted to their primary currency, this primary
    currency is used instead.
    """

    currency_id: str
    """ID for the currency used by this account.

    If the user prefers amounts converted to their primary currency, this primary
    currency is used instead.
    """

    currency_name: str
    """Currency name for the currency used by this account.

    If the user prefers amounts converted to their primary currency, this primary
    currency is used instead.
    """

    currency_symbol: str
    """Currency symbol for the currency used by this account.

    If the user prefers amounts converted to their primary currency, this primary
    currency is used instead.
    """

    name: str
    """Name of the account found by an auto-complete search."""

    name_with_balance: str
    """
    Asset accounts and liabilities have a second field with the given date's account
    balance in the account currency or primary currency.
    """

    type: str
    """Account type of the account found by the auto-complete search."""

    account_currency_code: Optional[str] = None
    """Code for the currency used by this account.

    Even if "convertToPrimary" is on, the account currency code is displayed here.
    """

    account_currency_decimal_places: Optional[int] = None
    """Number of decimal places for the currency used by this account.

    Even if "convertToPrimary" is on, the account currency code is displayed here.
    """

    account_currency_id: Optional[str] = None
    """ID for the currency used by this account.

    Even if "convertToPrimary" is on, the account currency ID is displayed here.
    """

    account_currency_name: Optional[str] = None
    """Name for the currency used by this account.

    Even if "convertToPrimary" is on, the account currency name is displayed here.
    """

    account_currency_symbol: Optional[str] = None
    """Code for the currency used by this account.

    Even if "convertToPrimary" is on, the account currency code is displayed here.
    """

    active: Optional[bool] = None
    """Is the bill active or not?"""


AutocompleteListAccountsResponse: TypeAlias = List[AutocompleteListAccountsResponseItem]
