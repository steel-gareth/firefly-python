# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .attachable_type import AttachableType

__all__ = ["AttachmentCreateParams"]


class AttachmentCreateParams(TypedDict, total=False):
    attachable_id: Required[str]
    """ID of the model this attachment is linked to."""

    attachable_type: Required[AttachableType]
    """The object class to which the attachment must be linked."""

    filename: Required[str]

    notes: Optional[str]

    title: str

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
