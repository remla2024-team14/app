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

# How to: Custom Docker Network

If you haven't already, you should make a docker network to make sure that the IP address stays the same when running the image.
_Note: `app` and `model-service` have to be on the same network_.
You can do this by executing this command in terminal: `docker network create --subnet=172.0.0.0/16 <yournetworkname>`

To build your Docker image, execute the following command in your terminal: `docker build .`
To start a container from your image, use this command: `docker run -p 8000:8000 --net <yournetworkname> --ip <ip-arg> --name appcontainer <yourappimghash>`

- Replace `<yournetworkname>` with your chosen network name
- Replace `<ip-arg>` with some ip matching your subnet e.g. `172.0.0.5`. _Note: It has to be different from the IP of the model service._
- Replace `<yourappimghash>` with the actual hash or tag of your Docker image.

In `model-service` you had to choose `<ip-arg>` as well, this argument serves as your `MODEL_SERVICE_URL`
Hence, in `.env` please set `MODEL_SERVICE_URL=http://<model-service-ip-arg>:5000/predict` e.g. `MODEL_SERVICE_URL=http://172.0.0.4:5000/predict`.

# Vagrant

_NOTE: unsure if it works for ARM, cause I cannot test it._

Make sure you have Vagrant and VirtualBox/VMWare installed.
Navigate to the Vagrantfile for ARM or x86 (normal) and run `vagrant up` in terminal. It will create 1 controller node and 2 worker nodes.
IP has been made static for more convenient later use with Kubernetes.

## Vagrant Config

Controller node IP is:

`CONTROLLER_IP = "192.168.50.10"`

`X = {11, 12}`
`NETWORK_PREFIX = "192.168.50.X"`

Furthermore, the names are "controller", "node1" and "node2". You can run them by using `vagrant ssh <NAME>` from the directory that contains the Vagrantfile.

To test the communication between the VMs I ran all the VMs on different terminals. You can check the IP of the VM by typing `ip address` on their respective terminals. I then pinged every other VM from one of the other VMs using `ping <IP_ADDRESS>` and I did this for all of them. The result from node1 to node2 looks like this: ![image](https://github.com/remla2024-team14/app/assets/72865119/e8be97a1-d1cc-4311-91da-37469c3874a3).

# Prometheus and Grafana

To run Prometheus locally without helm, you need to make sure Prometheus is installed, then run prometheus.exe --config.file=prometheus.yml.
To run Grafana locally, just download it and it will continually run on your localhost on port 3000 (use a browser to go to 127.0.0.1:3000). Then configure a data source to the port Prometheus is running (by default, localhost:9093) and importing the dashboard JSON located in the path grafana-dashboards/dashbard.json.
