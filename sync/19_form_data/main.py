from fastapi import FastAPI, Form

app = FastAPI()


# Define Form parameters
@app.post("/login/")
def login(username: str = Form(), password: str = Form()):
    return {"username": username}
