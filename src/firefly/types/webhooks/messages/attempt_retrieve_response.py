# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .webhook_attempt import WebhookAttempt

__all__ = ["AttemptRetrieveResponse"]


class AttemptRetrieveResponse(BaseModel):
    data: WebhookAttempt
