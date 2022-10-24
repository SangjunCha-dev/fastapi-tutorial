from lib2to3.pytree import Base
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Union[str, None] = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    user_in_db = UserInDB(
        **user_in.dict(), 
        hashed_password=fake_password_hasher(user_in.password)
    )
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    return fake_save_user(user_in)


# Reduce duplication
class UserBase2(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn2(UserBase2):
    password: str


class UserOut2(UserBase2):
    pass

class UserInDB2(UserBase2):
    hashed_password: str


def fake_password_hasher2(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user2(user_in: UserIn2):
    user_in_db = UserInDB2(
        **user_in.dict(), 
        hashed_password=fake_password_hasher2(user_in.password)
    )
    print("User saved! ..not really")
    return user_in_db


@app.post("/user2/", response_model=UserOut2)
async def create_user2(user_in: UserIn2):
    return fake_save_user2(user_in)


# Union or anyOf
class BaseItem3(BaseModel):
    description: str
    type: str


class CarItem(BaseItem3):
    type = "car"


class PlaneItem(BaseItem3):
    type = "plane"
    size: int


items3 = {
    "item1": {
        "description": "All my friends drive a low rider", 
        "type": "car",
    },
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items3/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items3[item_id]


# List of models
class Item4(BaseModel):
    name: str
    description: str


items4 = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items4/", response_model=list[Item4])
async def read_items():
    return items4


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}
