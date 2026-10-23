# Binary Sentiment Classification — Licence PFE 2024–2025

## Project Overview

This project was developed as part of my Bachelor's degree final-year project (PFE) for the 2024–2025 academic year.

The main objective is to build a sentiment analysis application that performs **binary sentiment classification**, identifying whether a text expresses a positive or negative sentiment.

The application uses Natural Language Processing (NLP) techniques and a machine learning model to analyze text and predict its sentiment. It also provides a web interface where users can interact with the system and explore product reviews.

## Objectives

- Develop a binary sentiment classification system.
- Preprocess textual data using NLP techniques.
- Transform text into numerical features using TF-IDF.
- Train and use a machine learning model for sentiment prediction.
- Build a web application for analyzing user reviews.
- Display product information and collect user feedback.

## Technologies Used

- **Python** — Core programming language.
- **Scikit-learn** — Machine learning and model training.
- **TF-IDF** — Text feature extraction.
- **Natural Language Processing (NLP)** — Text preprocessing and analysis.
- **Flask** — Web application framework, if used in the implementation.
- **HTML / CSS** — Web interface and styling.
- **Pickle** — Saving and loading trained model artifacts.

## Project Structure

```text
SentimentAnalysisPFE/
├── data/
│   ├── feedback.csv
│   └── produits.json
├── models/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
├── src/
│   ├── __init__.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── train.py
│   └── utils.py
├── static/
│   ├── images/
│   ├── admin.css
│   └── styles.css
├── templates/
│   ├── admin.html
│   ├── avis.html
│   └── produits.html
├── admin.py
├── app.py
└── README.md
```

## How It Works

1. **Text Input:** The user submits a text or product review.
2. **Text Preprocessing:** The text is cleaned and prepared for analysis.
3. **Feature Extraction:** TF-IDF converts the text into numerical features.
4. **Sentiment Prediction:** The trained machine learning model predicts one of two classes: positive or negative.
5. **Result Display:** The application displays the predicted sentiment through its web interface.

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/salmaboutahir/PFE-Licence-2024-2025.git
cd PFE-Licence-2024-2025
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by the source code and create a `requirements.txt` file for reproducibility.

### 4. Run the Application

If the application uses Flask:

```bash
python app.py
```

Then open the local URL displayed in the terminal, commonly `http://127.0.0.1:5000`.

## Machine Learning Pipeline

The classification pipeline consists of text preprocessing, TF-IDF feature extraction, and a trained classification model. The model and vectorizer are saved in the `models/` directory and loaded by the application to make predictions.

## Academic Context

**Project:** Final-Year Bachelor's Degree Project (PFE)  
**Academic Year:** 2024–2025  
**Field:** Data Science / Artificial Intelligence  
**Topic:** Binary Sentiment Classification using Natural Language Processing and Machine Learning

## Author

**Salma Boutahir**

GitHub: [@salmaboutahir](https://github.com/salmaboutahir)
