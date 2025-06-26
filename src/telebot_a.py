import configparser
import telebot
import time
import threading
"""
Bot creado como prueba
"""
# Obtenemos credenciales de nuestro config.ini
cp = configparser.ConfigParser()
cp.read('./config.ini')
bot = telebot.TeleBot(cp['AUTH']['bot_token'])
bot.set_my_commands([
    telebot.types.BotCommand(command = '/start', description = 'Iniciar el bot')
])

@bot.message_handler(commands = ['start', 'help'])
def cmd_start(message):
    bot.reply_to(message, 'Hola, soy tu bot')
    
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text.startswith('/'):
        bot.send_message(chat_id = message.chat.id, text = f'Comando no disponible')
    else:
        x = bot.send_message(chat_id = message.chat.id, text = f'Hola')
        time.sleep(3)
        bot.delete_message(chat_id = message.chat.id, message_id = x.message_id, timeout = 5)
        
def thread_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    print('Iniciando bot')
    bot_thread = threading.Thread(name = 'ThreadBot', target = thread_bot)
    bot_thread.start()
    print('Bot iniciado')