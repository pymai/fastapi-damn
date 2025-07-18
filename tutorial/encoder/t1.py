from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(json_compatible_item_data)
    print(fake_db)

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/1' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "title": "foobar",
#   "timestamp": "2025-07-15T06:55:00.948Z",
#   "description": "barfoo"
# }'
