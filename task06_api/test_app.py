from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == \
        "Customer Churn Prediction API is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["model_loaded"] is True


def test_predict():
    sample_features = {
        "tenure_months": 18,
        "support_tickets": 1,
        "monthly_spend_inr": 499,
        "last_login_days": 21,
        "plan_type": "Basic"
    }

    response = client.post(
        "/predict",
        json=sample_features
    )

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert result["prediction"] in [0, 1]

    assert "probabilities" in result
    assert "confidence" in result


def test_predict_invalid_payload():
    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 422