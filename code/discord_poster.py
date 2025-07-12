import requests
import json

class DiscordPoster:
    def __init__(self, webhook_url: str, username:str):
        self.webhook_url = webhook_url
        self.username = username

    def post_message(self, message: str):
        data = {"username" : self.username, 
                "content": message}
        response = requests.post(self.webhook_url, json=data)
        response.raise_for_status()

    def post_warning(self, message: json):
        content = f"[{message['Type']}] {message['Name']}: {message['Description']}"
        data = {"username": self.username,
                "content": content}
        response = requests.post(self.webhook_url, json=data)
        response.raise_for_status()
