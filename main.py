from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# 👇 Yahan apne favourite members ke IDs baad me aayenge
FAV_USERS = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Favourite Bot Online!\n\nUse:\n/fav Quiz start ho gaya!"
    )

async def fav(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        text = "📢 Quiz Start!"
    else:
        text = " ".join(context.args)

    if not FAV_USERS:
        await update.message.reply_text(
            "❌ Abhi koi favourite member add nahi hai."
        )
        return

    msg = text + "\n\n"

    for uid in FAV_USERS:
        msg += f'<a href="tg://user?id={uid}">⭐ Member</a> '

    await update.message.reply_text(
        msg,
        parse_mode="HTML"
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("fav", fav))

print("Bot Started...")

app.run_polling()