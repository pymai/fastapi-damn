from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    for x, y in weights.items():
        print(type(x), type(y))
    return weights

# curl -X 'POST' \
#   'http://127.0.0.1:8000/index-weights/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "1": 2
# }'
