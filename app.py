from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML page

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']  # Get message from HTML form
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})  # Send back bot response

def get_bot_response(user_message):
    # Simple predefined responses for demo purposes
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm doing great, thanks for asking!",
        "bye": "Goodbye! Take care.",
        "default": "Sorry, I don't understand that."
    }
    
    # Get the response from the dictionary, or use the default response
    return responses.get(user_message.lower(), responses["default"])

if __name__ == '__main__':
    app.run(debug=True)
