"""
Test cases for the project.
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

from os import getcwd
import unittest
from my_moodle.config_utility import check_and_read_config
from my_moodle.json_utility import load_json_from_file
from my_moodle.moodle_data_downloader import MoodleDataDownloader


class MoodleDataDownloaderTestSuite(unittest.TestCase):
    """Module for testing the MoodleDataDownloader class."""

    def test_download_program_courses_contents(self) -> None:
        """Test the check_and_read_config function."""
        moodle_data_downloader: MoodleDataDownloader = self.__build_sut()
        test_file = moodle_data_downloader.json_downloader.program_filepath
        courses = load_json_from_file(test_file)
        moodle_data_downloader.download_program_courses_contents(courses)

    def test_download_my_data(self) -> None:
        """Test the MoodleDataDownloader.download_my_data function."""
        moodle_data_downloader: MoodleDataDownloader = self.__build_sut()
        moodle_data_downloader.download_my_data()

    def __build_sut(self) -> MoodleDataDownloader:
        """Generate a MoodleDataDownloader object for testing.

        Returns:
            MoodleDataDownloader: The MoodleDataDownloader object
        """
        #data_dir: str = "data"
        test_config_file: str = "tests/config-a-s.ini"
        program_name, server, token = check_and_read_config(test_config_file)
        return MoodleDataDownloader(program_name, server, token, getcwd(), True)


if __name__ == "__main__":
    unittest.main()
