import configparser
import telebot
"""
Bot creado como prueba
"""
# Obtenemos credenciales de nuestro config.conf
cp = configparser.ConfigParser()
cp.read('../config.conf')
bot = telebot.TeleBot(cp['AUTH']['bot_token'])

@bot.message_handler(commands = ['start', 'help'])

def cmd_start(message):
    bot.reply_to(message, 'Hola, soy tu bot')
    
if __name__ == '__main__':
    print('bot iniciado')
    bot.infinity_polling()