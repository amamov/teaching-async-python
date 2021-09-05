import time
import os
import threading

nums = [87, 78, 56, 43]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 0
    for i in numbers:
        for j in numbers:
            for k in numbers:
                for h in numbers:
                    total *= i * j * k * h


def main():
    for num in nums:
        cpu_bound_func(num)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)


"""
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
92760 process | 4344888640 thread
16.812243223190308
"""
