import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor

nums = [87, 78, 56, 43] * 5


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1, num)
    total = 0
    for i in numbers:
        for j in numbers:
            for k in numbers:
                for h in numbers:
                    total *= i * j * k * h


def main():
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

"""
4.156450986862183
"""
