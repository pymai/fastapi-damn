from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/4' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "item": {
#     "name": "apple",
#     "description": "fruit",
#     "price": 10.0,
#     "tax": 5.0
#   }
# }'
