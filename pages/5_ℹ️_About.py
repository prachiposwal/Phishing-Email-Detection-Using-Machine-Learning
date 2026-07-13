import streamlit as st
from src.utils import load_css

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

st.title("ℹ️ About This Project")

st.markdown("""
## AI Powered Phishing Email Detection

This project is a Machine Learning based web application that detects phishing emails using Natural Language Processing (NLP).

The objective is to improve email security by automatically classifying emails into:

- ✅ Legitimate
- 🚨 Phishing
""")

st.divider()

# ===================================
# Features
# ===================================

st.header("🚀 Features")

st.success("""
- AI Email Detection
- NLP Preprocessing
- TF-IDF Feature Extraction
- Suspicious Keyword Detection
- Performance Dashboard
- Dataset Insights
- Risk Assessment
""")

st.divider()

# ===================================
# Machine Learning
# ===================================

st.header("🤖 Machine Learning Models")

st.markdown("""
The following models were trained and compared:

- Linear SVM
- Logistic Regression
- Naive Bayes
- Random Forest
- Simple Neural Network
""")

st.info("""
Final Selected Model:

✅ Linear SVM

Reason:

- High Accuracy
- Fast Prediction
- Low Memory Usage
- Excellent Generalization
""")

st.divider()

# ===================================
# Technologies
# ===================================

st.header("⚙️ Technologies")

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
### Programming

- Python
- Streamlit
""")

with col2:

    st.markdown("""
### ML

- Scikit-Learn
- TensorFlow
- Joblib
""")

with col3:

    st.markdown("""
### NLP

- NLTK
- TF-IDF
- Pandas
- NumPy
""")

st.divider()

# ===================================
# Future Work
# ===================================

st.header("🚀 Future Improvements")

st.markdown("""
- Real-time Email API

- Browser Extension

- Gmail Integration

- Explainable AI

- Deep Learning Models

- Cloud Deployment

- Multi-language Support
""")

st.divider()

# ===================================
# Developer
# ===================================

st.header("👨‍💻 Developer")

st.success("""
Developed as an AI & Machine Learning project for phishing email detection using Natural Language Processing and Streamlit.
""")

st.divider()

st.caption("© 2026 AI Powered Phishing Email Detection System")