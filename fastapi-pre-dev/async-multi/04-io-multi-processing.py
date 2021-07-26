# 순수하게 웹 스크래핑
# 코루틴을 사용하여 스크래핑
# https://github.com/aio-libs/aiohttp
#  pipenv install aiohttp~=3.7.3

import time
import requests
import os
import threading
import asyncio
from concurrent.futures import ProcessPoolExecutor


def fetch(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    with session.get(url) as response:
        return response.text


async def main():
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor(max_workers=10)
    urls = ["https://google.com", "https://apple.com", "https://github.com"] * 100
    with requests.Session() as session:
        awaitables = [loop.run_in_executor(executor, fetch, session, url) for url in urls]
        await asyncio.gather(*awaitables)
        # print(results)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)


# 13.471907138824463
