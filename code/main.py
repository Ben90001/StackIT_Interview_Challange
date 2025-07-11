from fastapi import FastAPI, Request
from discord_poster import DiscordPoster

app = FastAPI()
discord = DiscordPoster("YOUR_DISCORD_WEBHOOK_URL")

@app.post("/send-message")
async def send_message(request: Request):
    data = await request.json()
    message = data.get("message")
    if not message:
        return {"error": "No message provided"}

    discord.post_message(message)
    return {"status": "Message sent"}
