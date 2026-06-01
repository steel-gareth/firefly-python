# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .webhook_message import WebhookMessage

__all__ = ["MessageRetrieveResponse"]


class MessageRetrieveResponse(BaseModel):
    data: WebhookMessage
