import keyring

from hrctui.api import Api
from hrctui.pages import login_page, chats_page


def run():
    username = keyring.get_password("HRCCLUI", "username")
    password = keyring.get_password("HRCCLUI", "password")
    cert_path = keyring.get_password("HRCCLUI", "cert_path")

    if not username or not password or not cert_path:
        api, path = login_page.run()

        if api:
            keyring.set_password("HRCCLUI", "username", api.username)
            keyring.set_password("HRCCLUI", "password", api.password)
            keyring.set_password("HRCCLUI", "cert_path", path)

            chats_page.run(api)
    else:
        api = Api(username, password)

        result = chats_page.run(api)
        print(result)

        if result == "login":
            keyring.delete_password("HRCCLUI", "username")
            keyring.delete_password("HRCCLUI", "password")
            keyring.delete_password("HRCCLUI", "cert_path")
            run()

if __name__ == "__main__":
    run()
