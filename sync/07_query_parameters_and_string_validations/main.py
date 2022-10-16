from typing import Union

from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get("/items/")
def read_items(q: Union[str, None] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Additional validation - 추가 검증
# Use Query as the default value - 쿼리를 기본값으로 사용
@app.get("/items2/")
def read_items2(
    q: Union[str, None] = Query(default=None, max_length=50)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Add more validations - 더 많은 유효성 검사 추가
@app.get("/items3/")
def read_items3(
    q: Union[str, None] = Query(default=None, min_length=3, max_length=50)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Add regular expressions - 정규식 추가
@app.get("/items4/")
def read_items4(
    q: Union[str, None] = Query(
        default=None, min_length=3, max_length=50, regex="^fixedquery$"
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Default values - 기본값
@app.get("/items5/")
def read_items5(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Make it required - 필수값 사용
@app.get("/items6/")
def read_items6(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Required with Ellipsis (...) - 줄임표로 필수값 사용
@app.get("/items7/")
def read_items7(q: str = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Required with None - None 또는 필수값 사용
@app.get("/items8/")
def read_items8(q: Union[str, None] = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Use Pydantic's Required instead of Ellipsis (...) - pydantic 필수값 사용
@app.get("/items9/")
def read_items9(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query parameter list / multiple values - 쿼리 매개변수 목록/여러 값
@app.get("/items10/")
def read_items10(q: Union[list[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items


# Query parameter list / multiple values with defaults - 쿼리 매개변수 목록/기본값이 있는 여러 값
@app.get("/items11/")
def read_items11(q: list[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# Using list - list 사용
@app.get("/items12/")
def read_items12(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items


# Declare more metadata - 더 많은 메타데이터 선언
@app.get("/items13/")
def read_items13(
    q: Union[str, None] = Query(default=None, title="Query string", min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items14/")
def read_items14(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Alias parameters - 별칭 매개변수
@app.get("/items15/")
def read_items15(
    q: Union[str, None] = Query(default=None, alias="item-query")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Deprecating parameters - 매개변수 지원 중단
@app.get("/items16/")
def read_items16(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Exclude from OpenAPI - OpenAPI에서 제외
@app.get("/items17/")
def read_items17(
    hidden_query: Union[str, None] = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
