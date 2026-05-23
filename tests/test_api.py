from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["status"] == "success"


def test_prediction():

    payload = {
        "Pclass": 1,
        "Sex": 1,
        "Age": 25,
        "SibSp": 0,
        "Parch": 0,
        "Fare": 100
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "result" in data