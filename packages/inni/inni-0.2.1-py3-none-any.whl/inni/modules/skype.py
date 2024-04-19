from skpy import Skype

from inni.modules.base import BaseModule
from inni.template import render_template


class Module(BaseModule):
    login_template_keys = ("login_template",)
    logout_template_keys = ("logout_template",)

    def setUp(self):
        self.sk = Skype(self.config["username"], self.config["password"])
        self.chat = self.sk.chats[self.config["chat_id"]]

    def send_message(self, msg):
        rich = self.config.get("rich", False)
        self.chat.sendMsg(msg, rich=rich)

    def login(self, responses):
        msg = render_template(self.config["login_template"], **responses)
        with self.out.status("[green]Sending Skype Message"):
            self.send_message(msg)
        self.out.print("[green]✅ Skype message sent")

    def logout(self, responses):
        msg = render_template(self.config["logout_template"], **responses)
        with self.out.status("[green]Sending Skype Message"):
            self.send_message(msg)
        self.out.print("[green]✅ Skype message sent")
