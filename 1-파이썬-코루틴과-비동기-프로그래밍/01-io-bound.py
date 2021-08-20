def io_bound_func():
    print("값을 입력해주세요.")
    input_value = input()
    return int(input_value) + 100


if __name__ == "__main__":
    result = io_bound_func()
    print(result)
