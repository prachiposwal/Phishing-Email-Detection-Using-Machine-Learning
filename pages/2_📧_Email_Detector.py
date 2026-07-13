import streamlit as st
from src.predictor import predict_email
from src.utils import (
    load_css,
    prediction_label,
    risk_level,
    find_suspicious_keywords,
)

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
    page_title="Email Detector",
    page_icon="📧",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ==================================================
# Header
# ==================================================

st.title("📧 AI Email Detector")

st.markdown("""
Paste an email below and let the AI determine whether it is **Legitimate** or **Phishing**.
""")

st.divider()

# ==================================================
# Sample Emails
# ==================================================

legitimate_email = """Hello John,

Your interview has been confirmed for Monday at 10:00 AM.

Please bring a copy of your resume.

Best Regards,
HR Team
"""

phishing_email = """URGENT!

Your account has been suspended.

Verify your identity immediately.

Click here:

http://secure-bank-login-update.com

Failure to verify within 24 hours will permanently suspend your account.
"""

col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Load Legitimate Email"):
        st.session_state["email"] = legitimate_email

with col2:
    if st.button("🚨 Load Phishing Email"):
        st.session_state["email"] = phishing_email

email = st.text_area(
    "Paste Email Here",
    key="email",
    height=300
)

st.divider()

# ==================================================
# Analyze Button
# ==================================================

if st.button("🔍 Analyze Email", type="primary"):

    if email.strip() == "":

        st.warning("Please paste an email first.")

    else:

        prediction, score = predict_email(email)

        confidence = min(abs(float(score)) * 25, 100)

        # ==========================================
        # Metrics
        # ==========================================

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "Prediction",
                prediction_label(prediction)
            )

        with m2:
            st.metric(
                "Decision Score",
                f"{score:.3f}"
            )

        with m3:
            st.metric(
                "Confidence",
                f"{confidence:.1f}%"
            )

        st.divider()

        # ==========================================
        # Confidence Meter
        # ==========================================

        st.subheader("📊 Prediction Confidence")

        st.progress(confidence / 100)

        st.caption(f"Confidence : {confidence:.1f}%")

        st.divider()

        # ==========================================
        # Prediction Result
        # ==========================================

        if prediction == 1:

            st.error("""
## 🚨 PHISHING EMAIL DETECTED

This email contains characteristics commonly found in phishing attacks.

### Recommendations

• Do NOT click unknown links

• Do NOT download attachments

• Never share OTPs or Passwords

• Verify the sender independently
""")

        else:

            st.success("""
## ✅ LEGITIMATE EMAIL

The email appears to be safe.

### Recommendations

• Verify unknown senders

• Stay cautious with links

• Scan attachments before opening
""")

        st.divider()

        # ==========================================
        # AI Summary
        # ==========================================

        st.subheader("🧠 AI Analysis")

        if prediction == 1:

            st.write("""
The model detected several phishing characteristics including:

- Urgent language
- Account verification request
- Suspicious wording
- Possible malicious links
- Request for sensitive information
""")

        else:

            st.write("""
The email appears to follow normal communication patterns.

No major phishing indicators were detected.
""")

        st.divider()

        # ==========================================
        # Suspicious Keywords
        # ==========================================

        st.subheader("🔎 Suspicious Keywords")

        keywords = find_suspicious_keywords(email)

        if len(keywords) == 0:

            st.success("No suspicious keywords detected.")

        else:

            cols = st.columns(min(4, len(keywords)))

            for i, word in enumerate(keywords):

                cols[i % len(cols)].error(word.upper())

        st.divider()

        # ==========================================
        # Risk Level
        # ==========================================

        st.subheader("⚠️ Risk Assessment")

        risk = risk_level(score)

        if risk == "High":
            st.error(f"Risk Level : {risk}")

        elif risk == "Medium":
            st.warning(f"Risk Level : {risk}")

        else:
            st.success(f"Risk Level : {risk}")

        st.divider()

        # ==========================================
        # Safety Checklist
        # ==========================================

        st.subheader("🛡️ Email Safety Checklist")

        st.checkbox("Verify sender email address")

        st.checkbox("Inspect hyperlinks before clicking")

        st.checkbox("Avoid downloading unknown attachments")

        st.checkbox("Never share passwords or OTPs")

        st.checkbox("Verify urgent requests independently")

        st.divider()

        # ==========================================
        # Footer
        # ==========================================

        st.info(
            "Prediction is generated using an Optimized Linear SVM model trained on the phishing email dataset."
        )