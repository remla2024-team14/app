# app
URL fishing detection application containing frontend and service

Contains endpoints so the front-end can make calls to the app service. 
Uses Flask to make calls to model service. 

Version of the library is displayed on the webpage.

# usage
In the front-end the user should provide a URL and the model they want to use to make a prediction.

Has `127.0.0.1:8000/predict` endpoint to make predictions.

URL of the model-service can be configured in the `.env` file by changing `MODEL_SERVICE_URL=YOUR_URL`
