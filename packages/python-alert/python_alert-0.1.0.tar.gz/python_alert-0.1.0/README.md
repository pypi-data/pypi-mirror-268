# alert-me

Multi-Platform Python tool to send notifications to your devices. alert-me allows you to send notifications to your devices using different services.

## 📝 Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Config](#config)
- [Command line arguments](#command-line-arguments)
- [License](#license)

## 📕 About <a name="about"></a>

alert-me is a multi-platform Python tool to send notifications to your devices. It supports different plugins to send notifications via different services.

Available plugins:

- Email
- Telegram
- Url

Creating additional plugins is easy. Just create a new class that inherits from `Plugin` and implements the `notify` method.

## ⚙️ Installation <a name="installation"></a>

## Python repository

The easiest way to get alert-me is through the pypi.org repository. Install it by running the following command:

```bash
pip install python-alert
```

## Building from source

To install alert-me from source, clone this repository and run `pip install .` as follows:

```bash
git clone https://github.com/NeverMendel/alert-me.git
cd alert-me
pip install .
```

## 📖 Usage <a name="usage"></a>

### Command line

alert-me can be used from the command line by invoking the `alert-me` command. It accepts a number of [arguments](#command-line-arguments) to configure the alert.

```bash
alert-me -p telegram <TOKEN> <CHAT_ID> "Hello!"

alert-me -c telegram "Hello!"
alert-me -c email to_email@example.com "subject" "body"
```

### Python

alert-me can be used as a Python module by importing `AlertMe`.

```python
from alert_me.alert_me import AlertMe
from alert_me.plugins.telegram import TelegramPlugin
from alert_me.config import get_config

alert_me = AlertMe([TelegramPlugin("<TOKEN>", "<CHAT_ID>")])
alert_me.notify("Hello!")

alert_me = AlertMe([get_config("email")])
alert_me.notify("to_email@example.com", "subject", "body")
```

## Config

alert-me can be used to fetch the configuration from a file. The file must be in the [INI format](https://en.wikipedia.org/wiki/INI_file) and be located in the user home directory (`~/.alert-me.ini`).

Here is an example of a configuration file:

```ini
[telegram]
plugin = telegram
token = <TOKEN>
chat_id = <CHAT_ID>

[email]
plugin = email
smtp_server = <SMTP_SERVER>
smtp_port = <SMTP_PORT>
sender_email = <SENDER_EMAIL>
sender_password = <SENDER_PASSWORD>
```

## Command line arguments

```
usage: alert-me [-h] (-c CONFIG_UNPROCESSED | -p PLUGIN) [-v] [-vv] [-V] ...

Multi-Platform Python tool to send notifications to your devices

positional arguments:
  args                  Plugin and/or notify arguments

options:
  -h, --help            show this help message and exit
  -c CONFIG_UNPROCESSED, --config CONFIG_UNPROCESSED
                        Configuration name
                        syntax: --config=[config_name1],[config_name2],...
                        example: --config=telegram,email
  -p PLUGIN, --plugin PLUGIN
                        Plugin name
  -v, --verbose         enable verbose logging
  -vv, --extra-verbose  enable extra verbose logging
  -V, --version         show program's version number and exit
```

## License

[MIT License](LICENSE)