# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .rule_read import RuleRead

__all__ = ["RuleArray"]


class RuleArray(BaseModel):
    data: List[RuleRead]

    links: PageLink

    meta: Meta
