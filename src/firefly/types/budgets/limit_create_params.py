# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LimitCreateParams"]


class LimitCreateParams(TypedDict, total=False):
    amount: Required[str]

    end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """End date of the budget limit."""

    start: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Start date of the budget limit."""

    currency_code: str
    """Use either currency_id or currency_code.

    Defaults to the user's primary currency.
    """

    currency_id: str
    """Use either currency_id or currency_code.

    Defaults to the user's primary currency.
    """

    fire_webhooks: bool
    """Whether or not to fire the webhooks that are related to this event."""

    notes: Optional[str]
    """Some notes for this specific budget limit."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
