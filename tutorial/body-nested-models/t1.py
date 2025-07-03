from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# tags: list = [] ，值一定要指定为 "" 的 json 格式
# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/55' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "banana",
#   "description": "fruit",
#   "price": 3.0,
#   "tax": 1.0,
#   "tags": ["1","a","-"]
# }'
