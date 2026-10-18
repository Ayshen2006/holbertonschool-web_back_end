#!/usr/bin/env python3
"""Create a tuple containing a string and the square of a number."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a key and the square of its numeric value."""
    return (k, float(v ** 2))
