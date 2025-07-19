from fastapi import APIRouter, HTTPException
from services.items_service import get_item, list_items
from pydantic import BaseModel, Field

class Item(BaseModel):
    """
    Represents an item with a price.
    """
    id: int = Field(..., example=1, description="Unique identifier for the item")
    name: str = Field(..., example="Item One", description="Name of the item")
    price: float = Field(..., example=9.99, description="Price of the item in USD")

router = APIRouter()

@router.get(
    "/",
    response_model=list[Item],
    summary="List all items",
    description="Retrieve a list of all available items.",
    responses={200: {"description":"List retrieved successfully"}}
)
async def read_items():
    """Fetch all items."""
    return list_items()

@router.get(
    "/{item_id}",
    response_model=Item,
    summary="Get a single item",
    description="Fetch detailed information about an item by ID.",
    responses={404: {"description":"Item not found"}}
)
async def read_item(item_id: int):
    """
    Get item by ID.
    - **item_id**: integer ID of the item to retrieve
    """
    item = get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item