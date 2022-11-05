from fastapi import FastAPI, Depends, Header, HTTPException


def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(
    dependencies=[
        Depends(verify_token), 
        Depends(verify_key),
    ]
)


@app.get("/items/")
def read_items():
    return [
        {"item": "Portal Gun"}, 
        {"item": "Plumbus"},
    ]


@app.get("/users/")
def read_users():
    return [
        {"username": "Rick"},
        {"username": "Morty"},
    ]
