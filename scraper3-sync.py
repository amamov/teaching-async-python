import requests
import time
from config import get_secret


class PhotoScraper:

    NAVER_API_PHOTO = "https://openapi.naver.com/v1/search/image"
    KAKAO_API_PHOTO = "https://dapi.kakao.com/v2/search/image"
    NAVER_API_ID = get_secret("NAVER_API_ID")
    NAVER_API_SECRET = get_secret("NAVER_API_SECRET")
    KAKAO_API_ID = get_secret("KAKAO_API_ID")

    def __init__(self):
        pass

    def fetch(self, session, url, headers):
        with session.get(url, headers=headers) as response:
            if response.ok:
                return response.json()

    def unit_api(self, keyword: str, page: str, size: int):
        return [
            {
                "name": "naver",
                "url": f"{self.NAVER_API_PHOTO}?query={keyword}&display={size}&start={page}",
                "headers": {
                    "X-Naver-Client-Id": self.NAVER_API_ID,
                    "X-Naver-Client-Secret": self.NAVER_API_SECRET,
                },
            },
            {
                "name": "kakao",
                "url": f"{self.KAKAO_API_PHOTO}?query={keyword}&page={page}&size={size}",
                "headers": {"Authorization": f"KakaoAK {self.KAKAO_API_ID}"},
            },
        ]

    def search(self, keyword: str, total_page: int = 10, size: int = 10):

        apis = []

        for per_page in range(1, total_page):
            apis += self.unit_api(keyword, per_page, size)

        # print(apis)

        with requests.Session() as session:
            result = [self.fetch(session, api["url"], api["headers"]) for api in apis]
            print(result)
            print(len(apis))

    def run(self, keyword: str, total_page: int, size: int = 10):

        self.search(keyword, total_page, size)


if __name__ == "__main__":
    start = time.time()
    scraper = PhotoScraper()
    scraper.run("joy", 100, 10)
    end = time.time()
    print(end - start)
