# Simple OAuth2 with Password and Bearer

간단한 OAuth2 - 비밀번호와 Bearer


## Get the username and password scope

### scope

- oauth2에서공통적으로 사용되는 변수
- 공백으로 구분된 긴 문자열로 사용됨
- scopes에는 특정 권한요청이나 응답요청 변수를 작성함


## OAuth2PasswordRequestForm

- 필수 입력 필드
    - username
    - password
    - scope
- 선택 입력 필드
    - grant_type
    - client_id
    - client_secret
- 실제로 입력필드를 강제하지 않음
- 입력필드가 강제할 경우 `OAuth2PasswordRequestFormStrict` 클래스 사용


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/