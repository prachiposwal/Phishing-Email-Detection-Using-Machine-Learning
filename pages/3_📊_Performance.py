import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.utils import load_css

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="Performance",
    page_icon="📊",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ==========================================
# Header
# ==========================================

st.title("📊 Model Performance Dashboard")

st.markdown("""
Compare the performance of different Machine Learning models used in this project.
""")

st.divider()

# ==========================================
# Model Results
# ==========================================

results = pd.DataFrame({

    "Model":[
        "Simple Neural Network",
        "Linear SVM",
        "Logistic Regression",
        "Naive Bayes",
        "Random Forest"
    ],

    "Accuracy":[
        98.70,
        98.64,
        98.18,
        95.40,
        94.33
    ],

    "Precision":[
        98.56,
        98.44,
        97.94,
        98.56,
        91.88
    ],

    "Recall":[
        98.96,
        98.95,
        98.60,
        92.54,
        97.77
    ],

    "F1 Score":[
        98.76,
        98.70,
        98.27,
        95.46,
        94.74
    ],

    "Training Time (s)":[
        179.77,
        2.46,
        0.78,
        0.04,
        6.95
    ]

})

st.subheader("📋 Model Comparison")

st.dataframe(
    results,
    use_container_width=True
)

st.divider()

# ==========================================
# Best Model
# ==========================================

st.subheader("🏆 Best Performing Model")

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Best Model","Simple Neural Network")

with col2:
    st.metric("Accuracy","98.70%")

with col3:
    st.metric("Runner Up","Linear SVM")

st.divider()

# ==========================================
# Accuracy Chart
# ==========================================

st.subheader("📈 Accuracy Comparison")

fig,ax=plt.subplots(figsize=(9,5))

ax.bar(
    results["Model"],
    results["Accuracy"]
)

ax.set_ylabel("Accuracy (%)")

ax.set_ylim(90,100)

plt.xticks(rotation=20)

st.pyplot(fig)

st.divider()

# ==========================================
# Training Time
# ==========================================

st.subheader("⏱ Training Time Comparison")

fig2,ax2=plt.subplots(figsize=(9,5))

ax2.bar(
    results["Model"],
    results["Training Time (s)"]
)

ax2.set_ylabel("Seconds")

plt.xticks(rotation=20)

st.pyplot(fig2)

st.divider()

# ==========================================
# Confusion Matrix
# ==========================================

st.subheader("📌 Confusion Matrix")

st.image(
    "assets/confusion_matrix.png",
    caption="Final Linear SVM Confusion Matrix",
    use_container_width=True
)

st.divider()

# ==========================================
# Model Summary
# ==========================================

st.subheader("📖 Summary")

st.success("""
### Final Selected Model

**Linear SVM**

Reason for Selection:

- Excellent Accuracy
- Very Fast Training
- Excellent Generalization
- Low Memory Usage
- Perfect for TF-IDF Features

Although the Neural Network achieved slightly higher accuracy,
the Linear SVM was selected because it is significantly faster,
lighter, and better suited for deployment.
""")

st.divider()

# ==========================================
# Performance Insights
# ==========================================

st.subheader("💡 Key Insights")

st.info("""
✅ Linear SVM provides an excellent balance between accuracy and speed.

✅ Naive Bayes trains almost instantly but sacrifices some accuracy.

✅ Random Forest performs well but requires more memory.

✅ Neural Network achieved the highest accuracy but requires much longer training.

✅ Linear SVM is the best deployment choice for this application.
""")

st.divider()

st.success("✅ Performance Dashboard Loaded Successfully.")