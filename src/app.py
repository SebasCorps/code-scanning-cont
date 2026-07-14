from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Exposed API key for demonstration purposes
# WARNING: In a real application, this would be stored in environment variables
# or a secure secrets manager, never hardcoded in source code
API_KEY = "sk_live_51NzUBTK9eVEGVDo5XMMFfhVfdbP994QI6Sd4UmYOMAGkzKaVp6f30XpkMUyLe6SBZ123"


@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Welcome to the demo API"
    })


@app.route('/data')
def get_data():
    # Insecure authentication method - API key exposed in code
    # This is intentionally vulnerable for demonstration purposes
    provided_key = request.headers.get('X-API-Key')

    if provided_key == API_KEY:
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
