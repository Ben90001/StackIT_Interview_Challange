import requests
import json

url = "http://localhost:8000/siren"

with open("test_requests.json") as f:
    posts = json.load(f)

for post in posts:
    response = requests.post(url, json=post)
    print(response.status_code)
    if response.content:
        print(response.json())
    else:
        print("No JSON response")
