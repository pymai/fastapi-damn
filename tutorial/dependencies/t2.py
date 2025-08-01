from fastapi import Depends, FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/?q=zzz&skip=0&limit=1' \
#   -H 'accept: application/json'

# Response body
# {
#   "q": "zzz",
#   "items": [
#     {
#       "item_name": "Foo"
#     }
#   ]
# }
