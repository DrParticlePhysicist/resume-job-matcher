# File: scripts/evaluate_model.py

import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load processed resume data
with open("../data/processed_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract text for evaluation
corpus = [item["text"] for item in data]
job_descriptions = [item["job_description"] for item in data]

# Load trained TF-IDF model
with open("../models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Transform data
X = vectorizer.transform(corpus)
Y = vectorizer.transform(job_descriptions)

# Compute cosine similarity
similarities = cosine_similarity(X, Y)

# Print average similarity score
avg_score = similarities.diagonal().mean()
print(f"✅ Model Evaluation Completed - Average Similarity Score: {avg_score:.2f}")
