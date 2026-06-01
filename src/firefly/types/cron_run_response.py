# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .cron_result_row import CronResultRow

__all__ = ["CronRunResponse"]


class CronRunResponse(BaseModel):
    auto_budgets: Optional[CronResultRow] = None

    recurring_transactions: Optional[CronResultRow] = None

    telemetry: Optional[CronResultRow] = None
