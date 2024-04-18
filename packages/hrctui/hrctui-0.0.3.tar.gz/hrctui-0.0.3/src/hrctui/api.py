import aiohttp

from hrctui.crypto import Crypto


class Api:
    server = "https://hrc.hecur.ru/api"
    dict = {}

    nicknames = {}

    def __init__(self, username="", password=""):
        self.token = None
        self.username = username
        self.password = password

    async def get_me_dict(self):
        async with aiohttp.ClientSession() as session:
            for i in ["nickname", "email"]:
                status, data = await self.get_request(f"/me/{i}", {}, session, True)
                self.dict[i] = data if status == 200 else None

        self.nicknames[self.username] = self.dict.get("nickname")

    async def get_friends(self):
        async with aiohttp.ClientSession() as session:
            status, data = await self.get_request("/me/friends", {}, session, True)
            return data if status == 200 else None

    async def get_friend_info(self, username, value: str | list):
        value = value if isinstance(value, list) else [value]

        async with aiohttp.ClientSession() as session:
            result = []
            for v in value:
                status, data = await self.get_request(f"/users/{username}/{v}", {}, session, True)
                result.append(data if status == 200 else None)
            return tuple(result) if len(result) > 1 else result[0]

    async def get_messages(self, username, amount, skip, crypto: Crypto) -> list:
        async with aiohttp.ClientSession() as session:
            status, messages = await self.get_request(f"/messages/{username}",
                                                      {'amount': amount, 'skip': skip},
                                                      session,
                                                      True)

            return [
                {
                    'id': msg['id'],
                    'sender': msg['sender'],
                    'message': crypto.decrypt(msg['message']),
                    'sended': msg['sended'],
                }

                for msg in messages] if status == 200 else None

    async def auth_user(self):
        async with aiohttp.ClientSession() as session:
            status, data = await self.get_request("/login",
                                                  {'username': self.username,
                                                   'password': self.password}, session)
            if status == 200:
                self.token = data
                await self.get_me_dict()
            return status == 200, data

    async def get_request(self, endpoint, params: dict, session: aiohttp.ClientSession, auth: bool = False):
        if auth: params['token'] = self.token
        try:
            response = await session.get(
                self.server + endpoint,
                params=params
            )

            if response.status == 401 and "Неверные учетные данные" in response.content:
                result, data = await self.auth_user()
                if result:
                    return await self.get_request(endpoint, params, session, auth)
                else:
                    return 500, data

            return response.status, await response.json()
        except aiohttp.ClientError as e:
            return 500, str(e)
