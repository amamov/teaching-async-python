# https://docs.python.org/3.2/library/inspect.html#current-state-of-a-generator

# 코루틴의 원리 : 제너레이터를 확장한

# yield : 코루틴 제어, 메인 루틴과 양방향 데이터 전송
# 코루틴은 기본적으로 싱글스레드에서 수행이되고


def co1():
    print("coroutine 시작")
    value = yield
    print(f"coroutine received : {value}")
    # while True:
    #     value = yield
    #     print(f"coroutine received : {value}")


def co2():
    print("coroutine2 시작")
    gen_value = 1
    while True:
        value = yield
        print(f"coroutine received : {value}")
        yield gen_value
        print(f"coroutine send : {gen_value}")
        gen_value += 1


if __name__ == "__main__":
    co1_object = co1()

    # yield 실행 전까지 실행 :
    next(co1_object)

    # 메인 루틴에서 코루틴에게 값 전송
    # co1_object.send(100)

    co2_object = co2()
    # yield 실행 전까지 실행 : coroutine2 시작
    next(co2_object)
    co2_object.send(30)  # coroutine received : 30

    next(co2_object)
    co2_object.send(50)  # coroutine received : 30
    next(co2_object)
