from typing import Union

from fastapi import FastAPI, Depends

app = FastAPI()


# Import Depends
def common_parameters(
    q: Union[str, None] = None,
    skip: int = 0,
    limit: int = 100,
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
def read_item(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
def read_users(commons: dict = Depends(common_parameters)):
    return commons
