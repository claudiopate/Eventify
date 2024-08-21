from telegram import Update
from telegram.ext import ContextTypes
from typing import Final
from dotenv import load_dotenv, dotenv_values
import os


USERNAME_BOT: Final = os.getenv('USERNAME_BOT')

#Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hey There!'
    if 'how are you' in processed:
        return 'I am good!'
    
    return 'I do not understand what you wrote'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if USERNAME_BOT in text:
            new_text: str = text.replace(USERNAME_BOT, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot: ', response)
    await update.message.reply_text(response)