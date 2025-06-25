from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# pip install fastapi-cli
# cd tutorial/first-steps
# fastapi dev main.py
