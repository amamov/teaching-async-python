# 코루틴을 사용하여 스크래핑
# https://github.com/aio-libs/aiohttp
#  pipenv install aiohttp~=3.7.3

import aiohttp
import asyncio
from config import get_secret


async def fetch(session, url):
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        print(result)


async def main():

    apis = [
        "https://openapi.naver.com/v1/search/image?query=cat&display=20&start=1",
    ]
    async with aiohttp.ClientSession() as session:
        awaitables = [fetch(session, api) for api in apis]
        await asyncio.gather(*awaitables)


if __name__ == "__main__":
    asyncio.run(main())
