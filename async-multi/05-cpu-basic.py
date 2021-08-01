import time
import os
import threading

nums = [(23784929, 23784923), (63784924, 93784913)] * 5


def gcd(nums):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    num1, num2 = nums
    min_num = min(num1, num2)
    for idx in range(min_num, 0, -1):
        if num1 % idx and num2 % idx == 0:
            return idx


def main():
    for num in nums:
        gcd(num)


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
