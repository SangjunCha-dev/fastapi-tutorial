from dataclasses import dataclass, field
from typing import Union

from fastapi import FastAPI


@dataclass
class Item:
    name: str
    price: float
    description: Union[str, None] = None
    tax: Union[float, None] = None

app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    return item


# Dataclasses response_model
@dataclass
class Item2:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)
    description: Union[str, None] = None
    tax: Union[float, None] = None


@app.get("/items2/next", response_model=Item)
def read_next_item():
    return {
        "name": "Island In The Moon",
        "price": 12.99,
        "description": "A place to be be playin' and havin' fun",
        "tags": ["breater"],
    }


# Dataclasses in Nested Data Structures
from dataclasses import field
from pydantic.dataclasses import dataclass


@dataclass
class Item3:
    name: str
    description: Union[str, None] = None


@dataclass
class Author3:
    name: str
    items: list[Item3] = field(default_factory=list)


@app.post("/authors/{author_id}/items/", response_model=Author3)
def create_author_items(author_id: str, items: list[Item3]):
    return {
        "name": author_id,
        "items": items,
    }


@app.get("/authors/", response_model=list[Author3])
def get_authors():
    return [
        {
            "name": "Breaters",
            "items": [
                {
                    "name": "Island In The Moon",
                    "description": "A place to be be playin' and havin' fun",
                },
                {
                    "name": "Holy Buddies",
                },
            ],
        },
        {
            "name": "System of an Up",
            "items": [
                {
                    "name": "Salt",
                    "description": "The kombucha mushroom people's favorite",
                },
                {
                    "name": "Pad Thai",
                },
                {
                    "name": "Lonely Night",
                    "description": "The mostests lonliest nightiest of allest",
                },
            ],
        },
    ]
