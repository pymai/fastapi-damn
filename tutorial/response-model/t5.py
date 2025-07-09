from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/foo/name' \
#   -H 'accept: application/json'

# Response body

# {
#   "name": "Foo",
#   "description": null
# }

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/baz/public' \
#   -H 'accept: application/json'

# Response body

# {
#   "name": "Baz",
#   "description": "There goes my baz",
#   "price": 50.2
# }
