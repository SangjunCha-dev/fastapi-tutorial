# SQL (Relational) Databases

관계형 데이터베이스


## ORM

- 코드의 개체와 데이터베이스 테이블(관계) 사이를 변환(매칭)하는 도구


## 파일 구조

```
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```

## Create the SQLAlchemy engine

### sqlite

- SQLite는 각 스레드가 독립적인 요청을 처리한다고 가정하여 하나의 스레드만 통신할 수 있도록 허용
- 서로 다른 요청에 대해 실수로 동일한 연결을 공유하는 것을 방지하기 위함

### Create a SessionLocal class

- 클래스 자체는 아직 데이터베이스 세션이 아님
- 클래스의 각 인스턴스는 SessionLocal 데이터베이스 세션이 됨


## Create SQLAlchemy models from the Base class

SQLAlchemy의 model
- 데이터베이스와 상호작용하는 클래스 및 인스턴스

Pydantic의 model
- 데이터 유효성 검사, 변환, 문서 클래스 및 인스턴스


## Create the Pydantic models

models.py
- SQLAlchemy model 작성

schemas.py
- Pydantic model 작성

### Technical Details about ORM mode

SQLAlchemy 기본 동작은 "lazy loading".방식
- 데이터가 포함된 특성에 엑세스하려고 시도하지 않는 한 데이터베이스에서 관계에 대한 데이터를 가져오지 않음


## CRUD utils

데이터베이스의 데이터와 상호 작용하는 재사용 가능한 기능

## Main FastAPI app

### About def vs async def

SQLAlchemy는 await를 직접 사용할 수 있는 호환성이 없음

```python
user = await db.query(User).first()
```

다음과 같이 경로 함수에서 비동기가 없는 일반 함수로 선언해야함

```python
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    ...
```


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/sql-databases/
