# Response Model

response_model 

- 출력 데이터를 해당 유형 선언으로 변환
- 데이터 검증
- JSON 스키마 response 추가


## 라이브러리 설치

```bash
pip install pydantic[email]
```


## Use the response_model_exclude_unset parameter

### response_model_exclude_unset

- True 설정 시 해당 기본값 모델에 설정되어 있어도 응답에 포함되지 않고 실제로 설정된 값 응답에 포함


## 테스트

### Add an output model

- POST http://loaclhost:8000/user/

request
```json
{
  "username": "tester1",
  "password": "password1",
  "email": "user@example.com",
  "full_name": "fullname1"
}
```

response
```json
{
  "username": "tester1",
  "email": "user@example.com",
  "full_name": "fullname1"
}
```

### response_model_include and response_model_exclude

- 특정 모델의 필드를 포함시키거나 제외시킬수 있음
- GET http://loaclhost:8000/items2/foo/name

response
```json
{
  "name": "Foo",
  "description": null
}
```

- GET /items2/foo/public

```json
{
  "name": "Foo",
  "description": null,
  "price": 50.2,
  "tags": []
}
```


## 요약

response_model 설정으로 응답 모델을 정의하고 특히 개인 및 비밀 데이터가 필터링되도록 함


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/response-model/
