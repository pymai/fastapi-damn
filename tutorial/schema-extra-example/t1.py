from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/111' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "foo",
#   "description": "zzz",
#   "price": 3.0,
#   "tax": 4.0
# }'

# Response body
# {
#   "item_id": 111,
#   "item": {
#     "name": "foo",
#     "description": "zzz",
#     "price": 3,
#     "tax": 4,
#     "model_config": {
#       "json_schema_extra": {
#         "examples": [
#           {
#             "name": "Foo",
#             "description": "A very nice Item",
#             "price": 35.4,
#             "tax": 3.2
#           }
#         ]
#       }
#     }
#   }
# }
