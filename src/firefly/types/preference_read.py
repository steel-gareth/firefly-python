# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .preference import Preference

__all__ = ["PreferenceRead"]


class PreferenceRead(BaseModel):
    id: str

    attributes: Preference

    type: str
    """Immutable value"""
