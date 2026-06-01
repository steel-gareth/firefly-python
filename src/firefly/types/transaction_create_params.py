# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .transaction_type_property import TransactionTypeProperty

__all__ = ["TransactionCreateParams", "Transaction"]


class TransactionCreateParams(TypedDict, total=False):
    transactions: Required[Iterable[Transaction]]

    apply_rules: bool
    """Whether or not to apply rules when submitting transaction."""

    error_if_duplicate_hash: bool
    """Break if the submitted transaction exists already."""

    fire_webhooks: bool
    """Whether or not to fire the webhooks that are related to this event."""

    group_title: Optional[str]
    """Title of the transaction if it has been split in more than one piece.

    Empty otherwise.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]


class Transaction(TypedDict, total=False):
    amount: Required[str]
    """Amount of the transaction."""

    date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Date of the transaction"""

    description: Required[str]
    """Description of the transaction."""

    type: Required[TransactionTypeProperty]

    bill_id: Optional[str]
    """Optional. Use either this or the bill_name"""

    bill_name: Optional[str]
    """Optional. Use either this or the bill_id"""

    book_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    budget_id: Optional[str]
    """The budget ID for this transaction."""

    budget_name: Optional[str]
    """The name of the budget to be used.

    If the budget name is unknown, the ID will be used or the value will be ignored.
    """

    category_id: Optional[str]
    """The category ID for this transaction."""

    category_name: Optional[str]
    """The name of the category to be used.

    If the category is unknown, it will be created. If the ID and the name point to
    different categories, the ID overrules the name.
    """

    currency_code: Optional[str]
    """Currency code.

    Default is the source account's currency, or the user's financial
    administration's primary currency. The value you submit may be overruled by the
    source or destination account.
    """

    currency_id: Optional[str]
    """Currency ID.

    Default is the source account's currency, or the user's financial
    administration's currency. The value you submit may be overruled by the source
    or destination account.
    """

    destination_id: Optional[str]
    """ID of the destination account.

    For a deposit or a transfer, this must always be an asset account. For
    withdrawals this must be an expense account.
    """

    destination_name: Optional[str]
    """Name of the destination account.

    You can submit the name instead of the ID. For everything except transfers, the
    account will be auto-generated if unknown, so submitting a name is enough.
    """

    due_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    external_id: Optional[str]
    """Reference to external ID in other systems."""

    external_url: Optional[str]
    """External, custom URL for this transaction."""

    foreign_amount: Optional[str]
    """The amount in a foreign currency."""

    foreign_currency_code: Optional[str]
    """Currency code of the foreign currency.

    Default is NULL. Can be used instead of the foreign_currency_id, but this or the
    ID is required when submitting a foreign amount.
    """

    foreign_currency_id: Optional[str]
    """Currency ID of the foreign currency.

    Default is null. Is required when you submit a foreign amount.
    """

    interest_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    internal_reference: Optional[str]
    """Reference to internal reference of other systems."""

    invoice_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    notes: Optional[str]

    order: Optional[int]
    """Order of this entry in the list of transactions."""

    payment_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    piggy_bank_id: Optional[int]
    """Optional. Use either this or the piggy_bank_name"""

    piggy_bank_name: Optional[str]
    """Optional. Use either this or the piggy_bank_id"""

    process_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    reconciled: bool
    """If the transaction has been reconciled already.

    When you set this, the amount can no longer be edited by the user.
    """

    sepa_batch_id: Optional[str]
    """SEPA Batch ID"""

    sepa_cc: Optional[str]
    """SEPA Clearing Code"""

    sepa_ci: Optional[str]
    """SEPA Creditor Identifier"""

    sepa_country: Optional[str]
    """SEPA Country"""

    sepa_ct_id: Optional[str]
    """SEPA end-to-end Identifier"""

    sepa_ct_op: Optional[str]
    """SEPA Opposing Account Identifier"""

    sepa_db: Optional[str]
    """SEPA mandate identifier"""

    sepa_ep: Optional[str]
    """SEPA External Purpose indicator"""

    source_id: Optional[str]
    """ID of the source account.

    For a withdrawal or a transfer, this must always be an asset account. For
    deposits, this must be a revenue account.
    """

    source_name: Optional[str]
    """Name of the source account.

    For a withdrawal or a transfer, this must always be an asset account. For
    deposits, this must be a revenue account. Can be used instead of the source_id.
    If the transaction is a deposit, the source_name can be filled in freely: the
    account will be created based on the name.
    """

    tags: Optional[SequenceNotStr[str]]
    """Array of tags."""
