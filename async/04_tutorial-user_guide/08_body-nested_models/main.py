from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


# List fields
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}


# List fields with type parameter
class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item2):
    return {"item_id": item_id, "item": item}


# Set types
class Item3(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()


@app.put("/items3/{item_id}")
async def update_item3(item_id: int, item: Item3):
    return {"item_id": item_id, "item": item}


# Nested Models
# Define a submodel
# Use the submodel as a type
class Image4(BaseModel):
    url: str
    name: str


class Item4(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    image: Union[Image4, None] = None


@app.put("/items4/{item_id}")
async def update_item4(item_id: int, item: Item4):
    return {"item_id": item_id, "item": item}


# Special types and validation
class Image5(BaseModel):
    url: HttpUrl
    name: str


class Item5(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None]
    tags: set[str] = str()
    image: Union[Image5, None] = None


@app.put("/items5/{item_id}")
async def update_item5(item_id: int, item: Item5):
    return {"item_id": item_id, "item": item}


# Attributes with lists of submodels
class Image6(BaseModel):
    url: HttpUrl
    name: str


class Item6(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    images: Union[list[Image6], None] = None


@app.put("/items6/{item_id}")
async def update_item6(item_id: int, item: Item6):
    return {"item_id": item_id, "item": item}


# Deeply nested models
class Image7(BaseModel):
    url: HttpUrl
    name: str


class Item7(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    images: Union[list[Image7], None] = None


class Offer7(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item7]


@app.post("/offers/")
async def create_offer(offer: Offer7):
    return offer


# Bodies of pure lists
class Image8(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images8/multiple/")
async def create_multiple_images(images: list[Image8]):
    return images


# Bodies of arbitrary dicts
@app.post("/index-weights")
async def create_index_weights(weights: dict[int, float]):
    return weights
