# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .recurrence_repetition_type import RecurrenceRepetitionType
from .recurrence_transaction_type import RecurrenceTransactionType

__all__ = ["RecurrenceCreateParams", "Repetition", "Transaction"]


class RecurrenceCreateParams(TypedDict, total=False):
    first_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """First time the recurring transaction will fire. Must be after today."""

    repeat_until: Required[Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]]
    """Date until the recurring transaction can fire.

    Use either this field or repetitions.
    """

    repetitions: Required[Iterable[Repetition]]

    title: Required[str]

    transactions: Required[Iterable[Transaction]]

    type: Required[RecurrenceTransactionType]

    active: bool
    """If the recurrence is even active."""

    apply_rules: bool
    """Whether or not to fire the rules after the creation of a transaction."""

    description: str
    """
    Not to be confused with the description of the actual transaction(s) being
    created.
    """

    notes: Optional[str]

    nr_of_repetitions: Optional[int]
    """Max number of created transactions. Use either this field or repeat_until."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]


class Repetition(TypedDict, total=False):
    moment: Required[str]
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

    type: Required[RecurrenceRepetitionType]
    """The type of the repetition.

    ndom means: the n-th weekday of the month, where you can also specify which day
    of the week.
    """

    skip: int
    """How many occurrences to skip. 0 means skip nothing. 1 means every other."""

    weekend: int
    """How to respond when the recurring transaction falls in the weekend.

    Possible values:

    1. Do nothing, just create it
    2. Create no transaction.
    3. Skip to the previous Friday.
    4. Skip to the next Monday.
    """


class Transaction(TypedDict, total=False):
    amount: Required[str]
    """Amount of the transaction."""

    description: Required[str]

    destination_id: Required[str]
    """ID of the destination account."""

    source_id: Required[str]
    """ID of the source account."""

    bill_id: Optional[str]
    """Optional."""

    budget_id: str
    """The budget ID for this transaction."""

    category_id: str
    """Category ID for this transaction."""

    currency_code: str
    """Submit either a currency_id or a currency_code."""

    currency_id: str
    """Submit either a currency_id or a currency_code."""

    foreign_amount: Optional[str]
    """Foreign amount of the transaction."""

    foreign_currency_code: Optional[str]
    """Submit either a foreign_currency_id or a foreign_currency_code, or neither."""

    foreign_currency_id: Optional[str]
    """Submit either a foreign_currency_id or a foreign_currency_code, or neither."""

    piggy_bank_id: Optional[str]
    """Optional."""

    tags: Optional[SequenceNotStr[str]]
    """Array of tags."""
