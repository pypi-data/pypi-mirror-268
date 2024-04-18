from notifypy import Notify


class Notifications:

    def __init__(self):
        self.notify = Notify()

    def new_message(self, sender, msg):
        self.notify.title = sender
        self.notify.message = msg
        self.notify.send()
