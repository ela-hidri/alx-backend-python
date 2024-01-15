#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times
    """
    delays_done = []
    for i in range(n):
        delay = wait_random(max_delay)
        delays_done.append(delay)
    delays_done = asyncio.as_completed(delays_done)
    delays = [await delay for delay in delays_done]
    return delays
