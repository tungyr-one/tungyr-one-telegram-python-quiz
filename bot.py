# https://www.youtube.com/watch?v=LJdu68ro-rU&ab_channel=GeekCode

import requests

from config import TG_TOKEN

MAIN_URL = f'https://api.telegram.org/bot{TG_TOKEN}'

r = requests.get(f'{MAIN_URL}/getUpdates')
print(r)

print(r.json())

