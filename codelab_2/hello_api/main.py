# main.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Basics",
    description="A beginner-friendly FastAPI tutorial - Inventory Demo",
    version="1.0.0"
)

# In-memory storage (demo purposes)
db = []

# Define data model with validation
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float = Field(..., ge=0)  # Ensure price is non-negative

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI 🎉"}

# Get all items
@app.get("/items")
def get_items():
    return db

# Get single item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

# Add new item
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    # Check for duplicate ID
    for existing_item in db:
        if existing_item["id"] == item.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item with this ID already exists")
    db.append(item.dict())
    return {"message": "Item added successfully", "item": item}

# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item.id != item_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID in body does not match URL")
    for i, existing_item in enumerate(db):
        if existing_item["id"] == item_id:
            db[i] = item.dict()
            return {"message": "Item updated", "item": item}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(db):
        if item["id"] == item_id:
            del db[i]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


if __name__ == "__main__":
    import subprocess
    subprocess.run(["gunicorn","main:app","--workers","4","--worker-class","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:8000","--reload"])