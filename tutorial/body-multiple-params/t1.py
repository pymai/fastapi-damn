from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
        q: str | None = None,
        item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/1?q=zzz' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "foo",
#   "description": "bar",
#   "price": 1.0,
#   "tax": 0.5
# }'
