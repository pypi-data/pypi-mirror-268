from telebot import TeleBot

def telegram(message, bot_id, server_id):
    TK = bot_id
    ID = server_id
    bot = TeleBot(TK)
    bot.send_message(ID, message)