# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AboutRetrieveInfoResponse", "Data"]


class Data(BaseModel):
    api_version: Optional[str] = None
    """Same value as the version field."""

    driver: Optional[str] = None

    os: Optional[str] = None

    php_version: Optional[str] = None

    version: Optional[str] = None


class AboutRetrieveInfoResponse(BaseModel):
    data: Optional[Data] = None
