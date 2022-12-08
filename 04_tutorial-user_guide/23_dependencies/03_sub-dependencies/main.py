from typing import Union

from fastapi import FastAPI, Cookie, Depends

app = FastAPI()


# First dependency "dependable"
def query_extractor(q: Union[str, None] = None):
    return q


# Second dependency, "dependable" and "dependant"
def query_or_cookie_extractor(
    q: str = Depends(query_extractor),
    last_query: Union[str, None] = Cookie(default=None),
):
    if not q:
        return last_query
    return q


# Use the dependency
@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


# Using the same dependency multiple times
@app.get("/items2/")
async def needy_dependency(fresh_value: str = Depends(query_extractor, use_cache=False)):
    return {"fresh_value": fresh_value}
