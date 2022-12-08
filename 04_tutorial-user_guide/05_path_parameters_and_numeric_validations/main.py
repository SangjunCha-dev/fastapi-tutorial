from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()


# Import Path - 경로 가져오기
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Declare metadata - 메타데이터 선언
@app.get("/items2/{item_id}")
async def read_items2(    
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Order the parameters as you need - 매개변수 메타데이터 순서 상관없이 선언
@app.get("/items3/{item_id}")
async def read_items3(
    q: str,
    item_id: int = Path(title="The ID of the item to get"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Order the parameters as you need, tricks - 매개변수 기본값 선언 순서상관없이 사용방법
@app.get("/items4/{item_id}")
async def read_items4(
    *, 
    item_id: int = Path(title="The ID of the item to get"),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Number validations: greater than or equal - 숫자 검증: 크거나 같음
@app.get("/items5/{item_id}")
async def read_items5(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=1),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Number validations: greater than and less than or equal - 숫자 검증: 크거나 작거나 같음
@app.get("/items6/{item_id}")
async def read_items6(
    *,
    item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Number validations: floats, greater than and less than - 숫자 유효성 검사: float, 보다 큼 및 보다 작음
@app.get("/items7/{item_id}")
async def read_items7(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
