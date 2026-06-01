# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .piggy_bank_read import PiggyBankRead

__all__ = ["PiggyBankSingle"]


class PiggyBankSingle(BaseModel):
    data: PiggyBankRead
