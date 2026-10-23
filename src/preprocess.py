import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

# Télécharger uniquement les stopwords et WordNet, une seule fois.
nltk.download('stopwords')
nltk.download('wordnet')

# Initialisation des ressources
stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\b[a-zA-Z]{2,}\b')  # Mots de 2 lettres ou plus
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Nettoie un texte :
    - Mise en minuscules
    - Tokenisation (sans punkt)
    - Suppression des stopwords
    - Lemmatisation
    - Suppression des caractères inutiles (URLs, mentions Twitter, etc.)
    """
    # Mise en minuscules
    text = text.lower()

    # Suppression des URLs, mentions Twitter et autres caractères non pertinents
    text = re.sub(r'http\S+|www\S+', '', text)  # Suppression des URLs
    text = re.sub(r'@\w+', '', text)  # Suppression des mentions Twitter
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Suppression des caractères non alphabétiques (conservant les lettres et les espaces)

    # Tokenisation
    tokens = tokenizer.tokenize(text)

    # Suppression des stopwords et lemmatisation
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    # Retourner le texte nettoyé
    return ' '.join(tokens)

def clean_dataframe(df):
    """
    Applique le nettoyage à tout le DataFrame.
    """
    # Applique la fonction de nettoyage à chaque texte de la colonne 'text'
    df['clean_text'] = df['text'].apply(clean_text)
    return df
