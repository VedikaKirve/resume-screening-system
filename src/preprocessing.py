import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# download once
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)

    stop_words = set(stopwords.words('english'))
    words = text.split()

    # ✅ NEW: Lemmatization added
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]

    return " ".join(words)