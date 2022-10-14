from fastapi import FastAPI

app = FastAPI()


# path-parameters-with-types
@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items2/{item_id}")
def read_item2(item_id: int):
    return {"item_id": item_id}


# Order matters
@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users")
def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
def read_users2():
    return ["Bean", "Elfo"]


# Predefined values
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    model_info = {"model_name": model_name}

    if model_name is ModelName.alexnet:
        model_info["message"] = "Deep Learning FTW!"
        return model_info
    
    if model_name.value == "lenet":
        model_info["message"] = "LeCNN all the images"
        return model_info
    
    model_info["message"] = "Have some residuals"
    return model_info


# Path convertor
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}
