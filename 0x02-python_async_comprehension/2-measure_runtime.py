#!/usr/bin/env python3
"""
The basics of  Asynchronous Comprehensions
"""
import asyncio
import random
from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime
    """
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time.time()
    total_time = end - start
    return total_time
