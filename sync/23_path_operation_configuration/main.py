from typing import Union
from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()


# Response Status Code
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item


# Tags
@app.post("/items2/", response_model=Item, tags=["items"])
def create_item2(item: Item):
    return item


@app.get("/items2/", tags=["items"])
def read_items2():
    return [{"name": "Foo", "price": 42}]


@app.get("/users2/", tags=["users"])
def read_users2():
    return [{"username": "johndoe"}]


# Tags with Enums
class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items3/", tags=[Tags.items])
def get_items3():
    return ["portal gun", "Plumbus"]


@app.get("/users3/", tags=[Tags.users])
def read_users3():
    return ["Rick", "Morty"]


# Summary and description
@app.post(
    "/items4/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax, and a set of unique tags",
)
def create_item4(item: Item):
    return item


# Description from docstring
@app.post("/items5/", response_model=Item, summary="Create an item")
def create_item5(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# Response description
@app.post(
    "/items6/",
    response_model=Item,
    summary="Create an item",
    response_description="The created item",
)
def create_item6(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# Deprecate a path operation
@app.get("/elements/", tags=["items"], deprecated=True)
def read_elements():
    return [{"item_id": "Foo"}]
