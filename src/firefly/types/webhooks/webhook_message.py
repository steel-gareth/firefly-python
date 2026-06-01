# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WebhookMessage", "Attributes"]


class Attributes(BaseModel):
    created_at: Optional[datetime] = None

    errored: Optional[bool] = None
    """If this message has errored out."""

    message: Optional[str] = None
    """The actual message that is sent or will be sent as JSON string."""

    sent: Optional[bool] = None
    """If this message is sent yet."""

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None
    """Long UUID string for identification of this webhook message."""

    webhook_id: Optional[str] = None
    """The ID of the webhook this message belongs to."""


class WebhookMessage(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
