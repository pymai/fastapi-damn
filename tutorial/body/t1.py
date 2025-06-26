from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

# curl -X 'POST' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "string",
#   "description": "string",
#   "price": 0,
#   "tax": 0
# }'
