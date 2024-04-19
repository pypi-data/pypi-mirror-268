"""
Test cases for the project.
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

import unittest
from my_moodle.config_utility import check_and_read_config
from my_moodle.api import Api
from my_moodle.moodle_json_downloader import MoodleJsonDownloader


class MoodleJsonDownloaderTestSuite(unittest.TestCase):
    """Module for testing the MoodleJsonDownloader class."""

    def test_download_program(self) -> None:
        """Test the MoodleJsonDownloader.download_program function."""
        moodle_json_downloader = self.__build_sut()
        moodle_json_downloader.download_program()

    def test_download_my_data(self) -> None:
        """Test the MoodleJsonDownloader.download_my_data function."""
        moodle_json_downloader = self.__build_sut()
        moodle_json_downloader.download_my_data()

    def __build_sut(self) -> MoodleJsonDownloader:
        """Generate a MoodleJsonDownloader object for testing.

        Returns:
            MoodleJsonDownloader: The MoodleJsonDownloader object
        """
        directory: str = "tests"
        test_config_file: str = f"{directory}/config-b-s.ini"
        program_name, server, token = check_and_read_config(test_config_file)
        api = Api(server, token)
        return MoodleJsonDownloader(program_name, api, True)


if __name__ == "__main__":
    unittest.main()
