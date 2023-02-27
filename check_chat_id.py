"""
The module finds the user's chat ID.
"""
import pprint

import requests
import settings

if __name__ == '__main__':
    url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getUpdates'
    pprint.pprint(requests.get(url).json())
