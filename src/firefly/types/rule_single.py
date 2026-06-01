# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .rule_read import RuleRead

__all__ = ["RuleSingle"]


class RuleSingle(BaseModel):
    data: RuleRead
