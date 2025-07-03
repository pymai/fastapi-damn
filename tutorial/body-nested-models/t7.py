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
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# curl -X 'POST' \
#   'http://127.0.0.1:8000/offers/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "foobar",
#   "description": "work",
#   "price": 2000.0,
#   "items": [
#     {
#       "name": "ops",
#       "description": "daza",
#       "price": 1.0,
#       "tax": 0.5,
#       "tags": ["ops", "dev"],
#       "images": [
#         {
#           "url": "http://www.baidu.com",
#           "name": "bidu"
#         },
#         {
#           "url": "http://www.baidu.com",
#           "name": "bidu"
#         }
#       ]
#     }
#   ]
# }'
