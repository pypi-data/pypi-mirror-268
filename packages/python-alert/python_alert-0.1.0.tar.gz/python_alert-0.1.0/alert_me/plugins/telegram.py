import logging

from alert_me.plugin import Plugin

import requests


class TelegramPlugin(Plugin):
    name = "telegram"
    required_init_params: dict["str", type] = {"token": str, "chat_id": str}
    required_notify_params: dict["str", type] = {"message": str}

    def notify(self, notify_params: dict[str, any]):
        super().notify(notify_params)
        requests.post(
            f"https://api.telegram.org/bot{self.init_params['token']}/sendMessage",
            data={
                "chat_id": self.init_params["chat_id"],
                "text": notify_params["message"],
                "disable_web_page_preview": "True",
                "parse_mode": "MarkDown",
            },
        )
        logging.info(
            f"Telegram message sent successfully to {self.init_params['chat_id']}: {notify_params['message']}"
        )
