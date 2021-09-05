# 코루틴을 사용하여 스크래핑
# https://github.com/aio-libs/aiohttp
#  pipenv install aiohttp~=3.7.3

import time
import aiohttp
import asyncio
import os
import threading

urls = ["https://instagram.com"] * 100


async def fetch(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls])
        print(results)


start = time.time()
asyncio.run(main())
end = time.time()

print(end - start)
