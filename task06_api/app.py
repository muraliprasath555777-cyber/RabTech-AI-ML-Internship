from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from pathlib import Path


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="Customer Churn Prediction API",
    description="REST API for customer churn prediction using the Task 04 champion model.",
    version="1.0.0"
)


# ============================================================
# Load Champion Model
# ============================================================

MODEL_PATH = Path(__file__).parent / "task04_champion_model.joblib"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    MODEL_LOAD_ERROR = str(e)


# ============================================================
# Request Schema
# ============================================================

class PredictionRequest(BaseModel):
    tenure_months: int = Field(..., ge=0)
    support_tickets: int = Field(..., ge=0)
    monthly_spend_inr: float = Field(..., ge=0)
    last_login_days: int = Field(..., ge=0)
    plan_type: str


# ============================================================
# Root Endpoint
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Customer Churn Prediction API is running",
        "version": "1.0.0",
        "endpoint": "/predict"
    }


# ============================================================
# Health Check Endpoint
# ============================================================

@app.get("/health")
def health():

    if model is None:
        return {
            "status": "unhealthy",
            "model_loaded": False
        }

    return {
        "status": "healthy",
        "model_loaded": True
    }


# ============================================================
# Prediction Endpoint
# ============================================================

@app.post("/predict")
def predict(request: PredictionRequest):

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Champion model could not be loaded."
        )

    # Create input DataFrame with the exact
    # five features used during Task 04 training.
    input_data = pd.DataFrame([{
        "tenure_months": request.tenure_months,
        "support_tickets": request.support_tickets,
        "monthly_spend_inr": request.monthly_spend_inr,
        "last_login_days": request.last_login_days,
        "plan_type": request.plan_type
    }])

    try:
        # Prediction
        prediction = int(model.predict(input_data)[0])

        response = {
            "prediction": prediction
        }

        # Prediction probabilities
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]

            response["probabilities"] = {
                str(index): round(float(probability), 6)
                for index, probability in enumerate(probabilities)
            }

            response["confidence"] = round(
                float(max(probabilities)),
                6
            )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )