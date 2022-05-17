import json
from moneycop.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "I'am Moneycop backend! Check out my API Doc on my /docs URL"}

def test_add_expense():
    json_request = {
        "amount": 20.75,
        "location": "supermarket"
    }

    response = client.post("/expense", json=json_request)
    res = response.json()
    assert res["amount"] == json_request["amount"]
    assert res["location"] == json_request["location"]
    assert response.status_code == 200
