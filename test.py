# https://www.youtube.com/watch?v=JC2QSNrOUs8&ab_channel=IT%D0%BA%D0%B0%D0%B6%D0%B4%D1%8B%D0%B9%D0%B4%D0%B5%D0%BD%D1%8C&t=7s

from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import datetime

from config import TG_TOKEN

button_help = 'Help'
# button_converter = 'Converter'
button_more = 'More'

def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Help is here',
        reply_markup=ReplyKeyboardRemove(),  # button remove after button press
    )

def button_more_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=str(datetime.datetime.now()) + ' This bot is developing by Victor the Staunch:)',
        reply_markup=ReplyKeyboardRemove(),
    )

# def button_converter_handler(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         text=str(datetime.datetime.now()) + ' This bot is developing by Victor the Staunch:)',
#         reply_markup=ReplyKeyboardRemove(),
#     )

# больше про CallbackContext - https://www.youtube.com/watch?v=HuuBYE9ND-k
def message_handler(update: Update, context: CallbackContext):
    """My message handler"""
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context=context)
    if text == button_more:
        return button_more_handler(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        # keyboard=[[KeyboardButton(text=button_help), ], ], resize_keyboard=True, )
        keyboard=[
            [
                KeyboardButton(text=button_help),
            ],
            [
                KeyboardButton(text=button_more)
            ],
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text='Hi! Push button below:',
        reply_markup=reply_markup,
    )

def main():
    print('Start')

# объект класса, принимающий данные от бота и прогоняющий их по всем бизнес логикам
    updater = Updater(
        token=TG_TOKEN,
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()  # запуск скачивания обновлений
    updater.idle()  # код в stand by

if __name__ == '__main__':
    main()


