from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple predefined responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm doing great, thanks for asking!",
    "bye": "Goodbye! Take care.",
    "default": "I'm sorry, I didn't understand that."
}


@app.route('/chat', methods=['GET'])
def chat():
    # Get the user input from the URL
    user_input = request.args.get('message')
    user_input = user_input.lower().strip()

    # Respond based on predefined responses
    bot_response = responses.get(user_input, responses["default"])
    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
