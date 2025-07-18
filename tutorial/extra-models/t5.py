from fastapi import FastAPI

app = FastAPI()


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}


# curl -X 'GET' \
#   'http://127.0.0.1:8000/keyword-weights/' \
#   -H 'accept: application/json'
