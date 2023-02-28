"""
---BASH SCRIPT CONF---
"""
CD_PATH = '/home/igor/prj/ground'  # Path to project directory/Needed for a bash script!
"""
---MAIL TESTER API SETTINGS---
You need to register an account in (https://www.mail-tester.com/).
They give 20 tests for free.
In the variable USER_NAME_MAIL_TESTER we indicate the name of the registered account,
in the variable PROJECT_NAME we indicate the name of the project.
Variables values are automatically substituted into the link for the API.
"""
USER_NAME_MAIL_TESTER = 'igooooor'
PROJECT_NAME = 'test'
API_URL = f'https://www.mail-tester.com/{USER_NAME_MAIL_TESTER}-{PROJECT_NAME}&format=json'

"""
---MAIL SETTINGS---
We need two-step authentication on the account in google and create an application password,
We use it to send ERROR notification via SMTP.
"""
USER_SENDER = 'ezerskiyigor2000@gmail.com'
SENDER_PASSWORD = 'pteswlonlallwjoo'
USER_RECIPIENT = f'{USER_NAME_MAIL_TESTER}-{PROJECT_NAME}@mail-tester.com'  # Needed for a bash script!

"""
---TEST MESSAGE SETTINGS---
Here we write down the message and the subject for the test letter.
"""
MESSAGE = 'TEST!sefe!!'  # Needed for a bash script!
SUBJECT = 'Test Email with exceptions'  # Needed for a bash script!

"""
---TELEGRAM API SETTINGS---
To get the CHAT_ID, you need to write any message to the bot and run the check_chat_id.py script.
The output will be JSON where we need the 'chat' field: {'id': 565280161, ...
-------------------------------------------------- -------------------------------------------------- -
Another option is to go to your telegram and find the Get My ID bot -> https://t.me/getmyid_bot
Press start, copy the Current chat ID: 565280161 field and paste the field value into our variable.
"""
TELEGRAM_BOT_TOKEN = '6113563336:AAGMBFWxOdDQbe1KOA6TCQJ5YGguunzf5_Q'
CHAT_ID = '565280161'
