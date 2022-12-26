# Extending OpenAPI

OpenAPI 확장


## The normal process

get_openapi() 매개변수
- title: 문서에 표시된 OpenAPI 제목
- version: API 버전
- openapi_version: 사용된 OpenAPI 사양의 버전
- description: API에 대한 설명
- routes: 경로 목록, 등록된 각 경로


## Self-hosting JavaScript and CSS for docs

API 문서는 Swagger UI 및 ReDoc를 사용하며 각각 JavaScript 및 CSS 파일을 필요함

기본적으로 제공하나 사용자 지정이 가능하며 특정 CDN을 설정하거나 파일을 직접 제공할 수 있음


### Download the files

static 디렉토리에 저장

- [swagger-ui-bundle.js](https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui-bundle.js)
- [swagger-ui.css](https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.css)
- [redoc.standalone.js](https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js)


### Test the static files

js 파일 조회됨

```
http://127.0.0.1:8000/static/redoc.standalone.js
```


## 참조 Docs

- https://fastapi.tiangolo.com/advanced/extending-openapi/
