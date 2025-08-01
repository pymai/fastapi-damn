from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    print("stored_item_model", stored_item_model)
    update_data = item.dict(exclude_unset=True)
    print("update_data", update_data)
    updated_item = stored_item_model.copy(update=update_data)
    print("updated_item", updated_item)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item

# name='Bar' description='The bartenders' price=62.0 tax=20.2 tags=[]
# {'name': 'Foo', 'description': None, 'price': 50.2, 'tax': 10.5, 'tags': []}
# name='Foo' description=None price=50.2 tax=10.5 tags=[]
