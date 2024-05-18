import os

from dotenv import load_dotenv
from flask import Flask, request, render_template
from libversion import VersionUtil
import requests

app = Flask(__name__)
load_dotenv()

from flask import Flask, request, render_template, jsonify

@app.route('/')
def home():
    version_info = VersionUtil.VersionUtil.get_version()
    return render_template("index.html", version=version_info)

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['input_text']
    model_choice = request.form['model_select']
    model_service_url = os.getenv("MODEL_SERVICE_URL")

    payload = {
        'input_url': text,
        'model_name': model_choice
    }

    try:
        response = requests.post(model_service_url, json=payload, timeout=10)
        response.raise_for_status()
        prediction = response.text  # Assuming response.text is your prediction result

        return jsonify({'prediction': prediction})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to reach model service', 'exception': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)