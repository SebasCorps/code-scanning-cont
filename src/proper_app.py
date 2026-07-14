from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Secure approach: load the API key from an environment variable instead of
# hardcoding it in source code
API_KEY = os.environ.get("API_KEY")


@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Welcome to the demo API"
    })


@app.route('/data')
def get_data():
    provided_key = request.headers.get('X-API-Key')

    if API_KEY and provided_key == API_KEY:
        return jsonify({
            "data": [
                {"id": 1, "name": "Item 1", "value": 100},
                {"id": 2, "name": "Item 2", "value": 200},
                {"id": 3, "name": "Item 3", "value": 300}
            ]
        })
    else:
        return jsonify({"error": "Unauthorized"}), 401


if __name__ == '__main__':
    app.run(debug=True, port=5000)
