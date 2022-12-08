import time

from fastapi import FastAPI, Request

app = FastAPI()


# Create a middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # Before and after the response
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    # 요청 처리시간을 담은 사용자 지정 헤더
    response.headers["X-Process-Time"] = str(process_time)

    return response
