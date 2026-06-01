# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChartDataSet"]


class ChartDataSet(BaseModel):
    currency_code: Optional[str] = None
    """The currency code of the currency associated with this object."""

    currency_decimal_places: Optional[int] = None

    currency_id: Optional[str] = None
    """The currency ID of the currency associated with this object."""

    currency_name: Optional[str] = None
    """The currency name of the currency associated with this object."""

    currency_symbol: Optional[str] = None

    date: Optional[datetime] = None

    end_date: Optional[datetime] = None

    entries: Optional[object] = None
    """The actual entries for this data set.

    They 'key' value is the label for the data point. The value is the actual
    (numerical) value.
    """

    label: Optional[str] = None
    """This is the title of the current set.

    It can refer to an account, a budget or another object (by name).
    """

    pc_entries: Optional[object] = None
    """The actual entries for this data set.

    They 'key' value is the label for the data point. The value is the actual
    (numerical) value.
    """

    period: Optional[Literal["1D", "1W", "1M", "3M", "1Y", "custom"]] = None
    """Period of the chart."""

    primary_currency_code: Optional[str] = None
    """The currency code of the administration's primary currency."""

    primary_currency_decimal_places: Optional[int] = None
    """The currency decimal places of the administration's primary currency."""

    primary_currency_id: Optional[str] = None
    """The currency ID of the administration's primary currency."""

    primary_currency_name: Optional[str] = None
    """The currency name of the administration's primary currency."""

    primary_currency_symbol: Optional[str] = None
    """The currency symbol of the administration's primary currency."""

    start_date: Optional[datetime] = None

    type: Optional[str] = None
    """Indicated the type of chart that is expected to be rendered.

    You can safely ignore this if you want.
    """

    y_axis_id: Optional[int] = FieldInfo(alias="yAxisID", default=None)
    """Used to indicate the Y axis for this data set.

    Is usually between 0 and 1 (left and right side of the chart).
    """
