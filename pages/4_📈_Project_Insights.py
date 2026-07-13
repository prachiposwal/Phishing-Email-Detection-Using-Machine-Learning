import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.utils import load_css

st.set_page_config(
    page_title="Project Insights",
    page_icon="📈",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

st.title("📈 Project Insights")

st.markdown("""
Understand the dataset, preprocessing pipeline and machine learning workflow used in this project.
""")

st.divider()

# =========================
# Dataset Overview
# =========================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("📧 Total Emails","82,486")

with c2:
    st.metric("🚨 Phishing","42,891")

with c3:
    st.metric("✅ Legitimate","39,595")

with c4:
    st.metric("⚖️ Balance","52 : 48")

st.divider()

# =========================
# Dataset Distribution
# =========================

st.subheader("📊 Dataset Distribution")

labels=["Phishing","Legitimate"]
sizes=[42891,39595]

fig,ax=plt.subplots(figsize=(6,6))

ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

st.pyplot(fig)

st.divider()

# =========================
# NLP Pipeline
# =========================

st.subheader("🧠 NLP Pipeline")

st.code("""
Raw Email

↓

Lowercase

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

Linear SVM Prediction
""")

st.divider()

# =========================
# Workflow
# =========================

st.subheader("⚙️ Project Workflow")

workflow = pd.DataFrame({

"Step":[
"Collect Dataset",
"Clean Data",
"Text Preprocessing",
"TF-IDF",
"Train/Test Split",
"Model Comparison",
"Hyperparameter Tuning",
"Final Model",
"Deployment"
]

})

st.dataframe(
workflow,
use_container_width=True
)

st.divider()

# =========================
# Technologies
# =========================

st.subheader("💻 Technologies Used")

t1,t2,t3 = st.columns(3)

with t1:

    st.markdown("""
### Programming

- Python
- Streamlit
- Joblib
""")

with t2:

    st.markdown("""
### Machine Learning

- Scikit-Learn
- Linear SVM
- Logistic Regression
- Random Forest
- Neural Network
""")

with t3:

    st.markdown("""
### NLP

- NLTK
- TF-IDF
- Lemmatization
- Stopword Removal
""")

st.divider()

st.success("✅ Project Insights Loaded Successfully.")