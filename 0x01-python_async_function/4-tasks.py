#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times
    """
    delays_done = []
    for i in range(n):
        tasks = task_wait_random(max_delay)
        delays_done.append(tasks)
    delays_done = asyncio.as_completed(delays_done)
    delays = [await delay for delay in delays_done]
    return delays
