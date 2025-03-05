import json
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import joblib
from vectorize import X
from preprocess import preprocess

# Load intents data
with open("ai-model/data/intents.json", "r") as file:
    intents = json.load(file)

# Prepare labels
y = []
responses = []
label_map = {}

for idx, intent in enumerate(intents["intents"]):
    for _ in intent["patterns"]:
        y.append(idx)
    responses.append(intent["responses"])
    label_map[idx] = intent["tag"]

# Train a classifier
model = MultinomialNB()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "ai-model/model/model.pkl")
joblib.dump(label_map, "ai-model/model/label_map.pkl")
joblib.dump(responses, "ai-model/model/responses.pkl")

print("Model training complete!")
