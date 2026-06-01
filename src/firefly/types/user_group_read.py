# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .object_link import ObjectLink

__all__ = ["UserGroupRead", "Attributes", "AttributesMember"]


class AttributesMember(BaseModel):
    roles: Optional[
        List[
            Literal[
                "ro",
                "mng_trx",
                "mng_meta",
                "read_budgets",
                "read_piggies",
                "read_subscriptions",
                "read_rules",
                "read_recurring",
                "read_webhooks",
                "read_currencies",
                "mng_budgets",
                "mng_piggies",
                "mng_subscriptions",
                "mng_rules",
                "mng_recurring",
                "mng_webhooks",
                "mng_currencies",
                "view_reports",
                "view_memberships",
                "full",
                "owner",
            ]
        ]
    ] = None

    user_email: Optional[str] = None
    """The email address of the member"""

    user_id: Optional[str] = None
    """The ID of the member."""

    you: Optional[bool] = None
    """Is this you? (the current user)"""


class Attributes(BaseModel):
    can_see_members: Optional[bool] = None
    """Can the current user see the members of this user group?"""

    created_at: Optional[datetime] = None

    in_use: Optional[bool] = None
    """
    Is this user group ('financial administration') currently the active
    administration?
    """

    members: Optional[List[AttributesMember]] = None

    primary_currency_code: Optional[str] = None
    """Returns the primary currency code of the user group."""

    primary_currency_decimal_places: Optional[int] = None
    """Returns the primary currency decimal places of the user group."""

    primary_currency_id: Optional[str] = None
    """Returns the primary currency ID of the user group."""

    primary_currency_symbol: Optional[str] = None
    """Returns the primary currency symbol of the user group."""

    title: Optional[str] = None
    """Title of the user group.

    By default, it is the same as the user's email address.
    """

    updated_at: Optional[datetime] = None


class UserGroupRead(BaseModel):
    id: str

    attributes: Attributes

    links: ObjectLink

    type: str
    """Immutable value"""
