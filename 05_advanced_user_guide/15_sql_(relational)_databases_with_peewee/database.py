from typing import Any

from contextvars import ContextVar

import peewee

DATABASE_NAME = "test.db"
db_state_default = {
    "closed": None, 
    "conn": None,
    "ctx": None,
    "transactions": None,
}

# 비동기 기능과 호환할 될수 있게 설정
db_state = ContextVar(
    "db_state",
    default=db_state_default.copy(),
)


# Make Peewee async-compatible PeeweeConnectionState
class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name: str, value: Any):
        self._state.get()[name] = value
    
    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.SqliteDatabase(
    DATABASE_NAME,
    check_same_thread=False,  # SQLite에 필요한 옵션
)


# Use the custom PeeweeConnectionState class
db._state = PeeweeConnectionState()
