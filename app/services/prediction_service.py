from pathlib import Path
import joblib
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model_path = BASE_DIR / "model" / "titanic_model.pkl"

imputer_path = BASE_DIR / "model" / "imputer.pkl"

# Charger modèle
model = joblib.load(model_path)

# Charger imputer
imputer = joblib.load(imputer_path)

def predict_survival(data):

    try:

        input_data = np.array([[
            data.Pclass,
            data.Sex,
            data.Age,
            data.SibSp,
            data.Parch,
            data.Fare
        ]])

        # Transformation
        input_data = imputer.transform(input_data)

        # Prediction
        prediction = model.predict(input_data)

        return int(prediction[0])

    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")