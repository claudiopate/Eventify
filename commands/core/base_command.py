from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello thanks for have choosen this bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can load a pdf file with a table and I will extract calendar events")
    
# Funzione per gestire l'annullamento
def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    update.message.reply_text("Operazione annullata")
    return ConversationHandler.END