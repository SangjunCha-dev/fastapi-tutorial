# Alternatives, Inspiration and Comparisons

대안, 영감 및 비교


## Previous tools

### [Django](https://www.djangoproject.com/)

- Python 프레임워크
- 관계형 데이터베이스(MySQL 또는 Post)와 밀접하게 결합되어 있음
- NoSQL(MongoDB 등) 데이터베이스를 기본 저장소 엔진으로 사용할 수도 있음

### [Django REST Framework](https://www.django-rest-framework.org/)

- API 기능을 개선하기 위해 웹 API를 구축하기 위한 툴킷

### [Flask](https://flask.palletsprojects.com/)

- 마이크로 프레임워크 
- 단순성과 유연성 있음
- 데이터베이스, 사용자 관리 또는 Django에 사전 구축된 많은 기능이 필요하지 않은 애플리케이션에서 일반적으로 사용됨

### [Requests](https://requests.readthedocs.io/)

- (클라이언트로서) API와 상호작용 하기위한 라이브러리
- FastAPI(서버로서)는 API를 빌드하기 위한 라이브러리
- 사용방법 간단

```
response = requests.get("http://example.com/some/url")
```

- FastAPI 대응 API 경로

```
@app.get("/some/url")
def read_url():
    return {"message": "Hello World"}
```

### [Swagger](https://swagger.io/) / [OpenAPI](https://github.com/OAI/OpenAPI-Specification/)

- JSON(또는 JSON의 확장인 YMAL)을 사용하여 API를 문서화하는 표준
- 이미 생성된 Swagger API용 웹 사용자 인터페이스가 있음
- API에 대한 Swagger 문서를 생성할 수 있으면 이 웹 사용자 인터페이스를 자동으로 사용할 수 있음
- 버전 2.0 - Swagger
- 버전 3+ - OpenAPI


## 참조 Docs

- https://fastapi.tiangolo.com/alternatives/
