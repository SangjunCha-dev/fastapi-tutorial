# FastAPI in Containers - Docker

- FastAPI 애플리케이션을 배포할 때 일반적으로 Linux 컨테이너 이미지를 빌드함
- [Docker](https://www.docker.com/)

dockerfile
```
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
```


## What is a Container

- 컨테이너(주로 Linux 컨테이너)는 동일한 시스템의 다른 컨테이너(다른 애플리케이션 또는 구성 요소)와 격리된 상태로 유지
- 모든 종속성과 필요한 파일을 포함하여 애플리케이션을 패키징하는 매우 가벼운 방법


## What is a Container Image

- 컨테이너는 컨테이너 이미지에서 실행되고, 일반적으로 실행 중인 인스턴스를 의미
- 컨테이너 이미지는 컨테이너에서 필요한 모든 파일, 환경 변수 및 기본 명령/프로그램이 있는 정적 이미지
- 컨테이너 자체는(컨테이너 이미지와 달리) 이미지의 실제 실행 인스터스이며 프로세스와 유사함


## Container Images

- Docker는 컨테이너 이미지와 컨테이너를 만들고 관리하는 도구중 하나
- [도커 허브](https://hub.docker.com/)에서 많은 도구, 환경, 데이터베이스 및 애플리케이션을 위한 사전 빌드된 공식 컨테이너 이미지를 사용할 수 있음
  
Image
- [Python](https://hub.docker.com/_/python)
- [PostgreSQL](https://hub.docker.com/_/postgres)
- [MySQL](https://hub.docker.com/_/mysql)
- [MongoDB](https://hub.docker.com/_/mongo)
- [Redis](https://hub.docker.com/_/redis)
- 등등
  
따라서 데이터베이스, Python 애플리케이션, React 프론트엔드 애플리케이션이 있는 웹서버와 같이 여러 컨테이너를 실행하고 내부 네트워크를 통해 연결할 수 있음


## Containers and Processes

- 컨테이너 이미지는 일반적으로 메타데이터에 컨테이너가 시작될 때 실행되어야 하는 기본 프로그램 또는 명령과 해당 프로그램에 전달될 매개변수를 포함
- 컨테이너가 시작되면 해당 명령/프로그램을 실행함
- 컨테이너는 기본 프로세스(명령 또는 프로그램)가 실행되는 동안 실행됨
- 컨테이너는 일반적으로 단일 프로세스가 있지만 기본 프로세스에서 하위 프로세스를 시작하는 것도 가능하므로 동일한 컨테이너에 여러 프로세스가 있음


## Build a Docker Image for FastAPI

### Package Requirements

패키지 요구사항 작성

requirements.txt

```
fastapi>=0.68.0,<0.69.0
pydantic>=1.8.0,<2.0.0
uvicorn>=0.15.0,<0.16.0
```

패키지 종속성 설치

```
pip install -r requirements.txt
```

### Behind a TLS Termination Proxy

TLS 종료 프록시 뒤에 컨테이너를 실행하는 경우 프록시 옵션을 추가하여 uvicorn 실행
- --proxy-headers 해당 프록시에서 보낸 헤더를 신뢰하고 응용 프로그램이 HTTPS 등에서 실행되고 있음을 알림

```
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
```

### Build the Docker Image

1. 프로젝트 디렉토리로 이동
2. 도커 이미지 빌드 `docker build -t myimage .`

### Start the Docker Container

도커 컨테이너 실행

```
$ docker run -d --name mycontainer -p 80:80 myimage
```

접속

```
request
http://127.0.0.1/items/5?q=somequery

response
{"item_id": 5, "q": "somequery"}
```


## 참조 Docs

- https://fastapi.tiangolo.com/deployment/docker/
