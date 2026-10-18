#!/usr/bin/env python3
"""Create a function that multiplies a number by a given multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(number: float) -> float:
        """Return the product of a number and the multiplier."""
        return number * multiplier

    return multiply
