# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LimitUpdateParams"]


class LimitUpdateParams(TypedDict, total=False):
    id: Required[str]

    amount: str

    currency_code: str
    """The currency code of the currency associated with this object."""

    currency_id: str
    """The currency ID of the currency associated with this object."""

    currency_name: str
    """The currency name of the currency associated with this object."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date of the budget limit."""

    fire_webhooks: bool
    """Whether or not to fire the webhooks that are related to this event."""

    notes: Optional[str]
    """Some notes for this specific budget limit."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start date of the budget limit."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
