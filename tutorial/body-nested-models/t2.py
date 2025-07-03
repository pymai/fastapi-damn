from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# tags: list[str] = [] 会自动把值转换为字符串
# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/222' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "apple",
#   "description": "fruit",
#   "price": 0.5,
#   "tax": 0.1,
#   "tags": [1, 2]
# }'
