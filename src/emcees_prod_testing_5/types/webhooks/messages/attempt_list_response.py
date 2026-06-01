# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...meta import Meta
from ...._models import BaseModel
from .webhook_attempt import WebhookAttempt

__all__ = ["AttemptListResponse"]


class AttemptListResponse(BaseModel):
    data: List[WebhookAttempt]

    meta: Meta
