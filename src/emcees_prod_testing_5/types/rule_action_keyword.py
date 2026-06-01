# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RuleActionKeyword"]

RuleActionKeyword: TypeAlias = Literal[
    "user_action",
    "set_category",
    "clear_category",
    "set_budget",
    "clear_budget",
    "add_tag",
    "remove_tag",
    "remove_all_tags",
    "set_description",
    "append_description",
    "prepend_description",
    "set_source_account",
    "set_destination_account",
    "set_notes",
    "append_notes",
    "prepend_notes",
    "clear_notes",
    "link_to_bill",
    "convert_withdrawal",
    "convert_deposit",
    "convert_transfer",
    "delete_transaction",
]
