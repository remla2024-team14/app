# App
URL fishing detection application containing frontend and service.
The webpage displays the version of the library and it has a textbox where the user can provide a URL.
The user is able to choose the model it wants to use for predictions. After providing these details, 
the user can submit the information and it will send a request to the app-service for the results.

# Service

Flask is used to create API endpoints. 
This service contains an endpoint `/predict` for requesting predictions from the model-service at `MODEL_SERVICE_URL`.
URL of the model-service can be configured in the `.env` file by changing `MODEL_SERVICE_URL=YOUR_URL`.

# Usage
In the front-end the user should provide a URL and the model they want to use to make a prediction. 
After providing this information the user clicks submit to let the model make a prediction.
The version of the library is automatically displayed on the webpage.


