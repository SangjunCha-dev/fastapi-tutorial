from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, escape, request

flask_app = Flask(__name__)


@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"


app = FastAPI()


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}

# Using WSGIMiddleware
app.mount("/v1", WSGIMiddleware(flask_app))
