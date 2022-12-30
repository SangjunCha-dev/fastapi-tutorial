# Run a Server Manually - Uvicorn

수동으로 서버 실행 - Uvicorn

FastAPI 애플리케이션을 실행할 수 ASGI 프로그램

- [Uvicorn](https://www.uvicorn.org/): 고성능 ASGI 서버
- [Hypercorn](https://pgjones.gitlab.io/hypercorn/): HTTP/2 및 Trio와 호환되는 ASGI 서버
- [Daphne](https://github.com/django/daphne): Django 채널용으로 구축된 ASGI 서버


## Server Machine and Server Program

"Server"는 일반적으로 원격/클라우드 컴퓨터와 해당 머신(물리적 또는 가상환경)에서 실행되는 프로그램(예: Uvicorn)을 모두 지칭함


## Uvicorn

### Install the Server Program

uviloop, httptools를 기반으로 구축

```
pip install "uvicorn[standard]"
```

- Uvicorn standard: 몇가지 권장되는 추가 종속성 설치 및 사용
- uviloop: 고성능 동시성 성능향상 라이브러리 asyncio의 대체 라이브러리

### Run the Server Program

```
uvicorn main:app --host 0.0.0.0 --port 80
```


## Hypercorn

### Install the Server Program

HTTP/2와 호환되는 ASGI 서버

```
pip install hypercorn
```

### Run the Server Program

```
hypercorn main:app --bind 0.0.0.0:80
```


## Hypercorn with Trio

Starlette 및 FastAPI 는 Python 표준 라이브러리인 asyncio 및 Trio와 호환되는 AnyIO를 기반으로 동작함

Uvicorn은 현재 uvloop를 사용하고 asyncio와 호환됨

Trio를 직접 사용하려면 Hypercorn이 지원하는 대로 사용할 수 있음

### Install Hypercorn with Trio

```
pip install "hypercorn[trio]"
```

### Run with Trio

```
hypercorn main:app --worker-class trio
```

trio를 백엔드로 Hypercorn ASGI 서버가 실행됨
- AnyIO를 사용하여 코드가 Trio 및 asyncio 와 호환되도록 유지할 수 있음


## Deployment Concepts

배포시 고려사항

- 보안 - HTTP
- 시작 또는 실행
- 재시작
- 복제(실행 프로세스 수)
- 메모리
- 시작전 사전실행


## 참조 Docs

- https://fastapi.tiangolo.com/deployment/manually/
