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
