"""
The module was created to check letters and mail for blacklisting.
All scripts from this module require python 3.10 and higher.
And install libraries from file requirements.txt.
pip freeze < requirements.txt
"""
import datetime
import pprint
import smtplib
import subprocess
import time

import requests
import settings


def run_bash():
    """
    This function runs a bash script with three positional parameters passed to it.
    All settings in the settings.py file
    :return:
    """
    try:
        proc = subprocess.run([f'./run_email_command.sh "{settings.MESSAGE}" '
                               f'"{settings.USER_RECIPIENT}" '
                               f'"{settings.SUBJECT}" '
                               f'"{settings.CD_PATH}"'],
                              shell=True)
        print(proc)
    except Exception as _ex:
        err = f'{_ex}\nSCRIPT ERROR\nProject: {settings.PROJECT_NAME}'
        send_result_to_bot(err)
        print(err)
        raise SystemExit from _ex


def make_msg_to_bot(json_dict):
    """
    The function parses the JSON file from the API response and
    generates a notification message in the telegram bot.
    The function takes as an argument JSON
    :param json_dict:
    :return:
    """
    try:
        sender_ip = json_dict['signature']['subtests']['aRecord']['tested']
        sender_ip = ''.join([x for x in sender_ip if x.isdigit() or x == '.']).lstrip('..')
        return f'Sender IP: {sender_ip}\n' \
               f'Project: {settings.PROJECT_NAME}\n' \
               f'Sender address: {json_dict["messageInfo"]["bounceAddress"]}\n' \
               f'MailBox email: {json_dict["mailboxId"]}@mail-tester.com\n' \
               f'Date: {datetime.datetime.today().strftime("%d.%m.%Y")}\n' \
               f'Time: {datetime.datetime.now().strftime("%H:%M:%S")}\n' \
               f'Status: {json_dict["displayedMark"]}'
    except Exception as _ex:
        print(f'{json_dict["title"]}'
              f'User: {settings.USER_SENDER}')
        err = f'{_ex}\n{json_dict["title"]}\n' \
              f'\nUser: {settings.USER_SENDER}'
        send_result_to_bot(err)
        raise SystemExit from _ex


def send_result_to_bot(msg_):
    """
    The function takes as an argument the generated message from the make_msg_to_bot function.
    Then, using the API, sends a message to the telegram bot.
    When an error is received, if the telegram bot API does not work,
    the function will send email to the sender's email specified in the settings,
    with a message that the telegram API is not available.
    :param msg_:
    :return:
    """
    try:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/" \
              f"sendMessage?chat_id={settings.CHAT_ID}&text={msg_}"
        requests.get(url).json()
        print('Message sent successfully!!!')
    except Exception as _ex:
        send_email(message_=f'Failed to send message to telegram bot!!!\n'
                            f'User: {settings.USER_SENDER}',
                   err=True)
        raise SystemExit from _ex


def send_email(message_, err):
    """
    The function receives a message from the settings file and sends it to the verification mail.
    Instructions on how to allow the script to use your mail can be found in the settings file.
    :param message_:
    :param err:
    :return:
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(settings.USER_SENDER,
                     settings.SENDER_PASSWORD)
        if err is False:
            server.sendmail(settings.USER_SENDER,
                            settings.USER_RECIPIENT,
                            message_)
            print('The message was sent!')
        else:
            server.sendmail(settings.USER_SENDER,
                            settings.USER_SENDER,
                            message_)
            print('The ERROR message was sent!')
    except Exception as _ex:
        err = f'{_ex}\nFail login!!!\nUser: {settings.USER_SENDER}'
        send_result_to_bot(err)
        print(err)
        raise SystemExit from _ex


def sleep_(time_=35):
    """
    The function is waiting for an API response. The default is 25 seconds.
    :param time_:
    :return:
    """
    print('Waiting API...')
    time.sleep(time_)


if __name__ == '__main__':
    # send_email(message_=settings.MESSAGE, err=False)
    run_bash()

    sleep_()

    r = requests.get(settings.API_URL)
    data = r.json()
    pprint.pprint(data)

    send_result_to_bot(make_msg_to_bot(data))
