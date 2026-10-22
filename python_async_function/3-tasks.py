#!/usr/bin/env python3
"""Create asyncio tasks for the wait_random coroutine."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a task that runs wait_random with the specified maximum delay."""
    return asyncio.create_task(wait_random(max_delay))
  
