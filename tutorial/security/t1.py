from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


"""
现在，我们回过头来介绍这段代码的原理。

Password 流是 OAuth2 定义的，用于处理安全与身份验证的方式（流）。

OAuth2 的设计目标是为了让后端或 API 独立于服务器验证用户身份。

但在本例中，FastAPI 应用会处理 API 与身份验证。

下面，我们来看一下简化的运行流程：

用户在前端输入 username 与password，并点击回车
（用户浏览器中运行的）前端把 username 与password 发送至 API 中指定的 URL（使用 tokenUrl="token" 声明）
API 检查 username 与password，并用令牌（Token） 响应（暂未实现此功能）：
令牌只是用于验证用户的字符串
一般来说，令牌会在一段时间后过期
过时后，用户要再次登录
这样一来，就算令牌被人窃取，风险也较低。因为它与永久密钥不同，在绝大多数情况下不会长期有效
前端临时将令牌存储在某个位置
用户点击前端，前往前端应用的其它部件
前端需要从 API 中提取更多数据：
为指定的端点（Endpoint）进行身份验证
因此，用 API 验证身份时，要发送值为 Bearer + 令牌的请求头 Authorization
假如令牌为 foobar，Authorization 请求头就是： Bearer foobar
"""
