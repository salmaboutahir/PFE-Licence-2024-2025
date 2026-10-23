import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

from src.utils import load_data
from src.preprocess import clean_dataframe

# 1. Charger les données
file_path = "data/raw/train.ft.txt"
df = load_data(file_path)

# 2. Nettoyage
df = clean_dataframe(df)

# 3. Séparer les données
X_train, X_test, y_train, y_test = train_test_split(
    df["clean_text"], df["label"], test_size=0.2, random_state=42)

# 4. Vectorisation
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# 5. Entraînement du modèle
model = LogisticRegression()
model.fit(X_train_vect, y_train)

# 6. Évaluation
y_pred = model.predict(X_test_vect)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 7. Sauvegarde
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/sentiment_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
