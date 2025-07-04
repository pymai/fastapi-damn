from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(title="The ID of the item to get"),
        q: str | None = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# http://127.0.0.1:8000/items/111?item-query=zzz
