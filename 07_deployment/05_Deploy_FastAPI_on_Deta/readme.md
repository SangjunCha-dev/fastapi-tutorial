# Deploy FastAPI on Deta

[Deta](https://www.deta.sh/?ref=fastapi)에 FastAPI 배포


## Deta

라이브러리 설치

```
pip install deta
```


## Create a free Deta account

Now create a [free account on Deta](https://fastapi.tiangolo.com/deployment/deta/#:~:text=Now%20create%20a,account%20on%20Deta)


## Install the CLI

운영체제별 설치([Getting Started](https://docs.deta.sh/docs/micros/getting_started))

Mac or Linux

```
$ curl -fsSL https://get.deta.dev/cli.sh | sh
```

windows powershell

```
> iwr https://get.deta.dev/cli.ps1 -useb | iex
```

설치 확인

```
$ deta --help

Deta command line interface for managing deta micros.
Complete documentation available at https://docs.deta.sh
```


## Login with the CLI

```
$ Deta login

Please, log in from the web page. Waiting..
Logged in successfully.
```


## Deploy with Deta

fastapideta 디렉토리 경로까지 터미널 접속

```
$ deta new --python

Successfully created a new micro
{
        "name": "fastapideta",
        "id": "9a024639-d95a-411c-bfed-2d9f2651c425",
        "project": "b07hrdfd",
        "runtime": "python3.9",
        "endpoint": "https://qi4ltf.deta.dev",
        "region": "us-east-1",
        "visor": "disabled",
        "http_auth": "disabled"
}
Adding dependencies...
```


## Enable public access

기본적으로 Deta는 계정 쿠키를 사용하여 인증함

공개 접속 활성화

```
$ deta auth disable

Successfully disabled http auth
```

기본 인증 활성화

```
$ deta auth enable

Successfully enabled http auth
```


## HTTPS

Deta는 HTTPS 연결을 지원함


## Check the Visor

[Visor](https://web.deta.sh/home)

```
$ deta visor enable
```


## Deployment Concepts

- HTTPS: Deta에서 처리하며 하위 도메인을 제공하고 HTTPS를 자동으로 처리함
- 시작시 실행: 서비스의 일부로 Deta에서 처리
- 다시 시작: 서비스의 일부로 Deta에서 처리
- 복제: 서비스의 일부로 Deta에서 처리
- 메모리: Deta에서 제한 정의
- 시작 전 이전 단계: 직접 지원되지 않으며 Cron 시스템 또는 추가 스크립트와 함께 작동


## 참조 Docs

- https://fastapi.tiangolo.com/deployment/deta/
- https://docs.deta.sh/docs/micros/getting_started?ref=fastapi
- [Deta 데이터베이스](https://docs.deta.sh/docs/base/py_tutorial?ref=fastapi)
