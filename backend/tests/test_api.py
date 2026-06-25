from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert "Hey" in response.json()


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "Ok"
    assert "model_version" in data
    assert "model" in data
    assert data["model"] is True


def test_predict_endpoint_valid_input():
    payload = {
        "Hours_Studied": 5,
        "Previous_Scores": 80,
        "Extracurricular_Activities": "Yes",
        "Sleep_Hours": 7,
        "Sample_Question_Papers_Practiced": 4
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert "Grade" in data


def test_predict_endpoint_missing_field():
    payload = {
        "Hours_Studied": 5,
        "Previous_Scores": 80,
        "Extracurricular_Activities": "Yes",
        "Sleep_Hours": 7
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422