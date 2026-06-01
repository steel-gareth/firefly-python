# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .recurrence_repetition_type import RecurrenceRepetitionType

__all__ = ["RecurrenceUpdateParams", "Repetition", "Transaction"]


class RecurrenceUpdateParams(TypedDict, total=False):
    active: bool
    """If the recurrence is even active."""

    apply_rules: bool
    """Whether or not to fire the rules after the creation of a transaction."""

    description: str
    """
    Not to be confused with the description of the actual transaction(s) being
    created.
    """

    first_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """First time the recurring transaction will fire."""

    notes: Optional[str]

    nr_of_repetitions: Optional[int]
    """Max number of created transactions. Use either this field or repeat_until."""

    repeat_until: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Date until when the recurring transaction can fire.

    After that date, it's basically inactive. Use either this field or repetitions.
    """

    repetitions: Iterable[Repetition]

    title: str

    transactions: Iterable[Transaction]

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]


class Repetition(TypedDict, total=False):
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

    skip: int
    """How many occurrences to skip. 0 means skip nothing. 1 means every other."""

    type: RecurrenceRepetitionType
    """The type of the repetition.

    ndom means: the n-th weekday of the month, where you can also specify which day
    of the week.
    """

    weekend: int
    """How to respond when the recurring transaction falls in the weekend.

    Possible values:

    1. Do nothing, just create it
    2. Create no transaction.
    3. Skip to the previous Friday.
    4. Skip to the next Monday.
    """


class Transaction(TypedDict, total=False):
    id: Required[str]

    amount: str
    """Amount of the transaction."""

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

    description: str

    destination_id: str
    """ID of the destination account. Submit either this or destination_name."""

    foreign_amount: Optional[str]
    """Foreign amount of the transaction."""

    foreign_currency_id: Optional[str]
    """Submit either a foreign_currency_id or a foreign_currency_code, or neither."""

    piggy_bank_id: Optional[str]

    source_id: str
    """ID of the source account. Submit either this or source_name."""

    tags: Optional[SequenceNotStr[str]]
    """Array of tags."""
