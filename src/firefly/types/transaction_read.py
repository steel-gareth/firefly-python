# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .object_link import ObjectLink
from .account_type_property import AccountTypeProperty
from .transaction_type_property import TransactionTypeProperty

__all__ = ["TransactionRead", "Attributes", "AttributesTransaction"]


class AttributesTransaction(BaseModel):
    amount: str
    """Amount of the transaction."""

    date: datetime
    """Date of the transaction"""

    description: str
    """Description of the transaction."""

    destination_id: Optional[str] = None
    """ID of the destination account.

    For a deposit or a transfer, this must always be an asset account. For
    withdrawals this must be an expense account.
    """

    source_id: Optional[str] = None
    """ID of the source account.

    For a withdrawal or a transfer, this must always be an asset account. For
    deposits, this must be a revenue account.
    """

    type: TransactionTypeProperty

    bill_id: Optional[str] = None
    """The associated subscription ID for this transaction.

    `bill` refers to the OLD name for subscriptions and this field will be removed.
    """

    bill_name: Optional[str] = None
    """The associated subscription name for this transaction.

    `bill` refers to the OLD name for subscriptions and this field will be removed.
    """

    book_date: Optional[datetime] = None

    budget_id: Optional[str] = None
    """The budget ID for this transaction."""

    budget_name: Optional[str] = None
    """The name of the budget used."""

    category_id: Optional[str] = None
    """The category ID for this transaction."""

    category_name: Optional[str] = None
    """The name of the category to be used.

    If the category is unknown, it will be created. If the ID and the name point to
    different categories, the ID overrules the name.
    """

    currency_code: Optional[str] = None
    """Currency code for the currency of this transaction."""

    currency_decimal_places: Optional[int] = None
    """Number of decimals used in this currency."""

    currency_id: Optional[str] = None
    """Currency ID for the currency of this transaction."""

    currency_name: Optional[str] = None
    """Currency name for the currency of this transaction."""

    currency_symbol: Optional[str] = None
    """Currency symbol for the currency of this transaction."""

    destination_balance_after: Optional[str] = None
    """The balance of the destination account.

    This is the balance in the account's currency which may be different from this
    transaction, and is not provided in this model.
    """

    destination_iban: Optional[str] = None

    destination_name: Optional[str] = None
    """Name of the destination account.

    You can submit the name instead of the ID. For everything except transfers, the
    account will be auto-generated if unknown, so submitting a name is enough.
    """

    destination_type: Optional[AccountTypeProperty] = None

    due_date: Optional[datetime] = None

    external_id: Optional[str] = None
    """Reference to external ID in other systems."""

    external_url: Optional[str] = None
    """External, custom URL for this transaction."""

    foreign_amount: Optional[str] = None
    """The amount in the set foreign currency.

    May be NULL if the transaction does not have a foreign amount.
    """

    foreign_currency_code: Optional[str] = None
    """Currency code of the foreign currency. Default is NULL."""

    foreign_currency_decimal_places: Optional[int] = None
    """Number of decimals in the foreign currency."""

    foreign_currency_id: Optional[str] = None
    """Currency ID of the foreign currency, if this transaction has a foreign amount."""

    foreign_currency_symbol: Optional[str] = None

    has_attachments: Optional[bool] = None
    """If the transaction has attachments."""

    import_hash_v2: Optional[str] = None
    """Hash value of original import transaction (for duplicate detection)."""

    interest_date: Optional[datetime] = None

    internal_reference: Optional[str] = None
    """Reference to internal reference of other systems."""

    invoice_date: Optional[datetime] = None

    latitude: Optional[float] = None
    """Latitude of the transaction's location, if applicable.

    Can be used to draw a map.
    """

    longitude: Optional[float] = None
    """Latitude of the transaction's location, if applicable.

    Can be used to draw a map.
    """

    notes: Optional[str] = None

    object_has_currency_setting: Optional[bool] = None
    """Indicates whether the transaction has a currency setting.

    For transactions this is always true.
    """

    order: Optional[int] = None
    """Order of this entry in the list of transactions."""

    original_source: Optional[str] = None
    """System generated identifier for original creator of transaction."""

    payment_date: Optional[datetime] = None

    pc_amount: Optional[str] = None
    """Amount of the transaction in the primary currency of this administration.

    The `primary_currency_*` fields reflect the currency used. This field is NULL if
    the user does have 'convert to primary' set to true in their settings.
    """

    pc_destination_balance_after: Optional[str] = None
    """
    The balance of the destination account in the primary currency of this
    administration. The `primary_currency_*` fields reflect the currency used. This
    field is NULL if the user does have 'convert to primary' set to true in their
    settings.
    """

    pc_foreign_amount: Optional[str] = None
    """Foreign amount of the transaction in the primary currency of this
    administration.

    The `primary_currency_*` fields reflect the currency used. This field is NULL if
    the user does have 'convert to primary' set to true in their settings.
    """

    pc_source_balance_after: Optional[str] = None
    """The balance of the source account in the primary currency of this
    administration.

    The `primary_currency_*` fields reflect the currency used. This field is NULL if
    the user does have 'convert to primary' set to true in their settings.
    """

    primary_currency_code: Optional[str] = None
    """Returns the primary currency code of the administration.

    This currency is used as the currency for all `pc_*` amount and balance fields
    of this account.
    """

    primary_currency_decimal_places: Optional[int] = None
    """See the other `primary_*` fields."""

    primary_currency_id: Optional[str] = None
    """Returns the primary currency ID of the administration.

    This currency is used as the currency for all `pc_*` amount and balance fields
    of this account.
    """

    primary_currency_symbol: Optional[str] = None
    """See the other `primary_*` fields."""

    process_date: Optional[datetime] = None

    reconciled: Optional[bool] = None
    """If the transaction has been reconciled already.

    When you set this, the amount can no longer be edited by the user.
    """

    recurrence_count: Optional[int] = None
    """The # of the current transaction created under this recurrence."""

    recurrence_id: Optional[str] = None
    """Reference to recurrence that made the transaction."""

    recurrence_total: Optional[int] = None
    """
    Total number of transactions expected to be created by this recurrence
    repetition. Will be 0 if infinite.
    """

    sepa_batch_id: Optional[str] = None
    """SEPA Batch ID"""

    sepa_cc: Optional[str] = None
    """SEPA Clearing Code"""

    sepa_ci: Optional[str] = None
    """SEPA Creditor Identifier"""

    sepa_country: Optional[str] = None
    """SEPA Country"""

    sepa_ct_id: Optional[str] = None
    """SEPA end-to-end Identifier"""

    sepa_ct_op: Optional[str] = None
    """SEPA Opposing Account Identifier"""

    sepa_db: Optional[str] = None
    """SEPA mandate identifier"""

    sepa_ep: Optional[str] = None
    """SEPA External Purpose indicator"""

    source_balance_after: Optional[str] = None
    """The balance of the source account.

    This is the balance in the account's currency which may be different from this
    transaction, and is not provided in this model.
    """

    source_iban: Optional[str] = None

    source_name: Optional[str] = None
    """Name of the source account.

    For a withdrawal or a transfer, this must always be an asset account. For
    deposits, this must be a revenue account. Can be used instead of the source_id.
    If the transaction is a deposit, the source_name can be filled in freely: the
    account will be created based on the name.
    """

    source_type: Optional[AccountTypeProperty] = None

    subscription_id: Optional[str] = None
    """The associated subscription ID for this transaction."""

    subscription_name: Optional[str] = None
    """The associated subscription name for this transaction."""

    tags: Optional[List[str]] = None
    """Array of tags."""

    transaction_journal_id: Optional[str] = None
    """ID of the underlying transaction journal.

    Each transaction consists of a transaction group (see the top ID) and one or
    more journals making up the splits of the transaction.
    """

    user: Optional[str] = None
    """User ID"""

    zoom_level: Optional[int] = None
    """Zoom level for the map, if drawn.

    This to set the box right. Unfortunately this is a proprietary value because
    each map provider has different zoom levels.
    """


class Attributes(BaseModel):
    transactions: List[AttributesTransaction]

    created_at: Optional[datetime] = None

    group_title: Optional[str] = None
    """Title of the transaction if it has been split in more than one piece.

    Empty otherwise.
    """

    updated_at: Optional[datetime] = None

    user: Optional[str] = None
    """User ID"""


class TransactionRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
