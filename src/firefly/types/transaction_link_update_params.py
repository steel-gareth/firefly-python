# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionLinkUpdateParams"]


class TransactionLinkUpdateParams(TypedDict, total=False):
    inward_id: str
    """The inward transaction transaction_journal_id for the link.

    This becomes the 'is paid by' transaction of the set.
    """

    link_type_id: str
    """The link type ID to use. Use this field OR use the link_type_name field."""

    link_type_name: str
    """The link type name to use. Use this field OR use the link_type_id field."""

    notes: Optional[str]
    """Optional.

    Some notes. If you submit an empty string the current notes will be removed
    """

    outward_id: str
    """The outward transaction transaction_journal_id for the link.

    This becomes the 'pays for' transaction of the set.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
