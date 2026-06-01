# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["WebhookAttempt", "Attributes"]


class Attributes(BaseModel):
    created_at: Optional[datetime] = None

    logs: Optional[str] = None
    """Internal log for this attempt. May contain sensitive user data."""

    response: Optional[str] = None
    """Webhook receiver response for this attempt, if any.

    May contain sensitive user data.
    """

    status_code: Optional[int] = None
    """The HTTP status code of the error, if any."""

    updated_at: Optional[datetime] = None

    webhook_message_id: Optional[str] = None
    """The ID of the webhook message this attempt belongs to."""


class WebhookAttempt(BaseModel):
    id: str

    attributes: Attributes

    type: str
    """Immutable value"""
