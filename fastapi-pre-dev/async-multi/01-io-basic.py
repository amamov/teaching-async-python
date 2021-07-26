# 순수하게 웹 스크래핑
# 코루틴을 사용하여 스크래핑
# https://github.com/aio-libs/aiohttp
#  pipenv install aiohttp~=3.7.3

import time
import requests
import os
import threading


def fetch(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com", "https://github.com"] * 100
    with requests.Session() as session:
        [fetch(session, url) for url in urls]
        # results = [fetch(session, url) for url in urls]
        # print(results)


start = time.time()
main()
end = time.time()

print(end - start)
