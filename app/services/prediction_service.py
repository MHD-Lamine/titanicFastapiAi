import joblib
import numpy as np

# Charger modèle
model = joblib.load("model/titanic_model.pkl")

# Charger imputer
imputer = joblib.load("model/imputer.pkl")

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