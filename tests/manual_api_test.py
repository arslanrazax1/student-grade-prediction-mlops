import requests


BASE_URL = "http://localhost:8000"


def test_home():
    response = requests.get(f"{BASE_URL}/")
    print("Home Status:", response.status_code)
    print("Home Response:", response.json())


def test_health():
    response = requests.get(f"{BASE_URL}/health")
    print("Health Status:", response.status_code)
    print("Health Response:", response.json())


def test_prediction():
    payload = {
        "Hours_Studied": 7,
        "Previous_Scores": 80,
        "Extracurricular_Activities": "Yes",
        "Sleep_Hours": 7,
        "Sample_Question_Papers_Practiced": 6
    }

    response = requests.post(f"{BASE_URL}/predict", json=payload)
    print("Prediction Status:", response.status_code)
    print("Prediction Response:", response.json())


if __name__ == "__main__":
    test_home()
    print("-" * 50)

    test_health()
    print("-" * 50)

    test_prediction()