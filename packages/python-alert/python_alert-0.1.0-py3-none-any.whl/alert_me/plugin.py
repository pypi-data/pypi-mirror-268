from abc import ABC, abstractmethod
from functools import singledispatchmethod
import logging
from typing import Any, Dict, List


class Plugin(ABC):
    name: str = ""
    required_init_params: dict["str", type] = {}
    required_notify_params: dict["str", type] = {}

    def __init__(self, init_params: Dict[str, Any]):
        """
        Initialize the plugin

        Args:
            init_params (dict[str, any]): The parameters to initialize the plugin with
        """
        if self.name.strip() == "":
            raise Exception("Plugin name cannot be empty")
        self.init_params = init_params
        check_params(self.required_init_params, self.init_params)

    @abstractmethod
    def notify(self, notify_params: dict[str, Any]) -> None:
        check_params(self.required_notify_params, notify_params)


def check_params(required_params: dict[str, type], params: dict[str, Any]) -> None:
    """
    Check that the required parameters are present and of the correct type

    Args:
        required_params (dict[str, type]): The required parameters
        params (dict[str, Any]): The parameters to check
    """
    for param_name, param_type in required_params.items():
        if param_name not in params:
            raise Exception(f"Missing required parameter {param_name}")
        if param_type != type(params[param_name]):
            raise Exception(
                f"Wrong type for parameter {param_name}. Expected {param_type}, got {type(params[param_name])}"
            )


def array_to_dict(array: [], expected_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Convert an array to a dict

    Args:
        array (list): The array to convert
        expected_dict (dict[str, Any]): The expected dict

    Returns:
        dict[str, Any]: The converted dict
    """
    if len(array) < len(expected_dict):
        logging.warning(
            f"Insufficient arguments. Expected {len(expected_dict)}, got {len(array)}"
        )
    if len(array) > len(expected_dict):
        logging.warning(
            f"Wrong number of arguments. Expected {len(expected_dict)}, got {len(array)}"
        )
    res: dict[str, Any] = {}
    param_names = list(expected_dict.keys())

    for i, arg in enumerate(array):
        if i >= len(param_names):
            break

        param_name = param_names[i]
        param_type = expected_dict[param_name]

        res[param_name] = arg

    check_params(expected_dict, res)

    return res
