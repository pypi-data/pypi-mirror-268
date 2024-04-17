import argparse
import logging

from alert_me._version import __version__
from alert_me.config import get_config, get_plugin
from alert_me.alert_me import AlertMe
from alert_me.plugin import array_to_dict


def parse_args():
    parser = argparse.ArgumentParser(
        description="Multi-Platform Python tool to send notifications to your devices",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(
            "alert-me", width=80
        ),
    )
    plugin_group = parser.add_mutually_exclusive_group(required=True)

    plugin_group.add_argument(
        "-c",
        "--config",
        type=str,
        help="configuration name\n"
        "syntax: --config=[config_name]\n"
        "example: --config=telegram",
    )
    plugin_group.add_argument(
        "-p", "--plugin", dest="plugin", type=str, help="plugin name"
    )

    parser.add_argument(
        "args", nargs=argparse.REMAINDER, help="plugin and/or notify arguments"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="enable verbose logging",
    )
    parser.add_argument(
        "-vv",
        "--extra-verbose",
        dest="extra_verbose",
        action="store_true",
        help="enable extra verbose logging",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )

    return parser.parse_args()


def configure_logging(args):
    logging_stream_handler = logging.StreamHandler()

    # Set stream logging level based on program arguments
    logging_stream_handler.setLevel(logging.WARNING)
    if args.verbose:
        logging_stream_handler.setLevel(logging.INFO)
    if args.extra_verbose:
        logging_stream_handler.setLevel(logging.DEBUG)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
        handlers=[logging_stream_handler],
    )


def main():
    args = parse_args()
    configure_logging(args)

    logging.debug(f"alert-me {__version__} run with arguments: {args}")

    alert_me = None
    notify_params = args.args

    if "config" in args:
        # Load plugin from config file
        plugin = get_config(args.config)
        alert_me = AlertMe([plugin])
    else:
        # Initalize plugin with arguments
        plugin = get_plugin(args.plugin)
        init_params = args.args[: len(plugin.required_init_params)]
        notify_params = args.args[len(plugin.required_init_params) :]
        alert_me = AlertMe(
            [plugin(array_to_dict(init_params, plugin.required_init_params))]
        )

    alert_me.notify(array_to_dict(notify_params, plugin.required_notify_params))


if __name__ == "__main__":
    main()
