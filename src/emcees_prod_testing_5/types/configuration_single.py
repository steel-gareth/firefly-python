# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .configuration import Configuration

__all__ = ["ConfigurationSingle"]


class ConfigurationSingle(BaseModel):
    data: Configuration
