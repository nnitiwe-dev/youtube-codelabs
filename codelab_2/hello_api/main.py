# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Initialize FastAPI app
app = FastAPI(title="FastAPI Basics", description="A beginner-friendly FastAPI tutorial - Inventory Demo", version="1.0.0")

# In-memory storage (demo purposes)
db = []

# Define data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

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
    return {"error": "Item not found"}

# Add new item
@app.post("/items")
def create_item(item: Item):
    db.append(item.dict())
    return {"message": "Item added successfully", "item": item}

# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(db):
        if existing_item["id"] == item_id:
            db[i] = item.dict()
            return {"message": "Item updated", "item": item}
    return {"error": "Item not found"}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(db):
        if item["id"] == item_id:
            del db[i]
            return {"message": "Item deleted"}
    return {"error": "Item not found"}


if __name__ == "__main__":
    import subprocess
    subprocess.run(["gunicorn","main:app","--workers","4","--worker-class","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:8000","--reload"])