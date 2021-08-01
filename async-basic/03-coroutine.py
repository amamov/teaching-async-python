# https://docs.python.org/ko/3/library/asyncio-task.html#running-tasks-concurrently
# https://docs.python.org/3.8/library/asyncio-dev.html

import time
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    result = await asyncio.gather(
        factorial("A", 10),
        factorial("B", 10),
        factorial("C", 10),
    )
    print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main(), debug=True)
    end = time.time()

    print(end - start)


"""
90358 process | 4370365760 thread
Task A: Compute factorial(2), currently i=2...
90358 process | 4370365760 thread
Task B: Compute factorial(3), currently i=2...
90358 process | 4370365760 thread
Task C: Compute factorial(4), currently i=2...
Task A: factorial(2) = 2
Task B: Compute factorial(3), currently i=3...
Task C: Compute factorial(4), currently i=3...
Task B: factorial(3) = 6
Task C: Compute factorial(4), currently i=4...
Task C: factorial(4) = 24
[2, 6, 24]
3.01682186126709
"""
