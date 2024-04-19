import smtplib
from email.mime.text import MIMEText

from inni.modules.base import BaseModule
from inni.template import render_template


class Module(BaseModule):
    login_template_keys = ("login_subject", "login_body")
    logout_template_keys = ("logout_subject", "logout_body")

    def setUp(self):
        if self.config["ssl"]:
            self.mailer = smtplib.SMTP_SSL(self.config["host"], self.config["port"])
        else:
            self.mailer = smtplib.SMTP(self.config["host"], self.config["port"])

    def send_mail(self, sub, body):
        msg = MIMEText(body)
        msg["Subject"] = sub
        from_ = msg["From"] = self.config.get("from", self.config["username"])
        to = msg["To"] = ", ".join(self.config["to"])
        with self.mailer as smtp:
            smtp.login(self.config["username"], self.config["password"])
            smtp.sendmail(from_, to, msg.as_string())

    def login(self, responses):
        body = render_template(self.config["login_body"], **responses)
        subject = render_template(self.config["login_subject"], **responses)
        with self.out.status("[green]Sending Email"):
            self.send_mail(subject, body)
        self.out.print("[green]✅ Email sent")

    def logout(self, responses):
        body = render_template(self.config["logout_body"], **responses)
        subject = render_template(self.config["logout_subject"], **responses)
        with self.out.status("[green]Sending Email"):
            self.send_mail(subject, body)
        self.out.print("[green]✅ Email sent")
