# Path Operation Configuration

경로 작업 구성

이 매개변수는 경로 작업 함수 가 아니라 경로 작업 데코레이터에 직접 전달함


## Tags

태그 설정시 OpenAPI 문서에서 카테고리로 사용됨

```python
@app.post(..., tags=["items"])
```


## Tags with Enums

열거형으로 태그를 지정할 수 있음

```python
from enum import Enum


class Tags(Enum):
    items = "items"
    users = "users"

@app.get(..., tags=[Tags.items])
@app.get(..., tags=[Tags.users])
```


## Summary and description

OpenAPI 문서의 기능 요약과 설명을 지정할 수 있음

```python
@app.post(
    ...
    summary="summary text",
    description="description text",
)
```


## Description from docstring

description과 동일한 역할이지만 마크다운 문법을 적용하여 가독성 좋게 작성 가능

함수에 메인 주석을 달아서 작성

```python
async def create_item(item: Item):
    """
    docstring text

    ...
    """
```


## Response description

OpenAPI 문서의 response 설명 지정

```python
@app.post(
    ...
    response_description="response description text",
)
```


## Deprecate a path operation

OpenAPI 문서에서 비활성화 표시

```python
@app.get(..., deprecated=True)
```


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
