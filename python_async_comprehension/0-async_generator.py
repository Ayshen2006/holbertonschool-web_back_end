#!/usr/bin/env python3
"""Generate random numbers asynchronously."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield ten random numbers, waiting one second before each number."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
