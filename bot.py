# https://www.youtube.com/watch?v=LJdu68ro-rU&ab_channel=GeekCode
# doc: https://github.com/eternnoir/pyTelegramBotAPI
# https://core.telegram.org/bots/api

import random
import telebot
from telebot.types import Message

from config import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)
sticker_id = 'CAADAgADOQADfyesDlKEqOOd72VKAg'
sticker_id2 = 'CAADAgADqAIAAkcVaAllGKpjZDCAgQI'

@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    if '/help' in message.text:
        bot.reply_to(message, 'This bot is developing by Tungyr')
    else:
        bot.reply_to(message, 'Menu is developing now:(')
        print(message.text)
        return


@bot.message_handler(content_types=['text', "sticker"])  # react to stickers (not working)
def sticker_handler(message: Message):
    print(message.chat.id)
    print(message.content_type)
    # if message.content_type == ['sticker']:
    #     bot.send_sticker(message.chat.id, sticker_id2, reply_to_message_id=message.id, )
    # bot.get_sticker_set('sticker-set')
    bot.send_sticker(message.chat.id,'https://telegram.org/file/811140823/2/gEXq-ZISs9g/55f6c9c9f87c4dceb0')
    return



# @bot.message_handler(content_types=['text'])  # бот реагирует на текст
# @bot.edited_message_handler(content_types=['text'])  # бот реагирует на отредактированный текст тоже
# def echo_digits(message: Message):
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
