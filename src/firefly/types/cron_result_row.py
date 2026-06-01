# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CronResultRow"]


class CronResultRow(BaseModel):
    job_errored: Optional[bool] = None
    """If the cron job ran into some kind of an error, this value will be true."""

    job_fired: Optional[bool] = None
    """This value tells you if this specific cron job actually fired.

    It may not fire. Some cron jobs only fire every 24 hours, for example.
    """

    job_succeeded: Optional[bool] = None
    """This value tells you if this specific cron job actually did something.

    The job may fire but not change anything.
    """

    message: Optional[str] = None
    """
    If the cron job ran into some kind of an error, this value will be the error
    message. The success message if the job actually ran OK.
    """
