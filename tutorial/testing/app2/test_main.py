from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_read_nonexistent_item():
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Item already exists"}


"""
/miniconda3/envs/fastapi-env/bin/python /Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /PycharmProjects/fastapi-damn/tutorial/testing/app2/test_main.py 
Testing started at 16:57 ...
Launching pytest with arguments /PycharmProjects/fastapi-damn/tutorial/testing/app2/test_main.py --no-header --no-summary -q in /PycharmProjects/fastapi-damn/tutorial/testing

============================= test session starts ==============================
collecting ... collected 6 items

app2/test_main.py::test_read_item PASSED                                 [ 16%]
app2/test_main.py::test_read_item_bad_token PASSED                       [ 33%]
app2/test_main.py::test_read_nonexistent_item PASSED                     [ 50%]
app2/test_main.py::test_create_item PASSED                               [ 66%]
app2/test_main.py::test_create_item_bad_token PASSED                     [ 83%]
app2/test_main.py::test_create_existing_item PASSED                      [100%]

============================== 6 passed in 0.27s ===============================

Process finished with exit code 0

"""

"""
(fastapi-env) ➜  app2 git:(main) ✗ pytest 
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.11.3, pytest-7.3.2, pluggy-1.0.0
rootdir: PycharmProjects/fastapi-damn/tutorial/testing/app2
plugins: anyio-3.7.0
collected 6 items                                                                                                                                                                                                                      

test_main.py ......                                                                                                                                                                                                              [100%]

========================================================================================================== 6 passed in 0.22s ===========================================================================================================
(fastap
"""
