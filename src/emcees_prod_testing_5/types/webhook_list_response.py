# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .webhook import Webhook
from .._models import BaseModel
from .page_link import PageLink

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    data: List[Webhook]

    links: PageLink

    meta: Meta
