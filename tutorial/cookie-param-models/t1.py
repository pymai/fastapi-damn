from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies

# 请记住，由于浏览器以特殊方式处理 cookie，并在后台进行操作，因此它们不会轻易允许 JavaScript 访问这些 cookie。
# 如果您访问 /docs 的 API 文档 UI，您将能够查看您路径操作的 cookie 文档。
# 但是即使您填写数据并点击“执行”，由于文档界面使用 JavaScript，cookie 将不会被发送。而您会看到一条错误消息，就好像您没有输入任何值一样。
