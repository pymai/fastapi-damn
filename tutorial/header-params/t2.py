from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: list[str] | None = Header(default=None)):
    print("x_token", x_token)
    return {"X-Token values": x_token}

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'x-token: foobar,zzz'
