# Extra Data Types

추가 데이터 유형


## Other data types

- UUID
    - Universally Unique Identifier
    - 요청 및 응답 표시: str
- datetime.datetime
    - 요청 및 응답 표시: str
    - 2008-09-15T15:53:00+05:00
- datetime.date
    - 요청 및 응답 표시: str
- datetime.time
    - 2008-09-15
    - 요청 및 응답 표시: str
    - 14:23:55.003
- datetime.timedelta
    - 요청 및 응답 표시: float 초단위
- frozenset
    - 요청 처리: set
    - 응답 변환: list
- bytes
    - 요청 및 응답 표시: str
- Decimal
    - 요청 및 응답 표시: float


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/extra-data-types/