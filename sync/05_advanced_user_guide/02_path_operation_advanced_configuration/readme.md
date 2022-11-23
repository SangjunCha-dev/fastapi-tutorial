# Path Operation Advanced Configuration

경로 작업 고급 구성


## 라이브러리 설치

```bash
pip install PyYAML
```


## OpenAPI operationId

operation_id: Docs 에서 사용할 경로명 지정

```
http://localhost:8000/docs#/default/some_specific_id_you_define
```


### Using the path operation function name as the operationId

모듈과 상관없이 각 경로 작업 함수 의 이름이 고유한지 확인 필요함


## Advanced description from docstring

\f(이스케이프된 "form feed" 문자) 를 추가 하면 FastAPI 가 이 시점에서 OpenAPI에 사용되는 출력을 생략함


## 참고 Docs

- https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/
