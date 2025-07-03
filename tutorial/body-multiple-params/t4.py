from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(gt=0),
        q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/3?q=zzz' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "item": {
#     "name": "apple",
#     "description": "fruit",
#     "price": 3.0,
#     "tax": 0.5
#   },
#   "user": {
#     "username": "bar",
#     "full_name": "foobar"
#   },
#   "importance": 1
# }'