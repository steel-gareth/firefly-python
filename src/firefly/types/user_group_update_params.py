# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserGroupUpdateParams"]


class UserGroupUpdateParams(TypedDict, total=False):
    title: Required[str]
    """A descriptive title for the user group."""

    primary_currency_code: str
    """Use either primary_currency_id or primary_currency_code.

    This will set the primary currency for the user group ('financial
    administration').
    """

    primary_currency_id: str
    """Use either primary_currency_id or primary_currency_code.

    This will set the primary currency for the user group ('financial
    administration').
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
