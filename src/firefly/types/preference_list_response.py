# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .preference_read import PreferenceRead

__all__ = ["PreferenceListResponse"]


class PreferenceListResponse(BaseModel):
    data: List[PreferenceRead]

    links: PageLink

    meta: Meta
