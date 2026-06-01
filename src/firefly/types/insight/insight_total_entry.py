# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InsightTotalEntry"]


class InsightTotalEntry(BaseModel):
    currency_code: Optional[str] = None
    """The currency code of the expenses listed for this expense account."""

    currency_id: Optional[str] = None
    """The currency ID of the expenses listed for this expense account."""

    difference: Optional[str] = None
    """
    The amount spent between start date and end date, defined as a string, for this
    expense account and all asset accounts.
    """

    difference_float: Optional[float] = None
    """
    The amount spent between start date and end date, defined as a string, for this
    expense account and all asset accounts. This number is a float (double) and may
    have rounding errors.
    """
