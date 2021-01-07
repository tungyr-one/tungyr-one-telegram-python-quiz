# https://www.youtube.com/watch?v=LJdu68ro-rU&ab_channel=GeekCode

import random
import telebot
from telebot.types import Message

from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Menu is developing now:(')


@bot.message_handler(content_types=['text'])  # бот реагирует на текст
def echo_digits(message: Message):
    if 'Victor' in message.text:  # реагирование на слово в тексте сообщения
        bot.reply_to(message, 'Victor the best!')
        return
    bot.reply_to(message, str(random.random()))



bot.polling(timeout=60)

