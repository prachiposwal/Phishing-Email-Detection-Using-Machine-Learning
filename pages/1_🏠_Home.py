import streamlit as st
from src.utils import load_css

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# Load CSS
# ==========================================

st.markdown(load_css(), unsafe_allow_html=True)

# ==========================================
# Hero Section
# ==========================================

st.title("🛡️ AI Powered Phishing Email Detection System")

st.markdown("""
### Enterprise Email Security using Artificial Intelligence

Detect phishing emails using **Natural Language Processing (NLP)** and **Machine Learning**.

This application classifies emails as:

- ✅ Legitimate Email
- 🚨 Phishing Email

using an optimized **Linear SVM** model.
""")

st.divider()

# ==========================================
# Dashboard Metrics
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📧 Total Emails", "82,486")

with col2:
    st.metric("🤖 Best Model", "Linear SVM")

with col3:
    st.metric("🎯 Accuracy", "98.64%")

with col4:
    st.metric("⚡ Status", "Ready")

st.divider()

# ==========================================
# Features
# ==========================================

st.header("🚀 Application Features")

left, right = st.columns(2)

with left:

    st.success("""
### 📧 Smart Email Detection

Predict whether an email is **Legitimate** or **Phishing** using AI.
""")

    st.success("""
### 🧠 NLP Processing

- Text Cleaning
- Stopword Removal
- Lemmatization
- TF-IDF Vectorization
""")

    st.success("""
### 🔍 Suspicious Keyword Detection

Detect phishing-related words inside emails.
""")

with right:

    st.info("""
### 📊 Performance Dashboard

View:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
""")

    st.info("""
### 📈 Project Insights

Explore:

- Dataset Statistics
- NLP Pipeline
- Machine Learning Workflow
""")

    st.info("""
### ⚠ Risk Analysis

Displays confidence score and estimated phishing risk.
""")

st.divider()

# ==========================================
# Workflow
# ==========================================

st.header("🧠 Machine Learning Workflow")

st.code("""
Email

↓

Text Cleaning

↓

Lowercase Conversion

↓

Remove URLs

↓

Remove Email Addresses

↓

Remove Numbers

↓

Remove Punctuation

↓

Stopword Removal

↓

Lemmatization

↓

TF-IDF Vectorization

↓

Optimized Linear SVM

↓

Prediction
""")

st.divider()

# ==========================================
# Technologies
# ==========================================

st.header("⚙ Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.markdown("""
### 💻 Programming

- Python
- Streamlit
""")

with tech2:
    st.markdown("""
### 🤖 Machine Learning

- Scikit-Learn
- Linear SVM
- Logistic Regression
- Naive Bayes
- Neural Network
""")

with tech3:
    st.markdown("""
### 📚 NLP & Data

- NLTK
- TF-IDF
- Pandas
- NumPy
- Matplotlib
""")

st.divider()

# ==========================================
# Navigation
# ==========================================

st.header("📌 Explore the Project")

st.info("""
Use the sidebar to navigate through the application.

🏠 Home

📧 Email Detector

📊 Performance

📈 Project Insights

ℹ About
""")

st.divider()

# ==========================================
# Footer
# ==========================================

st.success("✅ AI Powered Phishing Email Detection System is running successfully.")

st.caption(
    "Developed using Python, Streamlit, Machine Learning and Natural Language Processing."
)