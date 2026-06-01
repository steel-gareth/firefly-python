# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookSingle"]


class WebhookSingle(BaseModel):
    data: Webhook
