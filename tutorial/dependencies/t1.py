from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/?q=zzz&skip=1&limit=100' \
#   -H 'accept: application/json'

# curl -X 'GET' \
#   'http://127.0.0.1:8000/users/?q=zzz&skip=1&limit=99' \
#   -H 'accept: application/json'
