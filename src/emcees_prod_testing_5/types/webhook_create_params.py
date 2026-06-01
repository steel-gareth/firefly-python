# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .webhook_trigger import WebhookTrigger
from .webhook_delivery import WebhookDelivery
from .webhook_response import WebhookResponse

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    delivery: Required[object]

    response: Required[object]

    title: Required[str]
    """A title for the webhook for easy recognition."""

    trigger: Required[object]

    url: Required[str]
    """The URL of the webhook. Has to start with `https`."""

    active: bool
    """Boolean to indicate if the webhook is active"""

    deliveries: List[WebhookDelivery]

    responses: List[WebhookResponse]

    triggers: List[WebhookTrigger]

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
