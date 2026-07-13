def prediction_label(prediction):
    if prediction == 1:
        return "🚨 Phishing"
    return "✅ Legitimate"


def risk_level(score):
    score = abs(float(score))

    if score > 2:
        return "High"
    elif score > 1:
        return "Medium"
    else:
        return "Low"


def load_css():
    with open("assets/style.css", "r") as f:
        return f"<style>{f.read()}</style>"


def find_suspicious_keywords(text):

    keywords = [
        "verify",
        "account",
        "login",
        "password",
        "bank",
        "urgent",
        "click",
        "limited",
        "confirm",
        "security",
        "update",
        "payment",
        "invoice",
        "winner",
        "gift",
        "free",
        "bitcoin",
        "crypto",
        "otp",
        "reset"
    ]

    text = str(text).lower()

    found = []

    for word in keywords:
        if word in text:
            found.append(word)

    return found