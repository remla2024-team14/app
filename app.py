from flask import Flask, request, render_template, jsonify
from libversion import VersionUtil
import requests

app = Flask(__name__)


@app.route('/')
def home():
    version_info = VersionUtil.VersionUtil.get_version()
    return render_template("index.html", version=version_info)


@app.route('/predict', methods=['POST'])
def predict():
    # Receive data from the front end
    text = request.form['input_text']
    model_choice = request.form['model_select']

    model_service_url = 'http://0.0.0.0:5000/predict'

    payload = {
        'input_url': text,
        'model_name': model_choice
    }

    # POST request to model service
    response = requests.post(model_service_url, json=payload)

    # Prediction from model service
    if response.status_code == 200:
        prediction = response.json()
    else:
        prediction = {'error': 'Failed to get prediction from the model service'}

    # Response
    return jsonify({
        "input": text,
        "model_used": model_choice,
        "prediction": prediction
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # Run on a different port to avoid conflict
