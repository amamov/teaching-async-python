# FastAPI

- [fastapi docs](https://fastapi.tiangolo.com/ko/)
- [uvicorn](https://www.uvicorn.org/)
- [starlette](https://www.starlette.io/)
- [pydantic](https://pydantic-docs.helpmanual.io/)
- [github start 비교](https://star-history.t9t.io/#)

### uvicorn

> Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

> uvicorn은 ASGI중 하나이다.

- [docs](https://www.uvicorn.org/)

#### ASGI (Asynchronous Server Gateway Interface)

> ASGI는 애플리케이션 프로그램(FastAPI)의 실행 결과를 웹 서버(NGINX)에 전달해주며, 웹 서버(NGINX)는 ASGI로부터 전달받은 응답 결과를 웹 클라이언트(브라우저)에 전송한다.

- [docs](https://asgi.readthedocs.io/en/latest/introduction.html)
- 서버 게이트웨이 : 서버로 들어가는 입구 역할

### pydantic

> python에서의 dto

### 환경변수 관련

환경변수란 외부에서 변수를 정의하여 프로그램 내부에서 사용할 수 있도록 하는 변수입니다.
이렇게 함으로써 외부에 변수가 정의되어 있기 때문에 프로그램 코드가 유출이 되어도 해당 변수는 유출이 되지 않습니다. 따라서 보안상 중요한 변수값은 외부에서 정의해서 사용합니다. 또한 외부에서 자주 바뀌는 변수 또한 환경변수로 설정해줘서 프로그램 코드에 접근하지 않고 외부에서 쉽게 값을 변경하고 싶은 경우에도 환경변수로 사용합니다.

일반적으로 [fastapi 공식문서](https://fastapi.tiangolo.com/ko/advanced/settings/?h=env)와 같이 시스템 명령 쉘에서 저장하여 사용할 수 있습니다. 하지만 이는 관리가 어렵과 특정 경우에 한해 환경 변수를 이용하는 방법이 작동되지 않습니다.

이러한 문제점에 대한 적절한 솔루션은 [python dotenv](https://github.com/theskumar/python-dotenv) 패키지를 사용해서 `.env` 안에 변수들을 관리하는 방법이 있습니다.

또 패키지를 사용하지 않고 `json`, `xml`, `config`, `yml`중 한 가지 포맷을 선택하여 파일을 생성하여 작성하는 방법이 있습니다.

한 가지 주의할 것은 깃을 사용하여 버전 관리를 할 경우에 이러한 포맷들의 파일을 사용하든 `.env` 파일을 사용하든 반드시 `.gitignore` 에 추가해야 합니다.

```json
{
  "hello": "world"
}
```

## fastapi getting start

1. `pip install fastapi`

2. `pip install uvicorn`

## python type checking lint

1. [pylance 설치](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

2. `settings.json`파일에 아래의 옵션 추가하기

```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "strict"
}
```
