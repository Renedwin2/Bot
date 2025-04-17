from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

BOT_TOKEN = os.getenv("7718024967:AAFeR4uU8dsDnKZOKKuuTOucFXRwdUVkms")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from Render!")

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
