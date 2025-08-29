from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


# 直接运行这个文件，不用运行 fastapi dev main.py

"""
(fastapi-env) ➜  app git:(main) ✗ pytest 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.11.3, pytest-7.3.2, pluggy-1.0.0
rootdir: /PycharmProjects/fastapi-damn/tutorial/testing/app
plugins: anyio-3.7.0
collected 1 item                                                                                                                                                                                                                       

test_main.py .                                                                                                                                                                                                                   [100%]

========================================================================================================== 1 passed in 0.22s ===========================================================================================================
"""
