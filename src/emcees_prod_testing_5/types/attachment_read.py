# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .object_link import ObjectLink
from .attachable_type import AttachableType

__all__ = ["AttachmentRead", "Attributes"]


class Attributes(BaseModel):
    attachable_id: Optional[str] = None
    """ID of the model this attachment is linked to."""

    attachable_type: Optional[AttachableType] = None
    """The object class to which the attachment must be linked."""

    created_at: Optional[datetime] = None

    download_url: Optional[str] = None

    filename: Optional[str] = None

    hash: Optional[str] = None
    """Hash of the file for basic duplicate detection."""

    mime: Optional[str] = None

    notes: Optional[str] = None

    size: Optional[int] = None

    title: Optional[str] = None

    updated_at: Optional[datetime] = None

    upload_url: Optional[str] = None


class AttachmentRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
