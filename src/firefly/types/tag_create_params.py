# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TagCreateParams"]


class TagCreateParams(TypedDict, total=False):
    tag: Required[str]
    """The tag"""

    date: Annotated[Union[str, datetime.date, None], PropertyInfo(format="iso8601")]
    """The date to which the tag is applicable."""

    description: Optional[str]

    latitude: Optional[float]
    """Latitude of the tag's location, if applicable. Can be used to draw a map."""

    longitude: Optional[float]
    """Latitude of the tag's location, if applicable. Can be used to draw a map."""

    zoom_level: Optional[int]
    """Zoom level for the map, if drawn.

    This to set the box right. Unfortunately this is a proprietary value because
    each map provider has different zoom levels.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
