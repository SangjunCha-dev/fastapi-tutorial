from typing import Union

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


# Query Parameters
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip+limit]


# Optional parameters
# Query parameter type conversion
@app.get("/items/{item_id}")
async def read_item(
    item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id}
    
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})

    return item


# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    
    return item


# Required query parameters
@app.get("/items2/{item_id}")
async def read_user_item2(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
