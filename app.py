from pyrogram import Client, filters
import os

app = Client(
    "cobra_bot",
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN")
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello from Cobra Bot 🐍")

if name == "__main__":
    app.run()
