import logging

from alert_me.plugin import Plugin


class AlertMe:
    def __init__(self, plugins: list[Plugin]):
        self._plugins = plugins

    def notify(self, notify_params: dict[str, any]) -> None:
        """
        Notify all plugins

        Args:
            notify_params (dict[str, any]): The parameters to notify the plugins with
        """
        for plugin in self._plugins:
            plugin.notify(notify_params)
