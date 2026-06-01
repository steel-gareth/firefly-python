# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountRetrieveOverviewParams"]


class AccountRetrieveOverviewParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    start: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    period: Literal["1D", "1W", "1M", "3M", "6M", "1Y"]
    """Optional period to group the data by.

    If not provided, it will default to '1M' or whatever is deemed relevant for the
    range provided.

    If you want to know which periods are available, see the enums or get the
    configuration value: `GET /api/v1/configuration/firefly.valid_view_ranges`
    """

    preselected: Literal["empty", "all", "assets", "liabilities"]
    """Optional set of preselected accounts to limit the chart to.

    This may be easier than submitting all asset accounts manually, for example. If
    you want to know which selection are available, see the enums here or get the
    configuration value: `GET /api/v1/configuration/firefly.preselected_accounts`

    - `empty`: do not do a pre-selection
    - `all`: select all asset and all liability accounts
    - `assets`: select all asset accounts
    - `liabilities`: select all liability accounts

    If no accounts are found, the user's "frontpage accounts" preference will be
    used. If that is empty, all asset accounts will be used.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
