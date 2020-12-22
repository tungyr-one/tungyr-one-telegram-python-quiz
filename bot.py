# https://www.youtube.com/watch?v=LJdu68ro-rU&ab_channel=GeekCode

import telebot

from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)

bot.polling(timeout=60)

