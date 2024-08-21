from telegram import Update
from telegram.ext import ContextTypes

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello thanks for have choosen this bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can load a pdf file with a table and I will extract calendar events")