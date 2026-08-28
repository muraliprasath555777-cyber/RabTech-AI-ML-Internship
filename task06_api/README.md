# Customer Churn Prediction API

## Overview

This project packages the Task 04 champion machine-learning model
as a REST API using FastAPI.

The API accepts customer feature input and returns a churn prediction,
prediction probabilities, and confidence.

## Project Structure

```text
task06_api/
├── app.py
├── requirements.txt
├── Dockerfile
├── test_app.py
└── task04_champion_model.joblib