#!/usr/bin/env python3
"""
The basics of  Asynchronous Comprehensions
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    loop 10 times, each time asynchronously wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
