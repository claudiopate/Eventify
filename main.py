from typing import Final
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from commands.core.base_command import start_command, help_command, cancel
from commands.loader.pdf_loader import upload, WAITING_FOR_PDF
from handlers.loader.pdf_handler.pdf_handler import handle_pdf
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
    
    # Configurazione del ConversationHandler per gestire la sequenza di comandi
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('upload', upload)],  # Il comando che avvia la sequenza
        states={
            WAITING_FOR_PDF: [MessageHandler(filters.Document.PDF, handle_pdf)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]  # Comando per annullare l'operazione
    )
    app.add_handler(conv_handler)    
    
    #Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #Error
    app.add_error_handler(error)
    
    print('Polling...')
    app.run_polling(poll_interval=3)
    