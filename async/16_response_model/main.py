from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


# Return the same input data
# Add an output model
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# Response Model encoding parameters
class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {
        "name": "Foo", 
        "price": 50.2
    },
    "bar": {
        "name": "Bar", 
        "description": "The bartenders", 
        "price": 62, 
        "tax": 20.2
    },
    "baz": {
        "name": "Baz", 
        "description": None, 
        "price": 50.2, 
        "tax": 10.5, 
        "tags": []
    },
}


@app.get(
    "/items/{item_id}", 
    response_model=Item, 
    response_model_exclude_unset=True
)
async def read_item(item_id: str):
    return items[item_id]


# response_model_include and response_model_exclude
class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5


items2 = {
    "foo": {
        "name": "Foo", 
        "price": 50.2
    },
    "bar": {
        "name": "Bar", 
        "description": "The Bar fighters", 
        "price": 62, 
        "tax": 20.2
    },
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items2/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name2(item_id: str):
    return items[item_id]


@app.get(
    "/items2/{item_id}/public", 
    response_model=Item, 
    response_model_exclude={"tax"}
)
async def read_item_public_data2(item_id: str):
    return items[item_id]
