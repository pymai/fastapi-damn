from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
# FastAPI 使用 Python 类型声明实现了数据校验
# 入参加了校验 "msg": "value is not a valid integer"
async def read_item(item_id: int):
    return {"item_id": item_id}
