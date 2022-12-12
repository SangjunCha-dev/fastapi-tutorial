# Behind a Proxy

프록시

nginx 같은 프록시 서버를 사용해야 할 수 있다.


## Proxy with a stripped path prefix

1. `FastAPI()` root_path 별도 지정안한 경우 아래 명령어로 지정할 수 있음

```
uvicorn main:app --root-path /api/v1
```

2. 코드내 root_path 지정

```
FastAPI(root_path="/api/v1")
```


## Testing locally with Traefik

[traefik](https://github.com/traefik/traefik/releases) 다운로드
- 단일 바이너리 파일로 압축파일 다운받아 터미널에서 집적 실행

```
traefik --configFile=traefik.toml
```


## 참조 Docs

- https://fastapi.tiangolo.com/advanced/behind-a-proxy/
- https://doc.traefik.io/traefik/
