# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RuleGroupTestTransactionsParams"]


class RuleGroupTestTransactionsParams(TypedDict, total=False):
    accounts: Iterable[int]
    """Limit the testing of the rule group to these asset accounts or liabilities.

    Only asset accounts and liabilities will be accepted. Other types will be
    silently dropped.
    """

    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
    to. Both the start date and the end date must be present.
    """

    limit: int
    """Number of items per page. The default pagination is per 50 items."""

    page: int
    """Page number. The default pagination is per 50 items."""

    search_limit: int
    """Maximum number of transactions Firefly III will try.

    Don't set this too high, or it will take Firefly III very long to run the test.
    I suggest a max of 200.
    """

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    A date formatted YYYY-MM-DD, to limit the transactions the test will be applied
    to. Both the start date and the end date must be present.
    """

    triggered_limit: int
    """
    Maximum number of transactions the rule group can actually trigger on, before
    Firefly III stops. I would suggest setting this to 10 or 15. Don't go above the
    user's page size, because browsing to page 2 or 3 of a test result would fire
    the test again, making any navigation efforts very slow.
    """

    x_trace_id: Annotated[str, PropertyInfo(alias="X-Trace-Id")]
