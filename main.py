from typing import Final
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from commands.core.base_command import start_command, help_command
from commands.loader.pdf_loader import load_document_pdf_command
from handlers.core.base_handler import handle_message
from handlers.error.error_base_handler import error
from typing import Final
from dotenv import load_dotenv, dotenv_values
import os


TOKEN: Final = os.getenv("TOKEN")

if __name__ == '__main__':
    print('Starting bot....')
    
    app = Application.builder().token(TOKEN).build()
    
    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('load_document_pdf', load_document_pdf_command))    
    
    #Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #Error
    app.add_error_handler(error)
    
    print('Polling...')
    app.run_polling(poll_interval=3)
    