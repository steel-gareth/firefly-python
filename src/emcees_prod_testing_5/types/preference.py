# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .polymorphic_property import PolymorphicProperty

__all__ = ["Preference"]


class Preference(BaseModel):
    data: PolymorphicProperty

    name: str

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None
