from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# curl -X 'POST' \
#   'http://127.0.0.1:8000/items/?name=qqq' \
#   -H 'accept: application/json' \
#   -d ''
