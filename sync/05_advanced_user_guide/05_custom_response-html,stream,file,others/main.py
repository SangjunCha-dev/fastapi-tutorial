from typing import Any

from fastapi import FastAPI, Response
from fastapi.responses import (ORJSONResponse, HTMLResponse, UJSONResponse, 
                               PlainTextResponse, RedirectResponse, 
                               StreamingResponse, FileResponse)
import orjson

app = FastAPI(default_response_class=ORJSONResponse)


# Use ORJSONResponse
@app.get("/items/", response_class=ORJSONResponse)
def read_items():
    return ORJSONResponse([
        {"item_id": "Foo"}
    ])


# HTML Response
@app.get("/items2/", response_class=HTMLResponse)
def read_items2():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/items3/", response_class=HTMLResponse)
def read_items3():
    return generate_html_response()


# Available responses
@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")


# PlainTextResponse
@app.get("/", response_class=PlainTextResponse)
def main():
    return "Hello World"


# UJSONResponse
@app.get("/items4/", response_class=UJSONResponse)
def read_items4():
    return [{"item_id": "Foo"}]


# RedirectResponse
@app.get("/typer")
def redirect_typer():
    return RedirectResponse("https://typer.tiangolo.com")


@app.get("/pydantic", response_class=RedirectResponse, status_code=302)
def redirect_pydantic():
    return "https://pydantic-docs.helpmanual.io/"


# StreamingResponse
def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"


@app.get("/1")
def main():
    return StreamingResponse(fake_video_streamer())


# Using StreamingResponse with file-like objects
some_file_path = "large-video-file.mp4"

@app.get("/2")
def main():
    def iterfile():
        with open(some_file_path, mode="rb") as file_like:
            yield from file_like
    
    return StreamingResponse(iterfile(), media_type="video/mp4")


# FileResponse
@app.get("/3")
def main():
    return FileResponse(some_file_path)


@app.get("/4", response_class=FileResponse)
def main():
    return some_file_path


# Custom response class
class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)


@app.get("/5", response_class=CustomORJSONResponse)
def main():
    return {"message": "Hello World"}


# Default response class
@app.get("/items5/")
def read_items():
    return [
        {"item_id": "Foo"}
    ]
