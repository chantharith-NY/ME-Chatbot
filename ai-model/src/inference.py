# inference.py

import ollama

def query_model(query):
    """
    Send a query to the trained model and get a response
    """
    response = ollama.chat(model="custom_itc_bot", messages=[
        {"role": "user", "content": query}
    ])
    return response["message"]["content"]

if __name__ == "__main__":
    query = input("Ask the ITC chatbot: ")
    answer = query_model(query)
    print("Answer:", answer)
