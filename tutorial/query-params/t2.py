from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
# 可选参数
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
