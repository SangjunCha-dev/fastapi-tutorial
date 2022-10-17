from typing import Union

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


# Mix Path, Query and body parameters - Body (Path, Query) 매개변수
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: Union[Item, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# Multiple body parameters - Body 다중 매개변수
@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item, user: User):
    return {
        "item_id": item_id, 
        "item": item, 
        "user": user
    }


# Singular values in body - Body 특이한 값
@app.put("/items3/{item_id}")
async def update_item3(
    item_id: int, item: Item, user: User, importance: int = Body()
):
    return {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance,
    }


# Multiple body params and query
@app.put("/items4/{item_id}")
async def update_item4(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(gt=0),
    q: Union[str, None] = None
):
    results = {
        "item_id": item_id, 
        "item": item, 
        "user": user, 
        "importance": importance
    }

    if q:
        results.update({"q": q})
    return results


# Embed a single body parameter - 단일 Body 매개변수 embed
@app.put("/items5/{item_id}")
async def update_item5(item_id: int, item: Item = Body(embed=True)):
    return {"item_id": item_id, "item": item}
