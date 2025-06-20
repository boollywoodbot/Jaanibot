from pyrogram import Client, filters
import os

# Load .env file **ONLY if** running locally
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

api_id = int(os.environ.get("21905616"))
api_hash = os.environ.get("0506d1a8b04f4c580c369b47c885bbd4")
bot_token = os.environ.get("8126788658:AAFd57pq2CiSn0-T1c51ig79ji4k230nrH4")

app = Client(
    "cobra_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello from Cobra Bot 🐍")

if __name__ == "__main__":
    app.run()

