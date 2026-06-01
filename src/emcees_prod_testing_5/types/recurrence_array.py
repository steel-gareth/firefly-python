# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .recurrence_read import RecurrenceRead

__all__ = ["RecurrenceArray"]


class RecurrenceArray(BaseModel):
    data: List[RecurrenceRead]

    links: PageLink

    meta: Meta
