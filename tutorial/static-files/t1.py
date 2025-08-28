from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

path = "./static"
os.makedirs(path, exist_ok=True)
app.mount("/static", StaticFiles(directory=path), name="static")

# http://127.0.0.1:8000/static/1.txt
