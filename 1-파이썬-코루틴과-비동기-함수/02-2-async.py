import time
import asyncio

# 파이썬에서는 비동기 함수를 코루틴을 사용해서 구현할 수 있습니다.
# 비동기 프로그래밍에 대해서는 언급하지 말자
# 비동기 함수를 사용해서 동시성 프로그래밍이 가능하다.


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")


async def main():
    await asyncio.gather(
        delivery("A", 10),
        delivery("B", 3),
        delivery("C", 4),
    )


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
