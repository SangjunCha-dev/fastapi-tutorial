# Conditional OpenAPI

조건부 OpenAPI


## About security, APIs, and docs

- Body 요청 및 응답에 대해 잘 정의된 Pydantic 모델 정의
- 종속성을 사용하여 필요한 권한 및 역할 구성
- 암호는 일반 텍스트로 저장하지 말고 암호 해시로 저장해야 함
- Passlib 및 JWT 토큰 등과 같은 잘 알려진 암호화 도구를 구현하고 사용
- 필요한 경우 OAuth2 Scope로 세분화된 권한제어 가능


## 참조 Docs

- https://fastapi.tiangolo.com/advanced/conditional-openapi/
