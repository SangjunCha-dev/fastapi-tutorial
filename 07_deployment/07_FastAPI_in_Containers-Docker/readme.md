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


## Deployment Concepts

- HTTPS
- 시작시 실행
- 재시작
- 복제(실행 중인 프로세스 수)
- 메모리
- 시작하기 전 이전 단계


## HTTPS

[Traefik](https://traefik.io/)


## Running on Startup and Restarts

컨테이너 시작 및 실행을 담당하는 도구

- Docker 직접 실행
- Docker Compose
- Kubernetes
- 클라우드 서비스 등

Docker의 재시작 옵션 `--restart`

대부분의 경우 컨테이너로 작업할 때 재시작 기능이 기본적으로 포함됨


## Replication - Number of Processes

Kubernetes와 같은 분산 컨테이너 관리 시스템은 일반적으로 들어오는 요청에 대한 로드 밸런싱을 지원하면서 컨테이너 복제를 처리하는 통합 방법으로 동작함(클러스터 수준)

이러한 경우 Uvicorn, Gunicorn 같은 프록시 서버를 실행하는 대신 Docker 이미지를 처음부터 빌드하고 종속성을 설치하고 단일 Uvicorn 프로세스를 실행함


## Load Balancer

로드 밸런서는 작업자 간에 균형잡힌 방식으로 요청을 배포하므로 부하를 분산 처리함


## One Load Balancer - Multiple Worker Containers

Kubernetes 같은 분산 컨테이너 관리 시스템으로 작업할 때 내부 네트워킹 메커니즘을 사용하면 단일 포트에서 수신하는 단일 로드 밸런서가 앱을 실행하는 여러 컨테이너의 통신을 전송할 수 있음

- 앱을 실행하는 각 컨테이너는 일반적으로 하나의 프로세스로 동작함
- 모두 동일한 컨테이너이며 동일한 서버를 실행하지만 각각 고유한 프로세스, 메모리 등을 가지고 있음
- CPU의 다른 코어 또는 다른 시스템에서도 병렬화 활용할 수 있음
- 따라서 각 요청은 앱을 실행하는 여러 복제 컨테이너 중 하나에서 처리할 수 있음

로드 밸런서는 클러스터의 다른 앱(도메인, URL 경로 접두사 등)으로 이동하는 요청을 처리할 수 있음


## One Process per Container

컨테이너 내부에 또 다른 프로세스 관리자가 있으면 불필요한 복잡성만 추가되므로 컨테이너 내부에서는 단일 프로세스로만 동작하는것이 좋음


## Containers with Multiple Processes and Special Cases

내부에서 여러 Uvicorn 작업자 프로세스를 시작하는 Gunicorn 프로세스 관리자가 있는 컨테이너 같은 특별한 경우

일부 기본 설정을 사용하여 현재 CPU 코어를 기반으로 작업자 수를 자동으로 조정할 수 있음

[Official Docker Image with Gunicorn - Uvicorn](https://fastapi.tiangolo.com/deployment/docker/#official-docker-image-with-gunicorn-uvicorn)

### A Simple App

애플리케이션이 간단하여 프로세스 수를 미세 조정할 필요없고 자동화된 기본값으로 클러스터가 아닌 단일 서버에서 실행하는 경우

### Docker Compose

Docker Compose를 사용하여 단일 서버(클러스터 아님)에 배포할 수 있으므로 공유 네트워크 및 로드 밸런싱을 유지하면서 컨테이너 복제(Docker Compose 사용)를 쉽게 관리할 수 있음


## Memory

컨테이너당 단일 프로세스를 실행하는 경우 각 컨테이너에서 소비되는 메모리 양은 제한하여 사용할 수 있음

컨테이너 관리 시스템(Kubenetes 등)에서 컨테이너에 대한 동일한 메모리 제한 및 요구사항을 설정할 수 있음

컨테이너당 여러 프로세스를 실행하는 경우 프로세스가 사용 가능한 것보다 많은 메모리를 사용하지 않도록 해야함


## Previous Steps Before Starting and Containers

컨테이너를 사용하는 경우 2가지 접근방식이 있음

### Multiple Containers

여러 컨테이너가 있고 각각 단일 프로세스(Kubernetes 클러스터)를 실행하는 경우 이전 단계의 작업(예: 데이터베이스 마이그레이션 등)을 수행하는 별도의 컨테이너가 필요할 수 있음

[described above in: Build a Docker Image for FastAPI](https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi)

예시에서 이전 단계를 병렬로 여러번 실행하는데 문제가 없는 경우(예: 데이터베이스 마이그레이션을 실행하지 않고 데이터베이스가 준비되었는지 확인하는 경우) 각 컨테이너에서 실행해도 괜찮음

### Single Container

단일 컨테이너를 사용하여 여러 작업자 프로세스를 시작하는 간단한 설정이 있는 경우 앱으로 프로세스를 시작하기 직전에 동일한 컨테이너에서 이전 단계를 실행할 수 있음


## 참조 Docs

- https://fastapi.tiangolo.com/deployment/docker/
