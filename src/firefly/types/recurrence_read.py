# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel
from .object_link import ObjectLink
from .account_type_property import AccountTypeProperty
from .recurrence_repetition_type import RecurrenceRepetitionType
from .recurrence_transaction_type import RecurrenceTransactionType

__all__ = ["RecurrenceRead", "Attributes", "AttributesRepetition", "AttributesTransaction"]


class AttributesRepetition(BaseModel):
    moment: str
    """Information that defined the type of repetition.

    - For 'daily', this is empty.
    - For 'weekly', it is day of the week between 1 and 7 (Monday - Sunday).
    - For 'ndom', it is '1,2' or '4,5' or something else, where the first number is
      the week in the month, and the second number is the day in the week (between 1
      and 7). '2,3' means: the 2nd Wednesday of the month
    - For 'monthly' it is the day of the month (1 - 31)
    - For yearly, it is a full date, ie '2026-04-01'. The year you use does not
      matter.
    """

    type: RecurrenceRepetitionType
    """The type of the repetition.

    ndom means: the n-th weekday of the month, where you can also specify which day
    of the week.
    """

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Auto-generated repetition description."""

    occurrences: Optional[List[datetime]] = None
    """Array of future dates when the repetition will apply to. Auto generated."""

    skip: Optional[int] = None
    """How many occurrences to skip. 0 means skip nothing. 1 means every other."""

    updated_at: Optional[datetime] = None

    weekend: Optional[int] = None
    """How to respond when the recurring transaction falls in the weekend.

    Possible values:

    1. Do nothing, just create it
    2. Create no transaction.
    3. Skip to the previous Friday.
    4. Skip to the next Monday.
    """


class AttributesTransaction(BaseModel):
    amount: str
    """Amount of the transaction."""

    description: str

    id: Optional[str] = None

    budget_id: Optional[str] = None
    """The budget ID for this transaction."""

    budget_name: Optional[str] = None
    """The name of the budget to be used.

    If the budget name is unknown, the ID will be used or the value will be ignored.
    """

    category_id: Optional[str] = None
    """Category ID for this transaction."""

    category_name: Optional[str] = None
    """Category name for this transaction."""

    currency_code: Optional[str] = None
    """The currency code of the currency associated with this object."""

    currency_decimal_places: Optional[int] = None

    currency_id: Optional[str] = None
    """The currency ID of the currency associated with this object."""

    currency_name: Optional[str] = None
    """The currency name of the currency associated with this object."""

    currency_symbol: Optional[str] = None

    destination_iban: Optional[str] = None

    destination_id: Optional[str] = None
    """ID of the destination account. Submit either this or destination_name."""

    destination_name: Optional[str] = None
    """Name of the destination account. Submit either this or destination_id."""

    destination_type: Optional[AccountTypeProperty] = None

    foreign_amount: Optional[str] = None
    """Foreign amount of the transaction."""

    foreign_currency_code: Optional[str] = None

    foreign_currency_decimal_places: Optional[int] = None
    """Number of decimals in the currency"""

    foreign_currency_id: Optional[str] = None

    foreign_currency_name: Optional[str] = None

    foreign_currency_symbol: Optional[str] = None

    object_has_currency_setting: Optional[bool] = None
    """Indicates whether the object has a currency setting.

    If false, the object uses the administration's primary currency.
    """

    pc_amount: Optional[str] = None
    """Amount of the transaction in primary currency."""

    pc_foreign_amount: Optional[str] = None
    """Foreign amount of the transaction."""

    piggy_bank_id: Optional[str] = None

    piggy_bank_name: Optional[str] = None

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

    source_iban: Optional[str] = None

    source_id: Optional[str] = None
    """ID of the source account. Submit either this or source_name."""

    source_name: Optional[str] = None
    """Name of the source account. Submit either this or source_id."""

    source_type: Optional[AccountTypeProperty] = None

    subscription_id: Optional[str] = None

    subscription_name: Optional[str] = None

    tags: Optional[List[str]] = None
    """Array of tags."""


class Attributes(BaseModel):
    active: Optional[bool] = None
    """If the recurrence is even active."""

    apply_rules: Optional[bool] = None
    """Whether or not to fire the rules after the creation of a transaction."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """
    Not to be confused with the description of the actual transaction(s) being
    created.
    """

    first_date: Optional[date] = None
    """First time the recurring transaction will fire. Must be after today."""

    latest_date: Optional[date] = None
    """Last time the recurring transaction has fired."""

    notes: Optional[str] = None

    nr_of_repetitions: Optional[int] = None
    """Max number of created transactions. Use either this field or repeat_until."""

    repeat_until: Optional[date] = None
    """Date until the recurring transaction can fire.

    Use either this field or repetitions.
    """

    repetitions: Optional[List[AttributesRepetition]] = None

    title: Optional[str] = None

    transactions: Optional[List[AttributesTransaction]] = None

    type: Optional[RecurrenceTransactionType] = None

    updated_at: Optional[datetime] = None


class RecurrenceRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
