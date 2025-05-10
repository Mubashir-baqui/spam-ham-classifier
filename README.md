# spam-ham-classifier
# SPAM/HAM Message Classification using NLP

This project demonstrates the use of **Natural Language Processing (NLP)** and **Machine Learning** for classifying SMS messages as **SPAM** or **HAM** (non-spam). The project uses a **Naive Bayes classifier** to predict whether a given SMS message is spam or not, based on a trained model and TF-IDF features.

---

## 📂 Project Structure

- `app.py` – The main Streamlit web application for SMS classification.
- `spam_classifier.pkl` – The trained Naive Bayes model for SPAM/HAM classification.
- `vectorizer.pkl` – The TF-IDF vectorizer used for text feature extraction.
- `README.md` – Project description and instructions.

---

## 🚀 Getting Started

To run the project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/spam-ham-classification.git
cd spam-ham-classification
Install Required Dependencies
Make sure you have Python 3 installed, then install the necessary libraries:
pip install -r requirements.txt
Run the Streamlit App
Run the following command to start the Streamlit app

You can find the dataset here:
https://archive.ics.uci.edu/ml/datasets/sms+spam+collection
