#!/usr/bin/env python3
"""0. Async Generator"""

import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Wait 1 second, then yield a random number
    between 0 and 10, 10 times"""
    arr = []
    for _ in range(10):
        arr.append(random.uniform(0, 10))
    for i in arr:
        yield i
        await asyncio.sleep(1)
