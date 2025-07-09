from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


# 但如果它们并没有存储实际的值，你可能想从结果中忽略它们的默认值。
# response_model_exclude_defaults=True
# response_model_exclude_none=True
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/foo' \
#   -H 'accept: application/json'

# Response body
# {
#   "name": "Foo",
#   "price": 50.2
# }

# 使用 response_model_exclude_unset 来仅返回显式设定的值。
