from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# HTTPSRedirectMiddleware
app.add_middleware(HTTPSRedirectMiddleware)

# TrustedHostMiddleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["example.com", "*.example.com"]
)

# GZipMiddleware
app.add_middleware(
    GZipMiddleware,
    mininum_size=1000,
)


@app.get("/")
def main():
    return {"message": "Hello World"}


@app.get("/2")
def main2():
    return "somebigcontent"
