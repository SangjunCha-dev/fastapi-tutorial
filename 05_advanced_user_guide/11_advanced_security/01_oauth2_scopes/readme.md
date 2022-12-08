# OAuth2 scopes

 OAuth2 scopes는 Facebook, Google, GitHub, Microsoft, Twitter 등과 같은 많은 대규모 인증 공급자가 사용하는 메커니즘


## OAuth2 scopes and OpenAPI

"scopes"
- 공백으로 구분된 문자열 목록으로 정의
- 각 문자열 내용은 모든 형식을 사용할 수 있지만 공백을 포함해서는 안됨
- scopes는 `권한`을 의미
- 일반적으로 특정 보안권한을 선언하는데 사용
  - 일반적인 예: `users:read`,` users:write`


## 참고 Docs

- https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
