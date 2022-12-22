# Create the Pydantic models
from typing import Union

from pydantic import BaseModel


# Create initial Pydantic models / schemas
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


# Create Pydantic models / schemas for reading / returning
class Item(ItemBase):
    id: int
    owner_id: int

    # Use Pydantic's orm_mode
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
