# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttachmentUpdateParams"]


class AttachmentUpdateParams(TypedDict, total=False):
    filename: str

    notes: Optional[str]

    title: str

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
