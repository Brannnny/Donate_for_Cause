from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created", "item": item}

# {
#   "name": "Laptop",
#   "price": 1299.99,
#   "description": "High-performance laptop"
# }
