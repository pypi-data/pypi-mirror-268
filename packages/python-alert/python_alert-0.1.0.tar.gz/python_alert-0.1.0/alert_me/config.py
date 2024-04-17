import logging
import os

from alert_me.plugin import Plugin
from alert_me.plugins.telegram import TelegramPlugin
from alert_me.plugins.url import UrlPlugin
from alert_me.plugins.email import EmailPlugin

from configparser import ConfigParser

# Config file paths
# The first config file found will be used
CONFIG_FILE = [
    "~/.alert-me.conf",
    "~/.alert-me.ini",
    "/etc/alert-me/alert-me.conf",
    "/etc/alert-me/alert-me.ini",
]

# Installed plugins
_plugins: dict[str, Plugin] = {
    TelegramPlugin.name: TelegramPlugin,
    UrlPlugin.name: UrlPlugin,
    EmailPlugin.name: EmailPlugin,
}


def register_plugin(self, plugin: Plugin) -> None:
    """
    Register a plugin

    Args:
        plugin (Plugin): The plugin to register
    """
    if plugin.name in _plugins:
        raise Exception(f"Plugin with name '{plugin.name}' is already registered")
    _plugins[plugin.name] = plugin


def get_config(config_name: str) -> Plugin:
    """
    Fetch a plugin from the config file

    Args:
        config_name (str): The name of the config

    Returns:
        Plugin: The initialised plugin
    """
    config_path = None
    for path in CONFIG_FILE:
        if os.path.exists(os.path.expanduser(path)):
            config_path = os.path.expanduser(path)
            break
    if config_path is None:
        raise Exception(
            f"alert-me config file not found in any of these locations: {CONFIG_FILE}"
        )

    logging.debug(f"Reading config from '{config_path}'. Installed plugins: {_plugins}")

    parser = ConfigParser()
    parser.read(config_path)

    logging.debug(f"ConfigParser sections: {parser.sections()}")

    if config_name not in parser:
        raise Exception(f"Config {config_name} not found")
    section = parser[config_name]
    plugin_name = section["plugin"]
    if plugin_name not in _plugins:
        raise Exception(f"Plugin {plugin_name} not found")
    plugin_class = _plugins[plugin_name]
    plugin_params = {}
    for param in section:
        if param == "plugin" or param == "default":
            continue
        if param not in plugin_class.required_init_params:
            raise Exception(f"Unknown param {param} in config {config_name}")

        # Convert the string value to the required type
        plugin_params[param] = plugin_class.required_init_params[param](section[param])

    plugin = plugin_class(plugin_params)

    return plugin


def get_plugin(plugin_name: str) -> Plugin:
    """
    Get a plugin by name

    Args:
        plugin_name (str): The name of the plugin

    Returns:
        Plugin: uninitialised plugin
    """
    if plugin_name not in _plugins:
        raise Exception(f"Plugin {plugin_name} not found")
    return _plugins[plugin_name]
