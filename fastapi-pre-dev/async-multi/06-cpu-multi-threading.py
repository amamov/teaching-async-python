import time
import asyncio
import os
import threading
from concurrent.futures import ThreadPoolExecutor

nums = [(23784929, 23784923), (63784924, 93784913)] * 5


def gcd(nums):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    num1, num2 = nums
    min_num = min(num1, num2)
    for idx in range(min_num, 0, -1):
        if num1 % idx and num2 % idx == 0:
            return idx


async def main():
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(max_workers=10)
    loops = []
    for num in nums:
        loops.append(loop.run_in_executor(executor, gcd, num))

    await asyncio.gather(*loops)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)

"""
92693 process | 6110441472 thread
92693 process | 6127267840 thread
92693 process | 6144094208 thread
92693 process | 6110441472 thread
92693 process | 6177746944 thread
92693 process | 6194573312 thread
92693 process | 6144094208 thread
92693 process | 6228226048 thread
92693 process | 6160920576 thread
92693 process | 6211399680 thread
16.04899787902832
"""
