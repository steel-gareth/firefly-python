# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypeAlias

from .._types import SequenceNotStr

__all__ = ["PolymorphicPropertyParam"]

PolymorphicPropertyParam: TypeAlias = Union[bool, str, Dict[str, object], SequenceNotStr[str]]
