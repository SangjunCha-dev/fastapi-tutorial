from fastapi import FastAPI

description = """
himichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        }
    }
]

app = FastAPI(
    openapi_url="/api/v1/openapi.json",  # default: /openapi.json
    openapi_tags=tags_metadata,

    title="ChimichangApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },

    docs_url="/docs",  # default: /docs
    redoc_url=None,  # default: /redoc
)


@app.get("/items/")
def read_items():
    return [{"name": "Katana"}]


@app.get("/users/", tags=["users"])
def get_users():
    return [
        {"name": "Harry"},
        {"name": "Ron"},
    ]


@app.get("/items2/", tags=["items"])
def get_items():
    return [
        {"name": "wand"},
        {"name": "flying broom"},
    ]
