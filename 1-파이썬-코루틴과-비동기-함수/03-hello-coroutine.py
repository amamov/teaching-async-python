# 코루틴 hello world!
# https://docs.python.org/ko/3/library/asyncio-task.html

import asyncio


async def hello_world():
    print("hello world")
    return 123


if __name__ == "__main__":
    asyncio.run(hello_world())
