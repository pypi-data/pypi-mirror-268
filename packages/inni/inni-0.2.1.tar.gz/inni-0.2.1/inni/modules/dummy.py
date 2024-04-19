from inni.modules.base import BaseModule
from inni.template import render_template


class Module(BaseModule):
    login_template_keys = ("login_template",)
    logout_template_keys = ("logout_template",)

    def login(self, responses):
        x = render_template(self.config["login_template"], **responses)
        print("Rendered template:", x)

    def logout(self, responses):
        x = render_template(self.config["logout_template"], **responses)
        print("Rendered template:", x)
