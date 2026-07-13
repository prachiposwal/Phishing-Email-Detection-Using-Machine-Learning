import streamlit as st
from src.utils import load_css

st.set_page_config(
    page_title="AI Powered Phishing Email Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
st.markdown(load_css(), unsafe_allow_html=True)

st.title("🛡️ AI Powered Phishing Email Detection System")

st.markdown("""
## Enterprise Email Security using Machine Learning & NLP

Welcome to the **AI Powered Phishing Email Detection System**.

This application leverages **Natural Language Processing (NLP)** and **Machine Learning**
to classify emails as **Legitimate** or **Phishing** with high accuracy.

---

### 🚀 Features

- 📧 AI Email Detector
- 📊 Model Performance Dashboard
- 📈 Project Insights
- 🤖 Optimized Linear SVM Classifier
- 🧠 NLP Preprocessing Pipeline
- 🔍 Suspicious Keyword Detection
- ⚠️ Email Risk Analysis

---

### 📌 Navigation

Use the sidebar to explore the application.

- 🏠 Home
- 📧 Email Detector
- 📊 Performance
- 📈 Project Insights
- ℹ️ About
""")

st.info("👈 Select a page from the sidebar to begin.")

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Dataset", "82,486 Emails")

with c2:
    st.metric("Best Model", "Linear SVM")

with c3:
    st.metric("Accuracy", "98.64%")

st.markdown("---")

st.success("✅ Project Status : Production Ready")