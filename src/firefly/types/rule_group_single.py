# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .rule_group_read import RuleGroupRead

__all__ = ["RuleGroupSingle"]


class RuleGroupSingle(BaseModel):
    data: RuleGroupRead
