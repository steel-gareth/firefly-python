# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from .._models import BaseModel
from .object_link import ObjectLink

__all__ = ["TagRead", "Attributes"]


class Attributes(BaseModel):
    tag: str
    """The tag"""

    created_at: Optional[datetime.datetime] = None

    date: Optional[datetime.date] = None
    """The date to which the tag is applicable."""

    description: Optional[str] = None

    latitude: Optional[float] = None
    """Latitude of the tag's location, if applicable. Can be used to draw a map."""

    longitude: Optional[float] = None
    """Latitude of the tag's location, if applicable. Can be used to draw a map."""

    updated_at: Optional[datetime.datetime] = None

    zoom_level: Optional[int] = None
    """Zoom level for the map, if drawn.

    This to set the box right. Unfortunately this is a proprietary value because
    each map provider has different zoom levels.
    """


class TagRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
