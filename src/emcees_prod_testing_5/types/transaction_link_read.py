# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .object_link import ObjectLink

__all__ = ["TransactionLinkRead", "Attributes"]


class Attributes(BaseModel):
    inward_id: str
    """The inward transaction transaction_journal_id for the link.

    This becomes the 'is paid by' transaction of the set.
    """

    outward_id: str
    """The outward transaction transaction_journal_id for the link.

    This becomes the 'pays for' transaction of the set.
    """

    created_at: Optional[datetime] = None

    notes: Optional[str] = None
    """Optional. Some notes."""

    updated_at: Optional[datetime] = None


class TransactionLinkRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
