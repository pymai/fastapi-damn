from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
        q: str | None = Query(
            default=None, min_length=3, max_length=50, pattern="^fixedquery$"
        ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    print("q", q)
    if q:
        results.update({"q": q})
    return results

# 限制了 pattern="^fixedquery$" ，但在浏览器访问 http://127.0.0.1:8000/items/?q=fix 依然返回了结果？
