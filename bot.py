# https://www.youtube.com/watch?v=LJdu68ro-rU&ab_channel=GeekCode
# doc: https://github.com/eternnoir/pyTelegramBotAPI

import random
import telebot
from telebot.types import Message

from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    if '/help' in message.text:
        bot.reply_to(message, 'This bot is developing by Tungyr')
    else:
        bot.reply_to(message, 'Menu is developing now:(')
        print(message.text)


@bot.message_handler(content_types=['sticker'])  # react to stickers
def sticker_handler(message: Message):
    print(message.text)
    print(message.sticker)


@bot.message_handler(content_types=['text'])  # бот реагирует на текст
@bot.edited_message_handler(content_types=['text'])  # бот реагирует на отредактированный текст тоже
def echo_digits(message: Message):
    if 'Victor' in message.text:  # реагирование на слово в тексте сообщения
        bot.reply_to(message, 'Victor the best!')
        print(message.text)
        return

    if 'pow' in message.text:
        digit = ''
        for i in message.text:
            if i.isdigit():
                digit = digit + i
        if len(digit) == 0:
            digit = 0
        result = int(digit) * int(digit)
        bot.reply_to(message, f'The pow of {digit} is {str(result)}')

    # if 'pic' in message.text:  # Not working
    #     photo = open('girl.jpg', 'rb')
    #     bot.reply_to(message, photo)

    # else:
        # bot.reply_to(message, str(random.random()))  # reply as random digit
        # bot.reply_to(message, 'Your message: ' + message.text)  # send back user's message text
        # print(message.text)



# @bot.message_handler(func=lambda m: True)  # ответ на любые сообщения текстом отправленного сообщения
# def echo_all(message):
#     bot.reply_to(message, message.text)

bot.polling(timeout=60)

