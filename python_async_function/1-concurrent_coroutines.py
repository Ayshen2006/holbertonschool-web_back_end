#!/usr/bin/env python3
"""Execute multiple coroutines concurrently and return sorted delays."""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times concurrently and return delays in ascending order."""
    delays = await asyncio.gather(
        *(wait_random(max_delay) for _ in range(n))
    )
    return sorted(delays)
