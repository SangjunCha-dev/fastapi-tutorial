# 라이브러리 설치

```bash
pip install fastapi
pip install "uvicorn[standard]"
```


# 서버 실행

```
uvicorn main:app --reload
```


# 브라우저 테스트

- http://127.0.0.1:8000/items/5?q=somequery

```
{"item_id":5,"q":"somequery"}
```


# 대화형 API 문서

- http://127.0.0.1:8000/docs
- Swagger UI 제공


# 대안 API 문서

- http://127.0.0.1:8000/redoc
- ReDoc 제공


# 참고 Docs

- https://fastapi.tiangolo.com/ko/#_5