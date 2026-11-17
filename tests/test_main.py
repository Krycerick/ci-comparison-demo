from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add():
    response = client.get("/add/2/3")
    assert response.json() == {"result": 6}


def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 400
