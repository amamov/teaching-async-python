# 코루틴을 사용하여 스크래핑
# https://github.com/aio-libs/aiohttp
#  pipenv install aiohttp~=3.7.3

import aiohttp
import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


async def fetch(session, url):
    async with session.get(url) as response:
        # await asyncio.sleep(3)
        html = await response.text()
        soup = BeautifulSoup(html, features="html.parser")
        img_list = soup.find_all("img")
        print(img_list)


async def main():

    urls = [
        "http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&Wcode=001_005&query=%b0%ed%be%e7%c0%cc&domain=ALL&page_size=120",
        "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=%EA%B3%A0%EC%96%91%EC%9D%B4&x=0&y=0",
    ]

    headers = {
        "User-Agent": UserAgent().chrome,
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        awaitables = [fetch(session, url) for url in urls]
        await asyncio.gather(*awaitables)


if __name__ == "__main__":
    asyncio.run(main())
