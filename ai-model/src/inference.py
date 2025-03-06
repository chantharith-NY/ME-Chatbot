import joblib
from preprocess import preprocess

# Load trained model and vectorizer
vectorizer = joblib.load("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/model/vectorizer.pkl")
model = joblib.load("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/model/model.pkl")
label_map = joblib.load("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/model/label_map.pkl")
responses = joblib.load("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/model/responses.pkl")

def get_response(user_input):
    processed_input = preprocess(user_input)
    input_vector = vectorizer.transform([processed_input])
    predicted_label = model.predict(input_vector)[0]
    return responses[predicted_label][0]  # Return the best response

# Simple chatbot interaction
# print("Chatbot is ready! Type 'exit' to quit.")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         break
#     response = get_response(user_input)
#     print(f"ME Chatbot: {response}")
