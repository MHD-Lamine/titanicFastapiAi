from fastapi import APIRouter
from app.schemas.passenger import Passenger
from app.services.prediction_service import predict_survival

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "Titanic AI API is running"
    }

@router.post("/predict")
def predict(passenger: Passenger):

    prediction = predict_survival(passenger)

    result = "Survived" if prediction == 1 else "Did not survive"

    return {
        "prediction": prediction,
        "result": result
    }