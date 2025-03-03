# scripts/train_model.py

import json
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
DATA_PATH = os.path.join(BASE_DIR, "../data/processed_data.json")
MODEL_PATH = os.path.join(BASE_DIR, "../models/tfidf_vectorizer.pkl")

# Load processed resume data
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract text for training
corpus = [item["text"] for item in data]

# Train TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(corpus)

# Save trained model
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)  # Ensure directory exists
joblib.dump(vectorizer, MODEL_PATH)

print(f"✅ TF-IDF Model Trained and Saved Successfully at {MODEL_PATH}!")
