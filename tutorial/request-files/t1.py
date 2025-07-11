from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# curl -X 'POST' \
#   'http://127.0.0.1:8000/files/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'file=@WechatIMG2197.jpg;type=image/jpeg'

# curl -X 'POST' \
#   'http://127.0.0.1:8000/uploadfile/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'file=@WechatIMG2197.jpg;type=image/jpeg'
