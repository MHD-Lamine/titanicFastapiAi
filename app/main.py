from fastapi import FastAPI
from app.routes.prediction import router

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="Professional AI API with FastAPI",
    version="1.0.0"
)

app.include_router(router)