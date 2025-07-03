from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images


# curl -X 'POST' \
#   'http://127.0.0.1:8000/images/multiple/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '[
#   {
#     "url": "http://www.baidu.com",
#     "name": "bidu"
#   },
#     "url": "http://www.baidu2.com",
#     "name": "bidu2"
#   },
# ]'
