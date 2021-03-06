import time
from telethon.sync import TelegramClient
api_id = ''
api_hash = ''


def send_message(text_message, time_sleep):
    with TelegramClient('Session', api_id, api_hash) as client:
        while True:
            for id in open('chat_list.txt'):
                id.replace('\n', '')
                client.send_message(id, text_message)
            time.sleep(time_sleep)

    client.run_until_disconnected()


if __name__ == '__main__':
    text = input('Напишите текст для рассылки: ')
    time_sleep = int(input('Введите интервалы отправки: '))
    send_message(text, time_sleep)
