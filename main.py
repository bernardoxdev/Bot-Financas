import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from commands.start import start
from commands.help import help_command
from commands.ping import ping

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))

    print("🚀 Bot rodando...")
    app.run_polling()


if __name__ == "__main__":
    main()