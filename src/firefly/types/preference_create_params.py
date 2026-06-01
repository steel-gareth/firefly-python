# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .polymorphic_property_param import PolymorphicPropertyParam

__all__ = ["PreferenceCreateParams"]


class PreferenceCreateParams(TypedDict, total=False):
    data: Required[PolymorphicPropertyParam]

    name: Required[str]

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
