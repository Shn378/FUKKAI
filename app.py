from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to FUKKAI — The AI That Tells You To Fuck Off."

@app.route('/chat', methods=['POST'])
def chat():
    return jsonify({'response': 'fuck off'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
