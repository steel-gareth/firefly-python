# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .export_file_filter import ExportFileFilter

__all__ = ["ExportExportRecurringParams"]


class ExportExportRecurringParams(TypedDict, total=False):
    type: ExportFileFilter

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
