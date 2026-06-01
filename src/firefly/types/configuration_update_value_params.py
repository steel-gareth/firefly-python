# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .polymorphic_property_param import PolymorphicPropertyParam

__all__ = ["ConfigurationUpdateValueParams"]


class ConfigurationUpdateValueParams(TypedDict, total=False):
    value: Required[PolymorphicPropertyParam]

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
