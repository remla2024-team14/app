import os
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import requests
from libversion import VersionUtil
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_summary import Summary
from time import time

app = Flask(__name__)
load_dotenv()

# Prometheus metrics
feedback_yes_counter = Counter('feedback_yes_total', 'Total number of "Yes" feedbacks')
feedback_no_counter = Counter('feedback_no_total', 'Total number of "No" feedbacks')
inference_time_histogram = Histogram('inference_time_histogram', 'Duration of HTTP requests in seconds', ['method', 'endpoint'])
in_progress_requests_gauge = Gauge('in_progress_requests', 'Number of requests in progress', ['method', 'endpoint'])
inference_time_summary = Summary('inference_time_summary', 'Summary of inference times', ['method', 'endpoint'])
http_requests_total = Counter('http_requests_total', 'Total number of HTTP requests')

@app.before_request
def before_request():
    http_requests_total.inc()

@app.route('/')
def home():
    version_info = VersionUtil.VersionUtil.get_version()
    return render_template("index.html", version=version_info)

@app.route('/predict', methods=['POST'])
@inference_time_histogram.labels('POST', '/predict').time()
@in_progress_requests_gauge.labels('POST', '/predict').track_inprogress()
def predict():
    text = request.form['input_text']
    model_choice = request.form['model_select']
    model_service_url = os.getenv("MODEL_SERVICE_URL")

    payload = {
        'input_url': text,
        'model_name': model_choice
    }

    try:
        start_time = time()
        response = requests.post(model_service_url, json=payload, timeout=10)
        response.raise_for_status()
        duration = time() - start_time

        prediction = response.text

        return jsonify({'prediction': prediction})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to reach model service', 'exception': str(e)}), 500

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_type = request.json.get('feedback')
    if feedback_type == 'yes':
        feedback_yes_counter.inc()
    elif feedback_type == 'no':
        feedback_no_counter.inc()
    return jsonify({'status': 'success'})

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
