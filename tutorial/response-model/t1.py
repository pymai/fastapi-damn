from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json'

# Response body
# [
#   {
#     "name": "Portal Gun",
#     "description": null,
#     "price": 42,
#     "tax": null,
#     "tags": []
#   },
#   {
#     "name": "Plumbus",
#     "description": null,
#     "price": 32,
#     "tax": null,
#     "tags": []
#   }
# ]

# curl -X 'POST' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "apple",
#   "description": "fruit",
#   "price": 0.3,
#   "tax": 0.05,
#   "tags": ["a","b"]
# }'
