from typing import Union

from fastapi import FastAPI, Header

app = FastAPI()


# Import Header
# Declare Header parameters
@app.get("/items/")
def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}


# Automatic conversion
@app.get("/items2/")
def read_items2(
    strange_header: Union[str, None] = Header(default=None, convert_underscores=False)
):
    return {"strange_header": strange_header}


# Duplicate headers
@app.get("/items3/")
def read_items3(x_token: Union[list[str], None] = Header(default=None)):
    return {"X-Token values": x_token}
