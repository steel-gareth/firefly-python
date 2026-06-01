# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountRetrieveParams"]


class AccountRetrieveParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD.

    When added to the request, Firefly III will show the account's balance on that
    day.
    """

    end: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD.

    Must be after "start". Can not be the same as "start". May be omitted.
    """

    start: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD. May be omitted."""

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
