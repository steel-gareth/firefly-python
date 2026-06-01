# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TransferListByAssetAccountResponse", "TransferListByAssetAccountResponseItem"]


class TransferListByAssetAccountResponseItem(BaseModel):
    id: Optional[str] = None
    """This ID is a reference to the original object."""

    currency_code: Optional[str] = None
    """The currency code of the expenses listed for this account."""

    currency_id: Optional[str] = None
    """The currency ID of the expenses listed for this account."""

    difference: Optional[str] = None
    """
    The total amount transferred between start date and end date, a number defined
    as a string, for this asset account.
    """

    difference_float: Optional[float] = None
    """
    The total amount transferred between start date and end date, a number as a
    float, for this asset account. May have rounding errors.
    """

    in_: Optional[str] = FieldInfo(alias="in", default=None)
    """
    The total amount transferred TO this account between start date and end date, a
    number defined as a string, for this asset account.
    """

    in_float: Optional[float] = None
    """
    The total amount transferred FROM this account between start date and end date,
    a number as a float, for this asset account. May have rounding errors.
    """

    name: Optional[str] = None
    """This is the name of the object."""

    out: Optional[str] = None
    """
    The total amount transferred FROM this account between start date and end date,
    a number defined as a string, for this asset account.
    """

    out_float: Optional[float] = None
    """
    The total amount transferred TO this account between start date and end date, a
    number as a float, for this asset account. May have rounding errors.
    """


TransferListByAssetAccountResponse: TypeAlias = List[TransferListByAssetAccountResponseItem]
