import asyncio

import keyring
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Container, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Header, Static, Label, Button, Input, ContentSwitcher

from hrctui.api import Api
from hrctui.crypto import Crypto
from hrctui.notifications import Notifications
from hrctui.sockets import Sockets


class Message(Container):

    def __init__(self, nickname, message, *children: Widget, id=None):
        super().__init__(*children, id=id, classes="msgcont")
        self.nickname = nickname
        self.message = message

    def compose(self) -> ComposeResult:
        yield Label(self.nickname, classes="nickname")
        yield Static(self.message, classes="message")


class MessagesContainer(Container):
    messages = []
    need_upd = True
    vs = None

    def __init__(self, *children: Widget, id):
        super().__init__(*children, id=id)

    def clear_mesages(self):
        for m in self.messages:
            m.remove()
        self.messages.clear()

    async def add_message(self, message):
        self.messages.append(message)

        await self.vs.mount(message)
        if self.vs.max_scroll_y == self.vs.scroll_y:
            self.vs.scroll_end(animate=False)

    def compose(self) -> ComposeResult:
        yield VerticalScroll()
        yield InputBottom()

    async def on_mount(self) -> None:
        self.vs = self.query_one(VerticalScroll)


class InputBottom(Widget):

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Введите сообщение", classes="input_message")


class FriendButton(Button):
    last_message = ""
    last_msg_static = None

    def __init__(self, username, nickname, online, last_message):
        super().__init__()
        self.label = ""
        self.username = username
        self.nickname = nickname
        self.online = online
        self.last_message = last_message
        self.classes = "friend"
        self.can_focus_children = False

    def set_last_message(self, message):
        self.last_msg_static.update(message)


    def set_online(self, value):
        self.query_one(".fr_nickname").update(self.nickname + "🟢" if value else self.nickname)

    def compose(self) -> ComposeResult:
        yield Static(self.nickname + f"{self.online}", classes="fr_nickname")
        yield Static(self.last_message, classes="fr_last_msg")

    async def on_mount(self) -> None:
        self.last_msg_static = self.query_one(".fr_last_msg", Static)


class Chats(App):
    CSS_PATH = "tcss/chats.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    ENABLE_COMMAND_PALETTE = False

    sockets = None
    friendButtons = {}
    selectedFriend = None

    contentSwitcher = None

    def __init__(self, api: Api):
        super().__init__()
        self.api = api
        self.notifications = Notifications()
        self.crypto = Crypto(keyring.get_password("HRCCLUI", "cert_path"))

    def compose(self) -> ComposeResult:
        with Container(id="page"):
            with Container(id="leftSide"):
                yield Container(
                    Static(self.api.username + " - Онлайн", id="nick"),
                    id="me"
                )
                yield Container(
                    id="leftDown")

            with Container(id="rightSide"):
                with ContentSwitcher(initial="empty"):
                    yield Label("", id="empty")


    async def on_input_submitted(self, val):
        if "input_message" in val.control.classes:

            await self.sockets.send_message(self.selectedFriend.username, val.value)
            await self.app.query_one("#" + self.selectedFriend.username, MessagesContainer).add_message(Message(self.api.dict.get('nickname'), val.value))

            self.friendButtons.get(self.selectedFriend.username)[0].set_last_message((val.value[:50] + "...") if len(val.value) >= 51 else val.value)

            val.control.clear()
    async def update_messages(self, username):

        msgContainer = self.friendButtons.get(username)[1]

        msgContainer.clear_mesages()

        for msg in reversed(await self.api.get_messages(username, 10, 0, self.crypto)):
            await msgContainer.add_message(Message(self.api.nicknames.get(msg['sender']), msg['message']))
        msgContainer.vs.scroll_end()

    async def update_friends_btns(self):
        for key, value in self.friendButtons:
            value[0].remove()
            value[1].remove()
        self.friendButtons.clear()

        friends_list = await self.api.get_friends()
        container = self.query_one("#leftDown")
        for friend in friends_list:
            nickname, online = await self.api.get_friend_info(friend, ["nickname", "online"])
            self.api.nicknames[friend] = nickname
            message = await self.api.get_messages(friend, 1, 0, self.crypto)

            if len(message) != 0:
                fb = FriendButton(friend, nickname, "🟢" if online == 'True' else "", (message[0]['message'][:50] + "...") if len(message[0]['message']) >= 51 else message[0]['message'])
                fmc = MessagesContainer(id=friend)
                self.friendButtons[friend] = (fb, fmc)
                await container.mount(fb)
                await self.contentSwitcher.mount(fmc)
                self.contentSwitcher.current = friend

        self.contentSwitcher.current = "empty"

    async def on_mount(self) -> None:
        if not self.api.token:
            passed, data = await self.api.auth_user()
            if not passed:
                self.exit("login")
        self.sub_title = self.api.username
        self.contentSwitcher = self.query_one(ContentSwitcher)
        await self.update_friends_btns()

        self.sockets = Sockets(self.api.username, self.api.password, self.crypto, self, MessagesContainer, Message,
                               ContentSwitcher, self.notifications)

        asyncio.create_task(self.sockets.start_task())

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        button: FriendButton = event.button
        if "friend" in button.classes:
            button.disabled = True
            if self.selectedFriend:
                self.selectedFriend.disabled = False
            self.selectedFriend = button
            await self.update_messages(button.username)

            self.contentSwitcher.current = button.username



def run(api):
    app = Chats(api)
    return app.run()
