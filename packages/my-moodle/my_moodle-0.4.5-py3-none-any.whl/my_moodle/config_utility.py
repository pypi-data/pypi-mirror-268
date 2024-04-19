"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Config utility module
"""

from configparser import ConfigParser
from os import makedirs
from os.path import exists
from pathlib import Path


DEFAULT_CONFIG_FILE_PATH: str = "config.ini"
MESSAGE = "Config file not found. Please provide Moodle server URL and access token."


def check_and_read_config(config_filepath: str = "config.ini") -> tuple[str, str, str]:
    """Check if the config file exists. If not, create it and
    then read and return the server and token config.

    Args:
        config_filepath (str): The config file path

    Returns:
        tuple[str, str, str]: A tuple containing the program name, server and token
    """
    if not exists(config_filepath):
        print(MESSAGE)

        config_parser: ConfigParser = build_config_from_input()
        create_config_file(config_filepath, config_parser)

    return read_config(read_config_file(config_filepath))


def build_config_from_input() -> ConfigParser:
    """Build config file
    Args:
        file_path (str): The file path to create the config file
    """

    course_name: str = input("Enter your course name: ")
    server = input("Enter the Moodle server URL: ")
    print("To get your 'Moodle mobile web service' key, visit")
    print(f"{server}/user/managetoken.php")
    token = input("Enter the 'Moodle mobile web service' key: ")

    config = ConfigParser()
    config["User"] = {"program": course_name, "server": server, "token": token}

    return config


def create_config_file(file_path: str, config_parser: ConfigParser) -> None:
    """Create a config file

    Args:
        file_path (str): The file path to create the config file
    """

    path = Path(file_path)
    if not path.parent.exists():
        makedirs(path.parent)

    with open(file_path, "w", encoding="utf-8") as config_file:
        config_parser.write(config_file)


def read_config_file(file_path: str) -> ConfigParser:
    """Read the config file

    Args:
        file_path (str): The file path to read the config file

    Returns:
        ConfigParser: The config parser
    """
    config_parser: ConfigParser = ConfigParser()
    config_parser.read(file_path)
    return config_parser


def read_config(config_parser: ConfigParser) -> tuple[str, str, str]:
    """Read the config

    Args:
        config_parser (ConfigParser): The config parser

    Returns:
        tuple[str, str, str]: A tuple containing the course_name, the server and the token
    """
    program_name: str = config_parser["User"]["program"]
    server: str = config_parser["User"]["server"]
    token: str = config_parser["User"]["token"]
    return program_name, server, token
