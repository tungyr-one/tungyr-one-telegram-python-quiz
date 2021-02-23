# https://www.youtube.com/watch?v=LJdu68ro-rU&ab_channel=GeekCode
# doc: https://github.com/eternnoir/pyTelegramBotAPI
# https://core.telegram.org/bots/api


import random
import pickle

import telebot
from telebot import types
from telebot.types import Message

from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)
sticker_id = 'CAADAgADOQADfyesDlKEqOOd72VKAg'
sticker_id2 = 'CAADAgADqAIAAkcVaAllGKpjZDCAgQI'

USERS = set()
questions = []

# https://pythonru.com/primery/telegram-bot-na-python-ustanovka-i-nastrojka
#
@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    if '/help' in message.text:
        bot.reply_to(message, 'This bot is developing by Tungyr')

    if '/start' in message.text:
        bot.reply_to(message, 'Test is starting!')
        quest = test()
        bot.send_message(message.chat.id, quest)
        answer_handler(message)


    return


def test():
    with open('test.txt', 'r') as f:
        [questions.append(question) for question in f.readlines()]
    print(questions)
    for i in questions:
        yield i


# @bot.infinity_polling(lambda query: query.query)
# def query_text(inline_query):
#     try:
#         r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
#         r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
#     except Exception as e:
#         print(e)



@bot.message_handler(content_types=['text'])
def answer_handler(message: Message):
    print(message.chat.id)
    print(message.content_type)
    bot.reply_to(message, 'Right!')
    return



# @bot.message_handler(content_types=['text'])  # бот реагирует на текст
# @bot.edited_message_handler(content_types=['text'])  # бот реагирует на отредактированный текст тоже
# def echo_digits(message: Message):
#     print(message.from_user.id)
#     print(USERS)
#     if message.from_user.id in USERS:
#         reply = f'{message.from_user.first_name}, hello again!'
#     else:
#         reply = f'Hello {message.from_user.first_name}!'
#
#     bot.reply_to(message, reply)
#     USERS.add(message.from_user.first_name)
#     print(USERS)
#
#     if 'Victor' in message.text:  # реагирование на слово в тексте сообщения
#         bot.reply_to(message, 'Victor the best!')
#         return
#
#     if 'pow' in message.text:
#         digit = ''
#         for i in message.text:
#             if i.isdigit():
#                 digit = digit + i
#         if len(digit) == 0:
#             digit = 0
#         result = int(digit) ** int(digit)
#         bot.reply_to(message, f'The pow of {digit} is {str(result)}')
#
#     # if 'pic' in message.text:  # Not working
#     #     photo = open('girl.jpg', 'rb')
#     #     bot.reply_to(message, photo)
#
#     else:
#         # bot.reply_to(message, str(random.random()))  # reply as random digit
#         # bot.reply_to(message, 'Your message: ' + message.text)  # send back user's message text
#         # print(message.json)
#         pass
#
# @bot.message_handler(func=lambda m: True)  # ответ на любые сообщения текстом отправленного сообщения
# def echo_all(message):
#     bot.reply_to(message, message.text)



#
# upd = bot.get_updates()  # получение обновлений, как вытащить из него данные?
# for i in upd:
#     print(i)


bot.polling(timeout=60)
