from fastapi import FastAPI, Request
from discord_poster import DiscordPoster




app = FastAPI()
with open("../data/discord_webhook.txt", "r") as file:
    webhook_url = file.read().strip()
discord = DiscordPoster(webhook_url)

# listen to incomming messages
@app.post("/send-message")
async def send_message(request: Request):
    data = await request.json()
    message = data.get("message")
    if not message:
        return {"error": "No message provided"}
    discord.post_message(message)
    return {"status": "Message sent"}
 

discord.post_message("This is a test message")