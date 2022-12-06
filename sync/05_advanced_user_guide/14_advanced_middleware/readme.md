# Advanced Middleware

고급 미들웨어


## HTTPSRedirectMiddleware

들어오는 모든 요청이 `https` 또는 `wss` 이어야함


## TrustedHostMiddleware

들어오는 모든 요청에 올바르게 설정된 헤더가 있는지 확인 (HTTP 호스트 헤더 공격 방지)

- `allowed_hosts`: 허용하는 도메인 이름 목록 (와일드카드 사용가능)
    - 도메인이 일치하지 않으면 400 응답 반환
- `allowed_hosts=["*"]`: 모든 호스트 허용


## GZipMiddleware

모든 GZip 요청에 대한 응답 처리

- `minimum_size`: 최소 크기(bytes)보다 작은 응답을 GZip 압축 권장하지 않음. (default 500)


## Other middlewares

- [Sentry](https://docs.sentry.io/platforms/python/asgi/)
- [Uvicorn's ProxyHeadersMiddleware](https://github.com/encode/uvicorn/blob/master/uvicorn/middleware/proxy_headers.py)
- [MessagePack](https://github.com/florimondmanca/msgpack-asgi)


## 참조 Docs

- https://fastapi.tiangolo.com/advanced/middleware/
