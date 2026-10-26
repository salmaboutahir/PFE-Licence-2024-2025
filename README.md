# Binary Sentiment Classification — Licence PFE 2024–2025

## Project Overview

This project was developed as part of my Bachelor's degree final-year project (PFE) for the 2024–2025 academic year.

The main objective is to develop a sentiment analysis application that performs **binary sentiment classification**, identifying whether a text expresses a positive or negative sentiment.

The application combines Natural Language Processing (NLP), TF-IDF feature extraction, and a machine learning classifier to analyze customer reviews and predict their sentiment. A web interface allows users to interact with the system and explore product reviews.

## Objectives

- Develop a binary sentiment classification system.
- Preprocess textual data using NLP techniques.
- Convert text into numerical features using TF-IDF.
- Train and evaluate a machine learning classification model.
- Build a web application for analyzing customer reviews.
- Display product information and collect user feedback.

## Technologies Used

- **Python** — Core programming language.
- **Scikit-learn** — Machine learning and model evaluation.
- **TF-IDF** — Text feature extraction.
- **Natural Language Processing (NLP)** — Text preprocessing and analysis.
- **NLTK** — Text processing and linguistic resources.
- **Flask** — Web application framework.
- **HTML / CSS** — Web interface and styling.
- **Joblib / Pickle** — Saving and loading trained model artifacts.
- **Pandas / NumPy** — Data manipulation and processing.

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
├── requirements.txt
└── README.md
```

## How It Works

The application follows these steps:

1. **Text Input:** The user submits a product review.
2. **Text Preprocessing:** The text is cleaned and prepared for analysis.
3. **Feature Extraction:** TF-IDF transforms the text into numerical features.
4. **Sentiment Prediction:** The trained classifier predicts one of two classes: positive or negative.
5. **Result Display:** The predicted sentiment is displayed through the web interface.
6. **Feedback Management:** Customer reviews can be collected and stored for further analysis.

## Machine Learning Pipeline

The classification pipeline consists of the following stages:

- **Preprocessing:** Cleaning and preparing textual data.
- **Feature Extraction:** Transforming text into numerical representations using TF-IDF.
- **Model Training:** Training a machine learning classifier on labeled reviews.
- **Model Evaluation:** Measuring classification performance on a test dataset.
- **Model Persistence:** Saving the trained classifier and TF-IDF vectorizer in the `models/` directory.
- **Prediction:** Loading the saved artifacts to classify new reviews.

## Results and Model Evaluation

The model was evaluated on a test dataset containing **80,000 reviews**.

### Performance Metrics

| Evaluation Metric | Score |
|---|---:|
| Accuracy | **88.56%** |
| Macro Precision | 88.5%* |
| Macro Recall | 88.5%* |
| Macro F1-score | 88.5%* |
| Weighted F1-score | 88.5%* |

*The precision, recall, and F1-score averages above are approximate values based on the classification report rounded to two decimal places.*

### Classification Report

| Sentiment Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Class 0 | 0.89 | 0.88 | 0.88 | 39,896 |
| Class 1 | 0.88 | 0.89 | 0.89 | 40,104 |
| Macro Average | 0.89 | 0.89 | 0.89 | 80,000 |
| Weighted Average | 0.89 | 0.89 | 0.89 | 80,000 |

### Results Analysis

The model achieved an accuracy of **88.56%**, demonstrating its ability to classify customer reviews into two sentiment categories.

The classification report shows similar performance across both classes:

- **Class 0:** Precision of 0.89 and recall of 0.88.
- **Class 1:** Precision of 0.88 and recall of 0.89.

The test dataset contains 39,896 samples from Class 0 and 40,104 samples from Class 1, representing a nearly balanced distribution.

These results indicate that the TF-IDF-based classification pipeline can identify positive and negative sentiments with consistent performance across both classes.

**Note:** Class 0 and Class 1 should be mapped to negative and positive sentiment according to the label encoding used during training.

## Installation and Execution

### Prerequisites

- Python 3.10 or later.
- pip.
- Git.

### 1. Clone the Repository

```bash
git clone https://github.com/salmaboutahir/PFE-Licence-2024-2025.git
cd PFE-Licence-2024-2025
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by the project source code.

### 4. Run the Application

Start the Flask application:

```bash
python app.py
```

Then open the local address displayed in the terminal, commonly:

http://127.0.0.1:5000

### 5. Train the Model (Optional)

Pre-trained model files are expected in the `models/` directory. To train the model again, ensure that the required training dataset is available, then run the following command from the project root:

```bash
python -m src.train
```

The training process evaluates the classifier and displays metrics such as accuracy, precision, recall, and F1-score.

**Important:** The training dataset may be large and may not be included in the repository. Place it in the expected location before retraining the model.

## Academic Context

- **Project:** Final-Year Bachelor's Degree Project (PFE)
- **Academic Year:** 2024–2025
- **Field:** Data Science / Artificial Intelligence
- **Topic:** Binary Sentiment Classification using Natural Language Processing and Machine Learning

## Author

**Salma Boutahir**

- GitHub: [@salmaboutahir](https://github.com/salmaboutahir)
- Repository: [PFE-Licence-2024-2025](https://github.com/salmaboutahir/PFE-Licence-2024-2025)

---

If you find this project interesting, feel free to explore the repository and its implementation.
