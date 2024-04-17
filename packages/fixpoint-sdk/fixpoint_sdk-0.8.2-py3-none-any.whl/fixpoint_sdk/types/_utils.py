"""Utilities for working with types."""

from dataclasses import fields
from typing import cast, Any, Dict, Optional, TypeVar

from openai._types import NOT_GIVEN, NotGiven


T = TypeVar("T")


def to_dict_without_not_given(obj: Any) -> Dict[str, Any]:
    """Convert a dataclass to a dictionary, excluding fields with the value NOT_GIVEN"""
    result = {}
    for field in fields(obj.__class__):
        value = getattr(obj, field.name)
        if value != NOT_GIVEN and not isinstance(value, NotGiven):
            result[field.name] = value
    return result


def get_value_or_none(value: Optional[T]) -> Optional[T]:
    """If a value is given, return it. Otherwise return None"""
    if is_not_given(value):
        return cast(T, value)
    return None


def is_not_given(value: Any) -> bool:
    """Check if a value's type is not given, versus being defined or set to None"""
    return value == NOT_GIVEN and isinstance(value, NotGiven)
