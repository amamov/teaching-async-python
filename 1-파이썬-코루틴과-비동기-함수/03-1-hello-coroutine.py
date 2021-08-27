# 코루틴 hello world!
# https://docs.python.org/ko/3/library/asyncio-task.html


import asyncio


async def hello_world():  # 코루틴 함수
    print("Hello World!")


if __name__ == "__main__":
    asyncio.run(hello_world())  # hello world!
