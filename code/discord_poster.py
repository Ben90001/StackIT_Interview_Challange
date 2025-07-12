import requests
import json

class DiscordPoster:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def _forwarding_required(message: str) -> bool:
        try:
            data = json.loads(message)
            return data.get("Type") == "Warning"
        except (json.JSONDecodeError, TypeError):
            return False

    def post_message(self, message: str):
        data = {"username" : "Siren", 
                "content": message}
        response = requests.post(self.webhook_url, json=data)
        response.raise_for_status()
