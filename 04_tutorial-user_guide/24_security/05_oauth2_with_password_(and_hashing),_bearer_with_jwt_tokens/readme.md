# OAuth2 with Password (and hashing), Bearer with JWT tokens

비밀번호(및 해싱)가 있는 OAuth2, JWT 베어러 토큰


## About JWT

JWT - JSON 웹 토큰

JWT 토큰 작동 방식을 확인
- https://jwt.io


## 라이브러리 설치

```bash
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"
```
- `python-jose[cryptography]`: JWT 토큰을 생성하고 확인
- `passlib[bcrypt]`
    - "context" 생성
    - 암호 해시 처리 및 확인


## scopes

- JWT 토큰에 특정 권한 집합을 추가


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/