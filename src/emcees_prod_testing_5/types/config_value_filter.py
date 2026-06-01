# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ConfigValueFilter"]

ConfigValueFilter: TypeAlias = Literal[
    "configuration.is_demo_site",
    "configuration.permission_update_check",
    "configuration.last_update_check",
    "configuration.single_user_mode",
    "firefly.version",
    "firefly.default_location",
    "firefly.account_to_transaction",
    "firefly.allowed_opposing_types",
    "firefly.accountRoles",
    "firefly.valid_liabilities",
    "firefly.interest_periods",
    "firefly.enable_external_map",
    "firefly.expected_source_types",
    "app.timezone",
    "firefly.bill_periods",
    "firefly.credit_card_types",
    "firefly.languages",
    "firefly.valid_view_ranges",
    "cer.enabled",
    "firefly.preselected_accounts",
    "firefly.rule-actions",
    "firefly.context-rule-actions",
    "search.operators",
    "webhook.triggers",
    "webhook.responses",
    "webhook.deliveries",
]
