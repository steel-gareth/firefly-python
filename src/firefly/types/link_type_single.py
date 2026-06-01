# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .link_type_read import LinkTypeRead

__all__ = ["LinkTypeSingle"]


class LinkTypeSingle(BaseModel):
    data: LinkTypeRead
