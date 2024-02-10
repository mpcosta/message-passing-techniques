from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'response': 'Hello World!'})
