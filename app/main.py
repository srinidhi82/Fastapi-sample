from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .schemas import Item

app = FastAPI(title="Sample API", version="0.1")

# Simple in-memory "DB" for demonstration
fake_db = {}

@app.get("/", tags=["health"])
def read_root():
    return {"message": "Sample API is running"}

@app.get("/items", response_model=list[Item], tags=["items"], responses={200: {"description": "List of items"}})
def list_items():
    """Return all items"""
    return list(fake_db.values())

@app.get("/items/{item_id}", response_model=Item, tags=["items"])
def get_item(item_id: int):
    """Get an item by ID"""
    item = fake_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post(
    "/items",
    status_code=201,
    response_model=Item,
    tags=["items"],
    responses={
        201: {
            "content": {
                "application/json": {
                    "example": {"id": 1, "name": "Sample", "description": "A sample item"}
                }
            }
        }
    },
)
def create_item(item: Item):
    """Create a new item"""
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item

@app.put(
    "/items/{item_id}",
    response_model=Item,
    tags=["items"],
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": {"id": 1, "name": "Updated", "description": "Updated description"}
                }
            }
        }
    },
)
def update_item(item_id: int, item: Item):
    """Update an existing item (path id must match body id)"""
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    if item_id != item.id:
        raise HTTPException(status_code=400, detail="ID in path and body must match")
    fake_db[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204, tags=["items"], responses={204: {"description": "Item deleted"}})
def delete_item(item_id: int):
    """Delete an item by ID"""
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return JSONResponse(status_code=204, content=None)
