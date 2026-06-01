# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .link_type import LinkType
from .object_link import ObjectLink

__all__ = ["LinkTypeRead"]


class LinkTypeRead(BaseModel):
    id: str

    attributes: LinkType

    links: ObjectLink

    type: str
    """Immutable value"""
