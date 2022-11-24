from typing import Union

from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse

app = FastAPI()

items = {
    "foo": {"name": "Fighters", "size": 6},
    "bar": {"name": "Tenders", "size": 3},
}


@app.put("/items/{item_id}")
def upsert_item(
    item_id: str, 
    name: Union[str, None] = Body(default=None),
    size: Union[int, None] = Body(default=None),
):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        # Additional status codes
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)
