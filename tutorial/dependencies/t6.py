from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}


class OwnerError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")


@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    # plumbus Rick
    print(item_id, username)
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    item = data[item_id]
    # item["owner"] --> Morty
    print(item["owner"])
    if item["owner"] != username:
        # raise 了 OwnerError(Rick)
        raise OwnerError(username)
    return item

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/plumbus' \
#   -H 'accept: application/json'

# Response body
# {
#   "detail": "Owner error: Rick"
# }

# 问题？？？
# OwnerError(username) 不是 yield "Rick" 了吗，为什么会输出 Owner error: Rick
