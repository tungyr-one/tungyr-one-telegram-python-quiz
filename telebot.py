import telebot
from telebot.types import Message
from config import TG_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    pass

bot.polling(timeout=60)
