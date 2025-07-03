from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/555' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "orange",
#   "description": "fruit",
#   "price": 5.0,
#   "tax": 0.1,
#   "tags": ["orange", "fruit"],
#   "image": {
#     "url": "http://www.baidu.com",
#     "name": "bidu"
#   }
# }'
