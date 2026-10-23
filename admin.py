# admin.py
from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import json
import io
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

DATA_PATH = os.path.join('data', 'feedback.csv')
PRODUITS_PATH = os.path.join('data', 'produits.json')

# Charger les produits
with open(PRODUITS_PATH, 'r', encoding='utf-8') as f:
    produits = json.load(f)

# admin.py (partie admin)
@app.route('/', methods=['GET', 'POST'])
def admin():
    data = pd.read_csv(DATA_PATH) if os.path.exists(DATA_PATH) else pd.DataFrame(columns=['Produit', 'Commentaire', 'Sentiment', 'Date'])
    produit_selectionne = request.form.get('produit')
    if not produit_selectionne:
        produit_selectionne = produits[0]['nom'] if produits else None

    sentiment_filter = request.form.get('sentiment')
    if not sentiment_filter:
        sentiment_filter = 'Tous'

    periode = request.form.get('periode') or ''
    print(">>> Valeur brute reçue de 'periode':", repr(periode))

    start_date, end_date = None, None
    if 'au' in periode:
        dates = [d.strip() for d in periode.split('au')]
        if len(dates) == 2:
            try:
                start_date = pd.to_datetime(dates[0]).date()
                end_date = pd.to_datetime(dates[1]).date()
            except Exception:
                start_date, end_date = None, None
    
    print(">>> Dates interprétées -> Start:", start_date, ", End:", end_date)

    
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.date
    print(">>> Extrait des dates dans le DataFrame :")
    print(data[['Produit', 'Date']].head())            

    data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.date
    data['Sentiment'] = data['Sentiment'].astype(str)

    if produit_selectionne:
        data = data[data['Produit'] == produit_selectionne]

    if sentiment_filter != 'Tous':
        data = data[data['Sentiment'] == ('1' if sentiment_filter == 'Positif' else '0')]

    if start_date:
        data = data[data['Date'] >= start_date]
    if end_date:
        data = data[data['Date'] <= end_date]

    sentiment_counts = data['Sentiment'].value_counts().to_dict()
    count_pos = sentiment_counts.get('1', 0)
    count_neg = sentiment_counts.get('0', 0)

    chart_data = {
        'positif': count_pos,
        'negatif': count_neg
    }

    data = data.sort_values(by='Date', ascending=False)

    return render_template('admin.html',
                           produits=produits,
                           data=data,
                           produit_selectionne=produit_selectionne,
                           sentiment_filter=sentiment_filter,
                           periode=periode,
                           chart_data=chart_data)

@app.route('/export')
def export():
    data = pd.read_csv(DATA_PATH) if os.path.exists(DATA_PATH) else pd.DataFrame(columns=['Produit', 'Commentaire', 'Sentiment', 'Date'])
    output = io.StringIO()
    data.to_csv(output, index=False)
    output.seek(0)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    return send_file(io.BytesIO(output.getvalue().encode()),
                     mimetype='text/csv',
                     as_attachment=True,
                     download_name=f"feedback_export_{now}.csv")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
