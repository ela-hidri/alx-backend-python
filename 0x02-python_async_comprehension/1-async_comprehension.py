#!/usr/bin/env python3
"""
The basics of  Asynchronous Comprehensions
"""
import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    collect 10 random numbers using an async comprehensing    """
    randomNbs = []
    async for ran in async_generator():
        randomNbs.append(ran)
    return randomNbs
