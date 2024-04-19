"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Resource utility
"""

from enum import Enum
from os.path import dirname, join
from my_moodle.json_utility import load_json_from_file


def get_package_recourses(resource_filename: str = "resource.json") -> dict:
    """Get the package recourses

    Returns:
        dict: This package's recourses

    """
    return load_json_from_file(join(dirname(__file__), resource_filename))


class PackageKeys(Enum):
    """Package keys"""

    BINDER_URL = "binder-url"
    COLAB_URL = "colab-url"
    HTML_COMMENT = "html-comment"
    OPEN_WITH_TABLE = "open-with-table"
    TEMPLATE_MESSAGE = "template-message"


class PackageResources:
    """Package resources"""

    def __init__(self) -> None:
        """Initialise the PackageResources object"""
        self._resources = get_package_recourses()

    def __get(self, key: PackageKeys) -> str:
        """Get a resource

        Args:
            key (PackageKeys): The key as an enum value

        Returns:
            str: The resource
        """
        return self._resources[key.value]

    @property
    def binder_url(self) -> str:
        """Get the binder URL

        Returns:
            str: The binder URL
        """
        return self.__get(PackageKeys.BINDER_URL)

    @property
    def colab_url(self) -> str:
        """Get the colab URL

        Returns:
            str: The colab URL
        """
        return self.__get(PackageKeys.COLAB_URL)

    @property
    def html_comment(self) -> str:
        """Get the HTML comment

        Returns:
            str: The HTML comment
        """
        return self.__get(PackageKeys.HTML_COMMENT)

    @property
    def open_with_table(self) -> str:
        """Get the open with table

        Returns:
            dict: The open with table
        """
        return self.__get(PackageKeys.OPEN_WITH_TABLE)

    @property
    def template_message(self) -> str:
        """Get the template message

        Returns:
            str: The template message
        """
        return self.__get(PackageKeys.TEMPLATE_MESSAGE)
