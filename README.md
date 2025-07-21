# StackIT Interview: Siren Warning System
Creating a RESTful web service to forward warnings of from POST inputs to Discord.

## Dependencies
Install the following dependencies:
- Python FastAPI
- Python Requests
- Python Uvicorn

## Discord Webhook
Create a file `./data/discord_webhook.txt` and save your discord webhook inside.
The service will use this hook to send warnings to the respective channel.

## Run the Webservice
To run the service:
````
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
````
  
To test the service:
````
cd ./testing
python3 test_requests.py
````
## Docker
If you wish to containerize the service using Docker first install Docker:
````
curl -sSL https://get.docker.com | sh
````
Afterwards run you can simply run the set up script.
To do so first change permissions as follows:
````
chmod 700 build_siren_container.sh
./build_siren_container.sh
````