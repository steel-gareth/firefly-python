# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InsightGroupEntry"]


class InsightGroupEntry(BaseModel):
    id: Optional[str] = None
    """This ID is a reference to the original object."""

    currency_code: Optional[str] = None
    """The currency code of the expenses listed for this account."""

    currency_id: Optional[str] = None
    """The currency ID of the expenses listed for this account."""

    difference: Optional[str] = None
    """
    The amount spent or earned between start date and end date, a number defined as
    a string, for this object and all asset accounts.
    """

    difference_float: Optional[float] = None
    """
    The amount spent or earned between start date and end date, a number as a float,
    for this object and all asset accounts. May have rounding errors.
    """

    name: Optional[str] = None
    """This is the name of the object."""
