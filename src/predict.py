import joblib
import re
from langdetect import detect, LangDetectException
from src.preprocess import clean_text

def predict_sentiment(review):
    # Vérifie si le texte est vide
    if not review.strip():
        return "Veuillez entrer un avis non vide."

    # Nettoyage léger pour la détection de langue
    clean_for_lang = re.sub(r"[^\w\s]", "", review.lower()).strip()

    # Détection de langue si le texte est assez long
    if len(clean_for_lang.split()) >= 3:
        try:
            lang = detect(clean_for_lang)
            if lang != 'en':
                print("⚠️ Avertissement : le commentaire semble être en", lang.upper(), "et non en anglais.")
        except LangDetectException:
            print("⚠️ Langue non détectée. La prédiction sera tout de même effectuée.")
    else:
        print("ℹ️ Texte trop court pour détecter la langue. La prédiction sera tout de même effectuée.")

    # Charger le modèle et le vecteuriseur
    model = joblib.load("models/sentiment_model.pkl")
    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

    # Nettoyer le texte et faire la prédiction
    cleaned = clean_text(review)
    vect = vectorizer.transform([cleaned])
    pred = model.predict(vect)[0]

    # Retourner le sentiment
    return "Positive 😊" if pred == 1 else "Negative 😞"

if __name__ == "__main__":
    print("Tape 'exit' pour quitter.\n")

    while True:
        review = input("Ton avis : ")

        if review.lower() == "exit":
            print("À bientôt ! 👋")
            break

        sentiment = predict_sentiment(review)
        print("Sentiment prédit :", sentiment)
        print("-" * 40)
