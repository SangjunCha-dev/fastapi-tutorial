from typing import Union

from fastapi import Cookie, FastAPI

app = FastAPI()


# Import Cookie
@app.get("/items/")
def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}
