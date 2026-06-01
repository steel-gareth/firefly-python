# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookTrigger"]

WebhookTrigger: TypeAlias = Literal[
    "ANY",
    "STORE_TRANSACTION",
    "UPDATE_TRANSACTION",
    "DESTROY_TRANSACTION",
    "STORE_BUDGET",
    "UPDATE_BUDGET",
    "DESTROY_BUDGET",
    "STORE_UPDATE_BUDGET_LIMIT",
]
