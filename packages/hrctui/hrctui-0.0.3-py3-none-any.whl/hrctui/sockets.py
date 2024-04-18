import base64
import json
import random
import string

import websockets
from textual.app import App

from hrctui.crypto import Crypto


class Sockets:
    url = "wss://hrc.hecur.ru/sockets"
    key = ""
    websocket = None

    def __init__(self, username, password, crypto: Crypto, app: App, MessagesContainer, Message, ContentSwitcher, notifications):
        self.username = username
        self.password = password
        self.crypto = crypto
        self.app = app
        self.MessagesContainer = MessagesContainer
        self.Message = Message
        self.ContentSwitcher = ContentSwitcher
        self.notifications = notifications

    def xor_cypher(self, message):
        return ''.join(chr(ord(char) ^ ord(self.key[i % len(self.key)])) for i, char in enumerate(message))

    def encrypt(self, message):
        # Добавляем случайный символ в начало сообщения
        message = random.choice(string.ascii_letters) + message
        encrypted_message = self.xor_cypher(message)
        return base64.b64encode(encrypted_message.encode()).decode()

    def decrypt(self, encrypted_base64):
        encrypted_message = base64.b64decode(encrypted_base64).decode()
        # Убираем случайный символ из начала сообщения
        return self.xor_cypher(encrypted_message)[1:]

    async def send_message(self, recipient, msg):
        await self.websocket.send(json.dumps({
            'event': 'MESSAGE',
            'data': {
                'recipient': recipient,
                'message': self.encrypt(msg)
            }
        }))

    async def handle_info_event(self, message_data, websocket):
        msg = message_data['message']
        if msg and msg.startswith('Подключен.'):
            print(message_data)
            self.key = message_data['key']
            await websocket.send(json.dumps({
                'event': 'auth',
                'data': {
                    'username': self.encrypt(self.username),
                    'password': self.encrypt(self.password)
                }
            }))
        elif msg and msg.startswith('Успешный'):

            print("Вы успешно вошли!")

    async def handle_message_event(self, message_data, websocket):
        if message_data['sender'] == self.app.api.username:
            return

        msg = self.crypto.decrypt(self.decrypt(str(message_data['message'])))
        nickname = self.app.api.nicknames.get(message_data['sender'])

        await self.app.friendButtons.get(message_data['sender'])[1].add_message(self.Message(nickname, msg))
        msg = (msg[:50] + "...") if len(msg) >= 51 else msg
        self.app.friendButtons.get(message_data['sender'])[0].set_last_message(msg)

        if self.app.selectedFriend and self.app.selectedFriend.username != message_data['sender']:
            self.notifications.new_message(message_data['sender'], msg)
        else:
            if not self.app.focused:
                self.notifications.new_message(message_data['sender'], msg)


    async def handle_online_event(self, message_data, websocket):
        self.app.friendButtons.get(message_data['user'])[0].set_online(True)

    async def handle_offline_event(self, message_data, websocket):
        self.app.friendButtons.get(message_data['user'])[0].set_online(False)

    async def start_task(self):
        async with websockets.connect(self.url) as websocket:
            self.websocket = websocket
            async for message in websocket:
                data = json.loads(message)
                event = data['event']
                message_data = data['data']
                self.app.log(message_data)

                event_handlers = {
                    'INFO': self.handle_info_event,
                    'MESSAGE': self.handle_message_event,
                    'ONLINE': self.handle_online_event,
                    'OFFLINE': self.handle_offline_event,
                }

                handler = event_handlers.get(event)
                if handler:
                    await handler(message_data, websocket)
                else:
                    print(data)
