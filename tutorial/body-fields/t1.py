from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/items/3' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "item": {
#     "name": "banana",
#     "description": "fruit",
#     "price": 4.0,
#     "tax": 1.0
#   }
# }'

# 实际上，Query、Path 都是 Params 的子类，而 Params 类又是 Pydantic 中 FieldInfo 的子类。
# Pydantic 的 Field 返回也是 FieldInfo 的类实例。
# Body 直接返回的也是 FieldInfo 的子类的对象。后文还会介绍一些 Body 的子类。
# 注意，从 fastapi 导入的 Query、Path 等对象实际上都是返回特殊类的函数。
