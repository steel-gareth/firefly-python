# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SummaryRetrieveBasicResponse", "SummaryRetrieveBasicResponseItem"]


class SummaryRetrieveBasicResponseItem(BaseModel):
    currency_code: Optional[str] = None

    currency_decimal_places: Optional[int] = None
    """Number of decimals for the associated currency."""

    currency_id: Optional[str] = None
    """The currency ID of the associated currency."""

    currency_symbol: Optional[str] = None

    key: Optional[str] = None
    """
    This is a reference to the type of info shared, not influenced by translations
    or user preferences. The EUR value is a reference to the currency code.
    Possibilities are: balance-in-ABC, spent-in-ABC, earned-in-ABC,
    bills-paid-in-ABC, bills-unpaid-in-ABC, left-to-spend-in-ABC and
    net-worth-in-ABC.
    """

    local_icon: Optional[str] = None
    """Reference to a font-awesome icon without the fa- part."""

    monetary_value: Optional[float] = None
    """The amount as a float."""

    no_available_budgets: Optional[bool] = None
    """True if there are no available budgets available."""

    sub_title: Optional[str] = None
    """A short explanation of the amounts origin.

    Already formatted according to the locale of the user or translated, if
    relevant.
    """

    title: Optional[str] = None
    """A translated title for the information shared."""

    value_parsed: Optional[str] = None
    """The amount formatted according to the users locale"""


SummaryRetrieveBasicResponse: TypeAlias = Dict[str, SummaryRetrieveBasicResponseItem]
