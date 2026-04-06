import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from core.database import init_db, create_tables

from commands.start import start
from commands.help import help_command

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN não carregado do .env")

    init_db()
    create_tables()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🚀 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()