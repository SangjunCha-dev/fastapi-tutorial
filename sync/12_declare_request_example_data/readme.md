# Declare Request Example Data

request 예시 데이터 선언

## example and examples in OpenAPI

- Path()
- Query()
- Header()
- Cookie()
- Body()
- Form()
- File()

위의 기능을 사용할 때 example, examples 인수를 사용할 수 있음

## Body with multiple examples

examples 에서 사용되는 키

- summary: 예제에 대한 간단한 설명
- description: 마크다운 텍스트를 포함할 수 있는 긴 설명
- value: 표시된 실제 데이터 예시 json 형식
- externalValue: 대체 value, 예제 URL


## 테스트

### Pydantic schema_extra

- http://localhost:8000/docs
- PUT /items/{item_id} 기능 클릭시 아래와 같은 예시 데이터 입력된 것 확인

```json
{
    "name": "Foo",
    "description": "A very nice Item",
    "price": 35.4,
    "tax": 3.2
}
```


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/schema-extra-example/