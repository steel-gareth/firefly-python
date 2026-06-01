# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RuleGroupTriggerRulesParams"]


class RuleGroupTriggerRulesParams(TypedDict, total=False):
    accounts: Iterable[int]
    """Limit the triggering of the rule group to these asset accounts or liabilities.

    Only asset accounts and liabilities will be accepted. Other types will be
    silently dropped.
    """

    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    A date formatted YYYY-MM-DD, to limit the transactions the actions will be
    applied to. Both the start date and the end date must be present.
    """

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    A date formatted YYYY-MM-DD, to limit the transactions the actions will be
    applied to. Both the start date and the end date must be present.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
