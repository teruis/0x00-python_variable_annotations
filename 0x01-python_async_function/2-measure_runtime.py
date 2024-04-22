#!/usr/bin/env python3
""" The basics of async """
   
import asyncio
import random
from typing import List

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)

if __name__ == "__main__":
    import asyncio
    
    wait_n = __import__('1-concurrent_coroutines').wait_n

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))

