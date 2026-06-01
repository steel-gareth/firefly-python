# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..meta import Meta
from ..._models import BaseModel
from .webhook_message import WebhookMessage

__all__ = ["MessageListResponse"]


class MessageListResponse(BaseModel):
    data: List[WebhookMessage]

    meta: Meta
