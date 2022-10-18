from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# Import Field
# Declare model attributes
class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item = Body(embed=True)):
    return {"item_id": item_id, "item": item}
