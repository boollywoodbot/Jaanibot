from pyrogram import Client, filters
import os

app = Client(
    "cobra_bot",
    api_id=int(os.environ.get("21905616")),
    api_hash=os.environ.get("0506d1a8b04f4c580c369b47c885bbd4"),
    bot_token=os.environ.get("8126788658:AAFd57pq2CiSn0-T1c51ig79ji4k230nrH4")
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello from Cobra Bot 🐍")

if name == "__main__":
    app.run()
