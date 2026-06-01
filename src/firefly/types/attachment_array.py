# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .attachment_read import AttachmentRead

__all__ = ["AttachmentArray"]


class AttachmentArray(BaseModel):
    data: List[AttachmentRead]

    meta: Meta
