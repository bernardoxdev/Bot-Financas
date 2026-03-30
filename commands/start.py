from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT O6S Finanças ONLINE!\n\nDigite /help para ver os comandos."
    )