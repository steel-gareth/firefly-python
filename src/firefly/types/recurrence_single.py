# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .recurrence_read import RecurrenceRead

__all__ = ["RecurrenceSingle"]


class RecurrenceSingle(BaseModel):
    data: RecurrenceRead
