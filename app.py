import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("spam_classifier.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# --- Custom HTML/CSS ---
st.set_page_config(page_title="SPAM/HAM Classifier", layout="centered")

st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-box {
        font-size: 22px;
        padding: 10px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("Use this app to detect if a message is **SPAM** or **HAM**.")

# --- Main Title ---
st.markdown('<p class="main-title">📩 SPAM / HAM Classifier</p>', unsafe_allow_html=True)

# --- Input Section ---
st.subheader("Enter an SMS message:")
user_input = st.text_area("Write your message here", height=100)

# --- Prediction ---
if st.button("🔍 Classify Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message before classifying.")
    else:
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)[0]

        if prediction.lower() == "spam":
            st.markdown('<div class="result-box">🚫 <b>Result:</b> This message is <span style="color:red;"><b>SPAM</b></span>.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box">✅ <b>Result:</b> This message is <span style="color:green;"><b>HAM</b></span>.</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<center><small>Made with ❤️ using Streamlit</small></center>", unsafe_allow_html=True)
