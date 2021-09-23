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
        await asyncio.gather(*[fetch(session, api) for api in apis])


if __name__ == "__main__":
    asyncio.run(main())
