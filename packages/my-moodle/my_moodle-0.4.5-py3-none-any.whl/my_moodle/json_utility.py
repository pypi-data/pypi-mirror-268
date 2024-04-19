"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Json utility Methods
"""

from json import dumps, load
import logging


def load_json_from_file(file_path: str, encoding: str = "utf-8") -> dict:
    """Load JSON from file

    Args:
        file_path (str): The file path

    Returns:
        dict: The JSON data
    """
    with open(file_path, "r", encoding=encoding) as json_file:
        return load(json_file)


def load_json_list_from_file(file_path: str, encoding: str = "utf-8") -> list[dict]:
    """Load JSON from file

    Args:
        file_path (str): The file path

    Returns:
        dict: The JSON data
    """
    with open(file_path, "r", encoding=encoding) as json_file:
        return load(json_file)


def save_json_to_file(
    json_data: dict | list[dict],
    file_path: str,
    indent: int = 2,
    encoding: str = "utf-8",
) -> None:
    """Save JSON to file

    Args:
        json_dict (list[dict]): The JSON data
        file_path (str): The file path
    """
    with open(file_path, "w", encoding=encoding) as json_file:
        json_file.write(dumps(json_data, indent=indent))
    logging.info("JSON data saved to %s", file_path)
