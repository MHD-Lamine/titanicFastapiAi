# Titanic Survival Prediction API

Professional AI API built with FastAPI and Machine Learning.

## Features

- FastAPI REST API
- Machine Learning prediction
- Swagger documentation
- Docker support
- Clean architecture

## Technologies

- FastAPI
- Scikit-learn
- Pandas
- Docker
- Python

## Installation

```bash
git clone YOUR_GITHUB_URL
cd titanic-fastapi-ai

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

```

## Installation

```bash
docker build -t titanic-api .
docker run -p 8000:8000 titanic-api

```
## API Documentation

```bash
http://127.0.0.1:8000/docs

```

## Example Request

```bash

{
  "Pclass": 1,
  "Sex": 1,
  "Age": 25,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 100
}
```



