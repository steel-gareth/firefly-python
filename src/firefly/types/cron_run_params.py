# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CronRunParams"]


class CronRunParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A date formatted YYYY-MM-DD.

    This can be used to make the cron job pretend it's running on another day.
    """

    force: bool
    """Forces the cron job to fire, regardless of whether it has fired before.

    This may result in double transactions or weird budgets, so be careful.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
