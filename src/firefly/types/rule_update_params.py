# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .rule_trigger_type import RuleTriggerType
from .rule_action_keyword import RuleActionKeyword
from .rule_trigger_keyword import RuleTriggerKeyword

__all__ = ["RuleUpdateParams", "Action", "Trigger"]


class RuleUpdateParams(TypedDict, total=False):
    actions: Iterable[Action]

    active: bool
    """Whether or not the rule is even active. Default is true."""

    description: str

    order: int

    rule_group_id: str
    """ID of the rule group under which the rule must be stored.

    Either this field or rule_group_title is mandatory.
    """

    stop_processing: bool
    """
    If this value is true and the rule is triggered, other rules after this one in
    the group will be skipped. Default value is false.
    """

    strict: bool
    """
    If the rule is set to be strict, ALL triggers must hit in order for the rule to
    fire. Otherwise, just one is enough. Default value is true.
    """

    title: str

    trigger: RuleTriggerType
    """
    Which action is necessary for the rule to fire? Use either store-journal,
    update-journal or manual-activation.
    """

    triggers: Iterable[Trigger]

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]


class Action(TypedDict, total=False):
    active: bool
    """If the action is active."""

    order: int
    """Order of the action"""

    stop_processing: bool
    """When true, other actions will not be fired after this action has fired."""

    type: RuleActionKeyword
    """The type of thing this action will do. A limited set is possible."""

    value: Optional[str]
    """The accompanying value the action will set, change or update.

    Can be empty, but for some types this value is mandatory.
    """


class Trigger(TypedDict, total=False):
    active: bool
    """If the trigger is active."""

    order: int
    """Order of the trigger"""

    stop_processing: bool
    """When true, other triggers will not be checked if this trigger was triggered."""

    type: RuleTriggerKeyword
    """The type of thing this trigger responds to. A limited set is possible"""

    value: str
    """The accompanying value the trigger responds to.

    This value is often mandatory, but this depends on the trigger. If the rule
    trigger is something like 'has any tag', submit the string 'true'.
    """
