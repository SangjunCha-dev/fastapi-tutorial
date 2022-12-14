from fastapi import FastAPI, status

app = FastAPI()


# About HTTP status codes
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}


# Shortcut to remember the names
@app.post("/items2/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
