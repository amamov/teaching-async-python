import aiohttp
import asyncio
from config import get_secret


async def fetch(session, url, i):
    print(i + 1)
    headers = {"X-Naver-Client-Id": get_secret("NAVER_API_ID"), "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET")}
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        print(images)


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1+ i*20}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())
