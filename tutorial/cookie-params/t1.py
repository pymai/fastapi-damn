from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    print("Cookie", ads_id)
    return {"ads_id": ads_id}

# 必须使用 Cookie 声明 cookie 参数，否则该参数会被解释为查询参数。

# curl -H "Cookie: ads_id=zzz" http://localhost:8000/items/

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Cookie: ads_id=fafafafafafafaf'
