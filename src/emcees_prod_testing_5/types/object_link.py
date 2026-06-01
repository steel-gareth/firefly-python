# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ObjectLink", "_0"]


class _0(BaseModel):
    rel: Optional[str] = None

    uri: Optional[str] = None


class ObjectLink(BaseModel):
    api_0: Optional[_0] = FieldInfo(alias="0", default=None)

    self: Optional[str] = None
