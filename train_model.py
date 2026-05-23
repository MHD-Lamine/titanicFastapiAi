import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import joblib

# Charger dataset
df = pd.read_csv("datasets/train.csv")

# Colonnes utiles
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]

# Convertir sexe
df["Sex"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

# Variables
X = df[features]
y = df["Survived"]

# Gestion valeurs manquantes
imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Modèle
model = RandomForestClassifier()

# Entraînement
model.fit(X_train, y_train)

# Prédictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy : {accuracy}")

# Sauvegarde modèle
joblib.dump(model, "model/titanic_model.pkl")

# Sauvegarde imputer
joblib.dump(imputer, "model/imputer.pkl")

print("Modèle sauvegardé avec succès")