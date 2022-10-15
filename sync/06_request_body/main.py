from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    return item


# Use the model
@app.post("/items2/")
def create_item2(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request body + path parameters
@app.put("/items3/{item_id}")
def create_item3(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# Request body + path + query parameters
@app.put("/items4/{item_id}")
def create_item4(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result