import time
import asyncio
import os
import threading
from concurrent.futures import ProcessPoolExecutor

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
    executor = ProcessPoolExecutor(max_workers=10)
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
89126 process | 4382276928 thread
89126 process | 4382276928 thread
89124 process | 4302224704 thread
89124 process | 4302224704 thread
89127 process | 4375199040 thread
89127 process | 4375199040 thread
89125 process | 4369153344 thread
89125 process | 4369153344 thread
89128 process | 4304223552 thread
89128 process | 4304223552 thread
4.156450986862183
"""
