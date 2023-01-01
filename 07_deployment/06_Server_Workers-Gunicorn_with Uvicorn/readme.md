# Server Workers - Gunicorn with Uvicorn


## Gunicorn with Uvicorn Workers

Gunicorn
- WSGI 표준을 사용하는 애플리케이션 서버
- Gunicorn 자체는 FastAPI와 호환되지 않음

Gunicorn은 프로세스 관리자로 작업하고 사용자가 사용할 특정 작업자 프로세스 클래스를 지정할 수 있도록 지원함.
Gunicorn은 해당 클래스를 사용하여 하나 이상의 작업자 프로세스를 시작
Uvicorn에는 Gunicorn 호환 작업자 클래스가 있음

이 조합을 사용하여 Gunicorn은 포트와 IP에서 수신대기하는 프로세스 관리자 역할을 함
그리고 Uvicorn 클래스를 실행하는 작업자 프로세스로 통신을 전송함

Gunicorn 호환 Uvicorn 작업자 클래스는 Gunicorn에서 보낸 데이터를 FastAPI에서 사용할 수 있도록 ASGI 표준으로 변환하는 작업을 담당

Gunicorn 동기 프로세스들로 비동기 Uvicorn 프로세스 실행


## Install Gunicorn and Uvicorn

```
$ pip install "uvicorn[standard]" gunicorn
```


## Run Gunicorn with Uvicorn Workers

```
$ gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

- main:app : main.py 파일의 app 변수
- --workers : 사용할 작업자 프로세스 수, 각각 Uvicorn 작업자
- --worker-class : 작업자 프로세스에서 사용할 Gunicorn 호환 작업자 클래스
- --bind : Gunicorn에서 수신할 IP와 포트를 지정
  - Uvicorn 직접 실행할 경우 옵션 : `--host 0.0.0.0 --port 80`

Gunicorn은 죽은 프로세스를 관리하고 작업자 수를 유지하기 위해 필요한 경우 새 프로세스를 다시 시작함
따라서 Python 수준에서 프로세스 관리자를 사용하려면 Gunicorn을 프로세스 관리자로 사용하는 것이 좋음

```
$ uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
```


## Uvicorn with Workers

Uvicorn에는 여러 작업자 프로세스를 시작하고 실행할 수 있는 옵션도 있지만 Gunicorn 보다 제한적


## 요약

Gunicorn (또는 Uvicorn)을 Uvicorn 작업자와 함께 프로세스 관리자로 사용하여 멀티 코어 CPU를 활용하고 여러 프로세스를 병렬로 실행할 수 있음


## 참조 Docs

- https://fastapi.tiangolo.com/deployment/server-workers/#gunicorn-with-uvicorn-workers
