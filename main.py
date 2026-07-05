from pyrogram import Client, filters

API_ID = 123456
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

app = Client(
    "favbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

favorites = []

@app.on_message(filters.command("add"))
def add(client, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        if user.id not in favorites:
            favorites.append(user.id)
            message.reply("✅ User added to favorites")

@app.on_message(filters.command("fav"))
def fav(client, message):
    text = " ".join([f"[‎](tg://user?id={i})" for i in favorites])
    message.reply(text)

app.run()
