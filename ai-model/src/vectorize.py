from sklearn.feature_extraction.text import TfidfVectorizer
import json
from preprocess import preprocess

# Load intents data
with open("ai-model/data/intents.json", "r") as file:
    intents = json.load(file)

# Extract training data
patterns = [preprocess(q) for intent in intents["intents"] for q in intent["patterns"]]

# Initialize and fit TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Save vectorizer for later use
import joblib
joblib.dump(vectorizer, "ai-model/model/vectorizer.pkl")
