# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .object_link import ObjectLink

__all__ = ["PiggyBankRead", "Attributes", "AttributesAccount"]


class AttributesAccount(BaseModel):
    account_id: Optional[str] = None
    """The ID of the account."""

    current_amount: Optional[str] = None

    name: Optional[str] = None

    pc_current_amount: Optional[str] = None
    """If convertToPrimary is on, this will show the amount in the primary currency."""


class Attributes(BaseModel):
    account_id: object

    name: str

    target_amount: Optional[str] = None

    accounts: Optional[List[AttributesAccount]] = None

    active: Optional[bool] = None

    created_at: Optional[datetime] = None

    currency_code: Optional[str] = None
    """The currency code of the currency associated with this object."""

    currency_decimal_places: Optional[int] = None

    currency_id: Optional[str] = None
    """The currency ID of the currency associated with this object."""

    currency_name: Optional[str] = None
    """The currency name of the currency associated with this object."""

    currency_symbol: Optional[str] = None

    current_amount: Optional[str] = None

    left_to_save: Optional[str] = None

    notes: Optional[str] = None

    object_group_id: Optional[str] = None
    """The group ID of the group this object is part of. NULL if no group."""

    object_group_order: Optional[int] = None
    """The order of the group. At least 1, for the highest sorting."""

    object_group_title: Optional[str] = None
    """The name of the group. NULL if no group."""

    object_has_currency_setting: Optional[bool] = None
    """Indicates whether the object has a currency setting.

    If false, the object uses the administration's primary currency.
    """

    order: Optional[int] = None

    pc_current_amount: Optional[str] = None
    """The current amount in the primary currency of the administration."""

    pc_left_to_save: Optional[str] = None

    pc_save_per_month: Optional[str] = None

    pc_target_amount: Optional[str] = None
    """The target amount in the primary currency of the administration."""

    percentage: Optional[int] = None
    """
    The percentage of the target amount that has been saved, if a target amount is
    set.
    """

    primary_currency_code: Optional[str] = None
    """The currency code of the administration's primary currency."""

    primary_currency_decimal_places: Optional[int] = None
    """The currency decimal places of the administration's primary currency."""

    primary_currency_id: Optional[str] = None
    """The currency ID of the administration's primary currency."""

    primary_currency_name: Optional[str] = None
    """The currency name of the administration's primary currency."""

    primary_currency_symbol: Optional[str] = None
    """The currency symbol of the administration's primary currency."""

    save_per_month: Optional[str] = None

    start_date: Optional[datetime] = None
    """The date you started with this piggy bank."""

    target_date: Optional[datetime] = None
    """The date you intend to finish saving money."""

    updated_at: Optional[datetime] = None


class PiggyBankRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
