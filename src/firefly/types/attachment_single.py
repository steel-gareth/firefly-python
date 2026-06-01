# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .attachment_read import AttachmentRead

__all__ = ["AttachmentSingle"]


class AttachmentSingle(BaseModel):
    data: AttachmentRead
