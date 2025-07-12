from fastapi import FastAPI, Request
from discord_poster import DiscordPoster




app = FastAPI()
with open("../data/discord_webhook.txt", "r") as file:
    webhook_url = file.read().strip()
discord = DiscordPoster(webhook_url, "Siren")

# listen to incomming messages
@app.post("/siren")
async def send_message(request: Request):
    data = await request.json()
    type = data.get("Type")
    if not type:
        return {"error": "No Type provided"}
    elif (type == "Warning"):
        discord.post_warning(data)
        return {"status": "Warning sent"}
    return {"status": "Type not a warning"}
 

discord.post_message("The Webservice is now active and will Provide you with critical Warnings")