from typing import Set, Union

from fastapi import FastAPI, Request, HTTPException
from fastapi.routing import APIRoute
from pydantic import BaseModel, ValidationError
import yaml

app = FastAPI()


@app.get("/items/", operation_id="some_specific_id_you_define")
def read_items():
    return [{"item_id": "Foo"}]


# Using the path operation function name as the operationId
def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(app)


# Exclude from OpenAPI
@app.get("/items2/", include_in_schema=False)
def read_items2():
    return [{"item_id": "Foo"}]


# Advanced description from docstring
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.post("/items/", response_model=Item, summary="Create an item")
def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item


# OpenAPI Extensions
@app.get("/items3/", openapi_extra={"x-aperture-labs-portal": "blue"})
def read_items3():
    return [{"item_id": "portal-gun"}]


# Custom OpenAPI path operation schema
def magic_data_reader(raw_body: bytes):
    return {
        "size": len(raw_body),
        "content": {
            "name": "Maaaagic",
            "price": 42,
            "description": "Just kiddin', no magic here. ✨",
        },
    }


@app.post(
    "/items2/",
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "required": ["name", "price"],
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "price": {"type": "number"},
                            "description": {"type": "string"},
                        }
                    }
                }
            },
            "required": True
        },
    },
)
def create_item2(request: Request):
    raw_body = request.body()
    data = magic_data_reader(raw_body)
    return data


# Custom OpenAPI content type
class Item(BaseModel):
    name: str
    tags: list[str]


@app.post(
    "/items3/",
    openapi_extra={
        "requestBody": {
            "content": {
                "application/x-yaml": {
                    "schema": Item.schema(),
                },
            },
            "required": True,
        },
    },
)
def create_item3(request: Request):
    raw_body = request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    
    try:
        item = Item.parse_obj(data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    return item
