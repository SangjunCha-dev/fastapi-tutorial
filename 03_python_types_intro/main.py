from datetime import datetime
from typing import Union

from pydantic import BaseModel


# Pydantic models
class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2022-10-13 10:56",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)

print(user)
# id=123 signup_ts=datetime.datetime(2022, 10, 13, 10, 56) friends=[1, 2, 3] name='John Doe'

print(user.id)
# 123
