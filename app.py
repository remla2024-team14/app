import os

from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from libversion import VersionUtil
import requests

app = Flask(__name__)
CORS(app)
load_dotenv()


@app.route('/')
def home():
    version_info = VersionUtil.VersionUtil.get_version()
    return render_template("index.html", version=version_info)


@app.route('/predict', methods=['POST'])
def predict():
    # Receive data from the front end
    text = request.form['input_text']
    model_choice = request.form['model_select']

    model_service_url = os.getenv("MODEL_SERVICE_URL")

    payload = {
        'input_url': text,
        'model_name': model_choice
    }

    try:
        response = requests.post(model_service_url, json=payload, timeout=10)  # timeout in seconds
        response.raise_for_status()

        # should get the response and return "prediction"

    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        prediction = {'error': 'Failed to reach model service', 'exception': str(e)}

    # Response
    return jsonify({
        "input": text,
        "model_used": model_choice,
        "prediction": prediction
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # Run on a different port to avoid conflict
