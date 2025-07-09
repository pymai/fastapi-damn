from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/set_cookie/")
async def set_cookie(response: Response):
    response.set_cookie(key="ads_id", value="foobar")
    return {"message": "Cookie set"}

# curl -X 'GET' \
#   'http://127.0.0.1:8000/set_cookie/' \
#   -H 'accept: application/json'
