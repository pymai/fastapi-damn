from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


# Don't do this in production!
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user

# curl -X 'POST' \
#   'http://127.0.0.1:8000/user/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "username": "foo",
#   "password": "zzz",
#   "email": "user@example.com",
#   "full_name": "foobar"
# }'
