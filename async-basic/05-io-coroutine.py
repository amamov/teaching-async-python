# 코루틴을 사용하여 스크래핑
# https://github.com/aio-libs/aiohttp
#  pipenv install aiohttp~=3.7.3
import time
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://google.com", "https://apple.com", "https://github.com"] * 100
    async with aiohttp.ClientSession() as session:
        awaitables = [fetch(session, url) for url in urls]
        await asyncio.gather(*awaitables)
        # htmls = await asyncio.gather(*awaitables)
        # print(htmls)


start = time.time()
asyncio.run(main())
end = time.time()

print(end - start)
