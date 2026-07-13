import joblib

from src.preprocessing import clean_email

model = joblib.load("models/final_model.pkl")

tfidf = joblib.load("models/final_tfidf.pkl")


def predict_email(text):

    cleaned = clean_email(text)

    vector = tfidf.transform([cleaned])

    prediction = model.predict(vector)[0]

    decision_score = model.decision_function(vector)[0]

    return prediction, decision_score