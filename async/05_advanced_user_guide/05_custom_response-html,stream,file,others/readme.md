# Custom Response - HTML, Stream, File, others

사용자 지정 응답 - HTML, 스트림, 파일, 기타


## Use ORJSONResponse

JSON 직렬화/역직렬화 성능이 빠른 라이브러리 `orjson`


## Available responses

- content: `str` or `bytes`.
- status_code: `int` or `HTTP status code`.
- headers: `dict` of `strings`.
- media_type: `str` giving the `media type`. E.g. "text/html".


## Default response class

- 기본 응답 클래스 지정

```
app = FastAPI(default_response_class=ORJSONResponse)
```


## 참고 Docs

- https://fastapi.tiangolo.com/advanced/custom-response/
