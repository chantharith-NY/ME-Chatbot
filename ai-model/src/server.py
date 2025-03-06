from flask import Flask, request, jsonify
from inference import get_response  # Import function from inference.py

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    chatbot_response = get_response(user_message)  # Call inference.py
    return jsonify({"response": chatbot_response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
