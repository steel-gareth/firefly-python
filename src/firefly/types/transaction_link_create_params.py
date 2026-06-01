# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionLinkCreateParams"]


class TransactionLinkCreateParams(TypedDict, total=False):
    inward_id: Required[str]
    """The inward transaction transaction_journal_id for the link.

    This becomes the 'is paid by' transaction of the set.
    """

    link_type_id: Required[str]
    """The link type ID to use. You can also use the link_type_name field."""

    outward_id: Required[str]
    """The outward transaction transaction_journal_id for the link.

    This becomes the 'pays for' transaction of the set.
    """

    link_type_name: str
    """The link type name to use. You can also use the link_type_id field."""

    notes: Optional[str]
    """Optional. Some notes."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
