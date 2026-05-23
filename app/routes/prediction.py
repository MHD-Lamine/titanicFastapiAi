from fastapi import APIRouter, HTTPException
from app.schemas.passenger import Passenger
from app.services.prediction_service import predict_survival

router = APIRouter(
    tags=["Prediction"]
)

@router.get("/")
def home():

    return {
        "message": "Titanic AI API is running",
        "status": "success"
    }

@router.post("/predict")
def predict(passenger: Passenger):

    try:

        prediction = predict_survival(passenger)

        result = (
            "Survived"
            if prediction == 1
            else "Did not survive"
        )

        return {
            "status": "success",
            "prediction": prediction,
            "result": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )