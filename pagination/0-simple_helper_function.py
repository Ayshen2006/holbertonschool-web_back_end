#!/usr/bin/env python3
"""This module provides a helper function for pagination index ranges."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes corresponding to a pagination page.

    Args:
        page: The page number, starting from 1.
        page_size: The number of items per page.

    Returns:
        A tuple containing the start index (inclusive) and
        the end index (exclusive).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
