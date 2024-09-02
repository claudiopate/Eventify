from telegram import Update
from telegram.ext import ContextTypes

#Status of waiting
WAITING_FOR_PDF = 1

async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE )-> int:
    await update.message.reply_text("Load Your PDF file")
    return WAITING_FOR_PDF