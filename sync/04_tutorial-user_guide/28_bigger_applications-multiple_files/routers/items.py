from fastapi import APIRouter, Depends, HTTPException

# Import the dependencies
# from ..dependencies import get_token_header
from dependencies import get_token_header

# Another module with APIRouter
router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {
    "plumbus": {"name": "Plumbus"},
    "gun": {"name": "Portal Gun"},
}


@router.get("/")
def read_items():
    return fake_items_db


@router.get("/{item_id}")
def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=400, detail="Item not found")
    return {
        "name": fake_items_db[item_id]["name"],
        "item_id": item_id,
    }


# Add some custom tags, responses, and dependencies
@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus",
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
