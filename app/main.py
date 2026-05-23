from fastapi import FastAPI
from app.routes.prediction import router

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="""
Professional AI API built with FastAPI.

Features:
- Machine Learning Prediction
- REST API
- Swagger Documentation
- Clean Architecture
""",
    version="1.0.0",
    contact={
        "name": "Mohamed Lamine Diabate",
        "email": "mohaldiabate@gmail.com"
    }
)

app.include_router(router)