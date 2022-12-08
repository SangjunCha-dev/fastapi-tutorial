from typing import Union

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Get Current User
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


# Create a user model
class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[str, None] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", 
        email="john@example.com",
        full_name="John Doe",
    )


# Create a get_current_user dependency
# Get the user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    return fake_decode_token(token)


# Code size
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
