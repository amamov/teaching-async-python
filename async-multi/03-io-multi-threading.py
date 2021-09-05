# 순수하게 웹 스크래핑
# 코루틴을 사용하여 스크래핑
# https://github.com/aio-libs/aiohttp
#  pipenv install aiohttp~=3.7.3

import time
import requests
import os
import threading
from concurrent.futures import ThreadPoolExecutor

urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 100


def fetch(args):
    session = args[0]
    url = args[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        print("hello world")
        return response.text


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    with requests.Session() as session:
        params = [(session, url) for url in urls]
        results = list(executor.map(fetch, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

# 27
