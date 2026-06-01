# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from .._models import BaseModel
from .page_link import PageLink
from .rule_group_read import RuleGroupRead

__all__ = ["RuleGroupListAllResponse"]


class RuleGroupListAllResponse(BaseModel):
    data: List[RuleGroupRead]

    links: PageLink

    meta: Meta
