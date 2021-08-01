# https://docs.python.org/ko/3/library/asyncio-task.html#running-tasks-concurrently


import time


def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        time.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


def main():
    # Schedule three calls *concurrently*:
    result = [factorial("A", 2), factorial("B", 3), factorial("C", 4)]
    print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

"""
90318 process | 4344642880 thread
Task A: Compute factorial(2), currently i=2...
Task A: factorial(2) = 2
90318 process | 4344642880 thread
Task B: Compute factorial(3), currently i=2...
Task B: Compute factorial(3), currently i=3...
Task B: factorial(3) = 6
90318 process | 4344642880 thread
Task C: Compute factorial(4), currently i=2...
Task C: Compute factorial(4), currently i=3...
Task C: Compute factorial(4), currently i=4...
Task C: factorial(4) = 24
[2, 6, 24]
6.02688193321228
"""
