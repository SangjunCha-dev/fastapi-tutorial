# SQL (Relational) Databases with Peewee

Peewee를 사용한 SQL(관계형) 데이터베이스

> Peewee를 안전하게 사용하려면 Python 3.7 이상 필요


## 라이브러리 설치

```
pip install peewee
```


## Peewee for async

- 비동기 프레임워크용으로 설계되지 않음
- 기본값과 사용방법이 쉽지 않음
- 일부 기본값을 변경하거나 미리 정의된 데이터베이스를 2개 이상 지원하고 비동기 프레임워크(FastAPI)로 작업해야 하는 경우 기본값 재정의를 위해 복잡한 코드를 추가해야함
  

## File structure

```
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    └── schemas.py
```


## Make Peewee async-compatible PeeweeConnectionState

FastAPI 및 Peewee의 주요 문제는 [python threading.local](https://docs.python.org/3/library/threading.html#thread-local-data), 이를 재정의하거나 연결/세션을 직접 처리할 수 있는 직접적인 방법이 없음

`database.py`와 같이 설정하면 FastAPI With Peewee가 올바르게 작동할 수 있음

비동기를 지원하지 않아 `async def`가 아닌 동기 `def` 로 사용해야함


## Create a PeeweeGetterDict for the Pydantic models / schemas

pydantic에서 상속하는 사용자 정의클래스를 제공하여 ORM 모델 속성 값 검색가능

```
    class Config:
        orm_mode = True
        getter_dict = peeweeGetterDict
```


## About def vs async def

async
```
user = await models.User.select().first()
```

sync
```
user = models.User.select().first()
```


## 참조 Docs

- https://fastapi.tiangolo.com/advanced/sql-databases-peewee/
