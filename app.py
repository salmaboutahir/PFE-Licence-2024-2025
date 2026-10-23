# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import json
import os
from datetime import datetime
import joblib

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Chemins des fichiers
DATA_PATH = os.path.join('data', 'feedback.csv')
PRODUITS_PATH = os.path.join('data', 'produits.json')
MODEL_PATH = os.path.join('models', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join('models', 'tfidf_vectorizer.pkl')

# Charger la liste des produits
with open(PRODUITS_PATH, 'r', encoding='utf-8') as f:
    produits = json.load(f)

# Charger le modèle et le vectorizer
sentiment_model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route('/')
def accueil():
    return render_template('produits.html', produits=produits)

@app.route('/avis/<produit_nom>', methods=['GET', 'POST'])
def avis(produit_nom):
    produit = next((p for p in produits if p["nom"] == produit_nom), None)
    if not produit:
        flash("Produit non trouvé.", "error")
        return redirect(url_for('accueil'))
    
    if request.method == 'POST':
        commentaire = request.form.get('commentaire', '').strip()
        if not commentaire:
            flash("Le champ commentaire est obligatoire.", "error")
            return redirect(url_for('avis', produit_nom=produit_nom))
        
        # Prédire le sentiment
        commentaire_vect = vectorizer.transform([commentaire])
        prediction = sentiment_model.predict(commentaire_vect)[0]
        sentiment = '1' if prediction == 1 else '0'

        # Sauvegarder dans feedback.csv
        now = datetime.now().strftime("%Y-%m-%d")
        feedback = pd.DataFrame(
            [[produit_nom, commentaire, sentiment, now]],
            columns=['Produit', 'Commentaire', 'Sentiment', 'Date']
        )
        feedback.to_csv(DATA_PATH, mode='a', header=not os.path.exists(DATA_PATH), index=False)
        
        #flash(f"Merci pour votre avis ! Sentiment détecté : {sentiment}", "success")
        return redirect(url_for('avis', produit_nom=produit_nom))
    
    return render_template('avis.html', produit=produit)

if __name__ == '__main__':
    app.run(debug=True)
