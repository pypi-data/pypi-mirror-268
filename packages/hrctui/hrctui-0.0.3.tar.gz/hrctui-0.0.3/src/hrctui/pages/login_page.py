import asyncio
from tkinter import filedialog

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.reactive import reactive
from textual.widgets import Header, Input, Button, Static

from hrctui.api import Api


class FilePathDisplay(Static):
    text = reactive("")

    def watch_text(self, text: str) -> None:
        self.update(text)


class FileAsk(Static):
    def compose(self) -> ComposeResult:
        yield Button(label="Открыть ключ...", id="openkey")
        yield FilePathDisplay(id="filepath")


class Login(App):
    CSS_PATH = "tcss/main.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    ENABLE_COMMAND_PALETTE = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Center(Input(placeholder="Юзернейм", id="username"))
        yield Center(Input(placeholder="Пароль", id="password", password=True))
        yield Center(Button(label="Войти", id="login", disabled=True))
        yield FileAsk()

    @on(Input.Changed)
    def on_input(self):
        self.update_login_button_state()

    def update_login_button_state(self):
        self.query_one("#login", Button).disabled = not self.is_form_valid()

    def is_form_valid(self) -> bool:
        return (not self.query_one("#username", Input).value == "" and
                not self.query_one("#password", Input).value == "" and
                self.query_one(FilePathDisplay).text != "")

    @on(Button.Pressed)
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "login":
            api = Api(self.query_one("#username", Input).value, self.query_one("#password", Input).value)
            passed, data = await api.auth_user()
            if passed:
                self.exit((api, self.query_one(FilePathDisplay).text.replace('Выбран - ', "")))
            else:
                self.notify(data, title="Ошибка", severity='error', timeout=3)

        elif event.button.id == "openkey":
            self.open_key_file()

    def open_key_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".pem",
                                               filetypes=(('Certificate files (*.pem)', '*.pem'),))
        if file_path:
            self.query_one(FilePathDisplay).text = 'Выбран - ' + file_path
            self.update_login_button_state()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


def run():
    app = Login()
    return app.run()
