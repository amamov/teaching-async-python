# https://docs.python.org/ko/3/library/asyncio-task.html#coroutines
# https://2.python-requests.org/en/master/user/advanced/#id1

import requests
import time


def fetcher(session, url):
    response = session.get(url)
    return response.text


def main():
    urls = ["https://google.com", "https://instagram.com", "https://facebook.com"] * 30

    with requests.Session() as session:
        results = [fetcher(session, url) for url in urls]
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 51.15794801712036
