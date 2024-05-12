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

# Docker

If you haven't already, you should make a docker network to make sure that the ip address stays the same when running the image. 
*Note: app and model service have to be on the same network*
You can do this by executing this command in terminal: `docker network create --subnet=172.0.0.0/16 <yournetworkname>`

To build your Docker image, execute the following command in your terminal: `docker build .`
To start a container from your image, use this command: `docker run -p 8000:8000 --net <yournetworkname> --ip <ip-arg> --name appcontainer <yourappimghash>`

Replace `<yournetworkname>` with your chosen network name
Replace `<ip-arg>` with some ip matching your subnet e.g. `172.0.0.5` 
*Note: It has to be different from the IP of the model service.*
Replace `<yourappimghash>` with the actual hash or tag of your Docker image.

In `model-service` you had to choose `<ip-arg>` as well, this argument serves as your `MODEL_SERVICE_URL`
In `.env` please set `MODEL_SERVICE_URL=http://<model-service-ip-arg>:5000/predict` e.g. `MODEL_SERVICE_URL=http://172.0.0.4:5000/predict`


