# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .export_file_filter import ExportFileFilter

__all__ = ["ExportExportTransactionsParams"]


class ExportExportTransactionsParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    start: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date formatted YYYY-MM-DD."""

    accounts: str
    """Limit the export of transactions to these accounts only.

    Only asset accounts will be accepted. Other types will be silently dropped.
    """

    type: ExportFileFilter

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
