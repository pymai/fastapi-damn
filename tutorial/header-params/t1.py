from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}

# 必须使用 Header 声明 header 参数，否则该参数会被解释为查询参数

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
