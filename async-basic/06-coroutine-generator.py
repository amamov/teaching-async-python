# 제너레이터에 대하여
# https://docs.python.org/3.2/library/inspect.html#current-state-of-a-generator


# yield
def my_gen():
    print("generator start")
    i = 0
    while True:
        print(f"generator i : {i}")
        yield i
        i += 1


# yield from
def my_gen2():
    # for x in range(10):
    #     yield x

    yield from range(10)


if __name__ == "__main__":
    gen_obj = my_gen()
    next(gen_obj)  # generator start : GEN_CREATED (처음 대기 상태)
    # generator i : 0

    next(gen_obj)  # generator i : 1
    next(gen_obj)  # generator i : 2

    # 전송은 주체가 있고 대상이 있을 때 주체가 대상한테 값을 주는 것이다.
    # 제너레이터는 주체인 제너레이터에서 대상인 메인 루틴에게 값을 준다. (단방향)
