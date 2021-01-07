# https://www.youtube.com/watch?v=LJdu68ro-rU&ab_channel=GeekCode

import requests

from config import TG_TOKEN

MAIN_URL = f'https://api.telegram.org/bot{TG_TOKEN}'

payload = {
    'chat_id': 354310062,
    'text': 'Nice to see you again!',
    'reply_to_message_id': 68
}

# r = requests.get(f'{MAIN_URL}/getUpdates')  # получение сообщения
r = requests.post(f'{MAIN_URL}/sendMessage', data=payload)  # отсылка сообщения
print(r)

print(r.json())

