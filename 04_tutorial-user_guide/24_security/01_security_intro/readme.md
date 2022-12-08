# Security Intro

보안 소개


## OAuth2

- 인증 및 권한 부여를 처리하는 여러 방법을 정의하는 스펙
- `제3자`를 사용하여 인증하는 방법 포함
    - Facebook, Google, Twitter, GitHub 등


## OpenID Connect

- OAuth2 를 기반으로 하는 또 다른 스펙
- OAuth2에서 상대적으로 모호한 몇 가지 사항을 지정하여 OAuth2를 확장하여 상호 운용성을 높임
- 예를 들어 Google 로그인은 OpenID Connect(아래에서 OAuth2 사용)를 사용


## OpenAPI

- OpenAPI(이전에는 Swagger로 알려짐)는 API(현재 Linux Foundation의 일부) 구축을 위한 개방형 스펙
- FastAPI 는 OpenAPI 를 기반함
- FastAPI 가 여러 자동 대화형 문서 인터페이스, 코드 생성 등을 가능하게 하는 이유

### 보안체계 정의

- `apiKey`: 응용 프로그램별 키
    - query parameter
    - header
    - cookie
- `http`: 표준 HTTP 인증 시스템:
    - `bearer Authorization`: 헤더에 `Bearer` 토큰. OAuth2
    - HTTP Basic authentication
    - HTTP Digest
- `oauth2`: 모든 OAuth2 방법:
    - OAuth 2.0 인증 공급자(예: Google, Facebook, Twitter, GitHub 등)를 구축하는 데 적합
        - `implicit`
        - `clientCredentials`
        - `authorizationCode`
    - 동일한 애플리케이션에서 직접 인증을 처리하는 방법
        - `password`
- `openIdConnect`: OAuth2 인증 데이터를 자동으로 검색하는 방법
    - 이 자동 검색은 OpenID Connect 스펙에서 정의


## FastAPI utilities

- `fastapi.security` 보안 매커니즘의 사용을 단순화하는 모듈로 보안 체계 각각에 대해 여러 도구를 제공


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/security/
