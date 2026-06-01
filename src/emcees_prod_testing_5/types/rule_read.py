# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .object_link import ObjectLink
from .rule_trigger_type import RuleTriggerType
from .rule_action_keyword import RuleActionKeyword
from .rule_trigger_keyword import RuleTriggerKeyword

__all__ = ["RuleRead", "Attributes", "AttributesAction", "AttributesTrigger"]


class AttributesAction(BaseModel):
    type: RuleActionKeyword
    """The type of thing this action will do. A limited set is possible."""

    value: Optional[str] = None
    """The accompanying value the action will set, change or update.

    Can be empty, but for some types this value is mandatory.
    """

    id: Optional[str] = None

    active: Optional[bool] = None
    """If the action is active. Defaults to true."""

    created_at: Optional[datetime] = None

    order: Optional[int] = None
    """Order of the action"""

    stop_processing: Optional[bool] = None
    """When true, other actions will not be fired after this action has fired.

    Defaults to false.
    """

    updated_at: Optional[datetime] = None


class AttributesTrigger(BaseModel):
    type: RuleTriggerKeyword
    """The type of thing this trigger responds to. A limited set is possible"""

    value: str
    """The accompanying value the trigger responds to.

    This value is often mandatory, but this depends on the trigger.
    """

    id: Optional[str] = None

    active: Optional[bool] = None
    """If the trigger is active. Defaults to true."""

    created_at: Optional[datetime] = None

    order: Optional[int] = None
    """Order of the trigger"""

    prohibited: Optional[bool] = None
    """If 'prohibited' is true, this rule trigger will be negated.

    'Description is' will become 'Description is NOT' etc.
    """

    stop_processing: Optional[bool] = None
    """When true, other triggers will not be checked if this trigger was triggered.

    Defaults to false.
    """

    updated_at: Optional[datetime] = None


class Attributes(BaseModel):
    actions: List[AttributesAction]

    rule_group_id: str
    """ID of the rule group under which the rule must be stored.

    Either this field or rule_group_title is mandatory.
    """

    title: str

    trigger: RuleTriggerType
    """
    Which action is necessary for the rule to fire? Use either store-journal,
    update-journal or manual-activation.
    """

    triggers: List[AttributesTrigger]

    active: Optional[bool] = None
    """Whether or not the rule is even active. Default is true."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    order: Optional[int] = None

    rule_group_title: Optional[str] = None
    """Title of the rule group under which the rule must be stored.

    Either this field or rule_group_id is mandatory.
    """

    stop_processing: Optional[bool] = None
    """
    If this value is true and the rule is triggered, other rules after this one in
    the group will be skipped. Default value is false.
    """

    strict: Optional[bool] = None
    """
    If the rule is set to be strict, ALL triggers must hit in order for the rule to
    fire. Otherwise, just one is enough. Default value is true.
    """

    updated_at: Optional[datetime] = None


class RuleRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
