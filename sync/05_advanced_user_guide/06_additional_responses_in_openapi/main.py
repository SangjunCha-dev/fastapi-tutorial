from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


# Additional Response with model
@app.get(
    "/items/{item_id}", 
    response_model=Item, 
    responses={404: {"model": Message}}
)
def read_item(item_id: str):
    if item_id == "foo":
        return {
            "id": "foo", 
            "value": "there goes my hero"
        }
    return JSONResponse(
        status_code=404, 
        content={"message": "Item not found"}
    )


# Additional media types for the main response
@app.get(
    "/items2/{item_id}",
    response_model=Item,
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return the JSON item or an image.",
        }
    },
)
def read_item(item_id: str, img: Union[bool, None] = None):
    if img:
        return FileResponse(
            "image.png", 
            media_type="image/png"
        )
    else:
        return {
            "id": "foo", 
            "value": "there goes my hero"
        }


# Combining information
@app.get(
    "/items3/{item_id}",
    response_model=Item,
    responses={
        404: {"model": Message, "description": "The item was not found"},
        200: {
            "description": "Item requested by ID",
            "content": {
                "application/json": {
                    "example": {"id": "bar", "value": "The bar tenders"}
                }
            },
        },
    },
)
def read_item(item_id: str):
    if item_id == "foo":
        return {
            "id": "foo", 
            "value": "there goes my hero"
        }
    else:
        return JSONResponse(
            status_code=404, 
            content={"message": "Item not found"}
        )


# Combine predefined responses and custom ones
responses = {
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
    404: {"description": "Item not found"},
}


@app.get(
    "/items4/{item_id}",
    response_model=Item,
    responses={
        **responses,
        200: {"content": {"image/png": {}}}
    },
)
def read_item(item_id: str, img: Union[bool, None] = None):
    if img:
        return FileResponse(
            "image.png", 
            media_type="image/png"
        )
    else:
        return {
            "id": "foo",
            "value": "there goes my hero",
        }
