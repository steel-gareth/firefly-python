# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .config_value_filter import ConfigValueFilter
from .polymorphic_property import PolymorphicProperty

__all__ = ["Configuration"]


class Configuration(BaseModel):
    editable: bool
    """If this config variable can be edited by the user"""

    title: ConfigValueFilter
    """Title of the configuration value."""

    value: PolymorphicProperty
