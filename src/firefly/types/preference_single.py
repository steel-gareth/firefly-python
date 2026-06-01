# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .preference_read import PreferenceRead

__all__ = ["PreferenceSingle"]


class PreferenceSingle(BaseModel):
    data: PreferenceRead
