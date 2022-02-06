import asyncio
from telethon import TelegramClient

bot_token = ''
api_id = 
api_hash = ''

f = open('chat_list.txt', 'r')  # открываем файл с чатами в режиме чтения
chats = [i for i in f]  # добавляем каждый элемент файла в список. Потом по этому списку будем осуществлять рассылку

async def spam():
	client = await TelegramClient('session', api_id, api_hash).start()
	while True:
		await asyncio.sleep(3600)  # сообщение присылается каждые 3600 секунд, то есть каждый час
		await asyncio.wait([
			client.send_message(chat, 'текст рассылки')
			for chat in chats
		])

if __name__ == '__main__':
	asyncio.get_event_loop().run_until_complete(spam())

