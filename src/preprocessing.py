import re
import string

import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download only if needed
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")
    nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))


def clean_email(text):

    text = str(text)

    text = text.lower()

    text = re.sub(r"http\\S+|www\\S+", " ", text)

    text = re.sub(r"\\S+@\\S+", " ", text)

    text = re.sub(r"\\d+", " ", text)

    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    words = []

    for word in text.split():

        if word not in stop_words:

            word = lemmatizer.lemmatize(word)

            words.append(word)

    return " ".join(words)