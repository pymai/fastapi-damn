from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
        file: Annotated[bytes, File()],
        fileb: Annotated[UploadFile, File()],
        token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

# curl -X 'POST' \
#   'http://127.0.0.1:8000/files/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'file=@WechatIMG2197.jpg;type=image/jpeg' \
#   -F 'fileb=@HK_Stk_Sample_20250430_hi.rar;type=application/x-rar' \
#   -F 'token=aaa'
