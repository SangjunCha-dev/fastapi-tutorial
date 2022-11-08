# Security - First Steps

보안 - 첫번째 단계


## 라이브러리 설치

```bash
pip install python-multipart
```


## FastAPI's OAuth2PasswordBearer

- 헤더에서 Authorization 안에 Bearer 토큰 검증
- 유효한 Bearer 토큰이 없으면 401 상태 코드 오류를 응답함


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/security/first-steps/