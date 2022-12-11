from fastapi import FastAPI

# Top-level application
app = FastAPI()

@app.get("/app")
def read_main():
    return {
        "message": "Hello World from main app"
    }


# Sub-application
subapi = FastAPI()

@subapi.get("/sub")
def read_sub():
    return {
        "message": "Hello World from sub API"
    }

app.mount("/subapi", subapi)
