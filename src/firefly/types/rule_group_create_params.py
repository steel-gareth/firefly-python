# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RuleGroupCreateParams"]


class RuleGroupCreateParams(TypedDict, total=False):
    title: Required[str]

    active: bool

    description: Optional[str]

    order: int

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
