from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles

# Change Default Swagger UI Parameters
swagger_ui_default_parameters = {
    "dom_id": "#swagger-ui",
    "layout": "BaseLayout",
    "deepLinking": True,
    "showExtensions": True,
    "showCommonExtensions": True,
}


# Disable the automatic docs
app = FastAPI(
    docs_url=None, 
    redoc_url=None,
    # Disable Syntax Highlighting
    # swagger_ui_parameters={"syntaxHighlight": False},
    # Change the Theme
    # swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
    # Change Default Swagger UI Parameters
    swagger_ui_parameters={"deepLinking": False},
)


# Normal FastAPI
@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]


def custom_openapi():
    # Cache the OpenAPI schem
    if app.openapi_schema:
        return app.openapi_schema
    # Generate the OpenAPI schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    # Modify the OpenAPI schema
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Override the method
app.openapi = custom_openapi


# Serve the static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Include the custom docs
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


# Create a path operation to test it
@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
