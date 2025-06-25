from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 路径参数
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# 查询参数
@app.get("/items/")
# 默认参数
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# 对比路径参数和查询参数，就是变量是否 放路径 里
@app.get("/items-old/")
async def read_item(skip, limit):
    return fake_items_db[int(skip): int(skip) + int(limit)]

# curl -X 'GET' \
#   'http://127.0.0.1:8000/items/?skip=0&limit=3' \
#   -H 'accept: application/json'
