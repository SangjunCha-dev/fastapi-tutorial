from fastapi import FastAPI, Request

# Setting the root_path in the FastAPI app
app = FastAPI(
    root_path="/api/v1",

    # Additional servers
    servers=[
        {
            "url": "https://stag.example.com",
            "description": "Staging environment",
        },
        {
            "url": "https://prod.example.com",
            "description": "Production environment",
        },
    ],

    # Disable automatic server from root_path
    root_path_in_servers=False,
)


# Checking the current root_path
@app.get("/app")
def read_main(request: Request):
    return {
        "message": "Hello World",
        "root_path": request.scope.get("root_path"),
    }
