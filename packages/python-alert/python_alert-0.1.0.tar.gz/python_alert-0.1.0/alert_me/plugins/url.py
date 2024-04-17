from alert_me.plugin import Plugin

import requests


class UrlPlugin(Plugin):
    name = "url"
    required_init_params: dict["str", type] = {}
    required_notify_params: dict["str", type] = {"method": str, "url": str}

    def notify(self, notify_params: dict[str, any]):
        super().notify(notify_params)
        requests.request(notify_params["method"], notify_params["url"])
