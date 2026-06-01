# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .autocomplete_bill import AutocompleteBill

__all__ = ["AutocompleteListSubscriptionsResponse"]

AutocompleteListSubscriptionsResponse: TypeAlias = List[AutocompleteBill]
