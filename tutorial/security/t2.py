from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

# 定义了一个 oauth2_scheme 实例，它会从请求头中读取 token（Authorization: Bearer <token>）
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


"""
示例请求
GET /users/me
Authorization: Bearer abc123

返回结果类似于：
{
  "username": "abc123fakedecoded",
  "email": "john@example.com",
  "full_name": "John Doe",
  "disabled": null
}
"""
