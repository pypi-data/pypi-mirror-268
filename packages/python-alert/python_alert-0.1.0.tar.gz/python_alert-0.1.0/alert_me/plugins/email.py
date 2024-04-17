import smtplib, ssl

from alert_me.plugin import Plugin

import requests


class EmailPlugin(Plugin):
    name = "email"
    required_init_params: dict["str", type] = {
        "smtp_server": str,
        "smtp_port": int,
        "sender_email": str,
        "sender_password": str,
    }
    required_notify_params: dict["str", type] = {
        "receiver_email": str,
        "subject": str,
        "message": str,
    }

    def notify(self, notify_params: dict[str, any]):
        super().notify(notify_params)

        message = f"From: {self.init_params['sender_email']}\r\nTo: {notify_params['receiver_email']}\r\nSubject: {notify_params['subject']}\r\n\r\n{notify_params['message']}"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            self.init_params["smtp_server"],
            self.init_params["smtp_port"],
            context=context,
        ) as server:
            server.ehlo()
            server.login(
                self.init_params["sender_email"], self.init_params["sender_password"]
            )
            server.sendmail(
                self.init_params["sender_email"],
                notify_params["receiver_email"],
                message,
            )
