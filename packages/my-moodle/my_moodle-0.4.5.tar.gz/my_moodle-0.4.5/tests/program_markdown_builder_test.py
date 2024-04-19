"""
Test cases for the project.
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

from pathlib import Path
import unittest
from my_moodle import ProgramMarkdownBuilder
from my_moodle.json_utility import load_json_from_file


class ProgramBuilderTestSuite(unittest.TestCase):
    """Module for testing the MoodleDataDownloader class."""

    def test_program_builder(self) -> None:
        """Test the ProgramMarkdownBuilder class."""

        program_name = "Business with Computing"
        directory = "_data"
        test_file = "program-business-with-computing-courses.json"
        test_file_path = str(Path(directory, test_file).absolute())

        courses_json = load_json_from_file(test_file_path)
        program_builder = ProgramMarkdownBuilder(program_name)
        program_builder.process_courses_json(courses_json.get("courses", []))

        program_builder.save_to_directory("")


if __name__ == "__main__":
    unittest.main()
