# note

- [https://yeti.tistory.com/251](https://yeti.tistory.com/251)

Threading in Python is inefficient because of the GIL (Global Interpreter Lock) which means that multiple threads cannot be run in parallel as you would expect on a multi-processor system. Plus you have to rely on the interpreter to switch between threads, this adds to the inefficiency.

asyc/asyncio allows concurrency within a single thread. This gives you, as the developer, much more fine grained control of the task switching and can give much better performance for concurrent I/O bound tasks than Python threading.

The 3rd approach that you don't mention is multiprocessing. This approach uses processes for concurrency and allows programs to make full use of hardware with multiple cores.

- [https://leimao.github.io/blog/Python-Concurrency-High-Level/](https://leimao.github.io/blog/Python-Concurrency-High-Level/)

GIL은 코드 조각일 뿐입니다. CPython 가상 머신은 먼저 코드를 Cpython 바이트코드로 컴파일하는 프로세스이지만 일반적인 작업은 CPython 바이트코드를 해석하는 것입니다. GIL은 실행 중인 스레드 수에 관계없이 한 번에 한 줄의 바이트 코드가 실행되도록 하는 코드 조각입니다. Cpython Bytecode 명령어는 가상 머신 스택을 구성하는 것입니다. 따라서 어떤 면에서 GIL은 주어진 시간에 하나의 스레드만 GIL을 보유하도록 합니다. (또한 다른 스레드에 대해 GIL을 계속 릴리스하고 굶지 않게 합니다.)

asyncio는 코루틴을 기반으로 동작하며 데이터를 요청하고 응답하는 IO 작업에서 효율적이다.

asyncio는 기본적으로 싱글 스레드에서 돌아가기 때문에 멀티 스레드의 컨텍스트 스위칭 비용이 적게 들어갑니다.

https://brownbears.tistory.com/540
