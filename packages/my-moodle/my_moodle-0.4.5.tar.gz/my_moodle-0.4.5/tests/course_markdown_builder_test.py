"""
Test cases for the project.
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

import unittest
from pathlib import Path
from my_moodle import CourseMarkdownBuilder
from my_moodle.data_utility import N_TUTORR
from my_moodle.json_utility import load_json_from_file, load_json_list_from_file
from my_moodle.project_structure import (
    clean_course_name,
    course_contents_filename,
    course_directory,
)


class CourseMarkdownBuilderTestSuite(unittest.TestCase):
    """Module for testing the MoodleDataDownloader class."""

    def test_course_builder(self) -> None:
        """Test the CourseMarkdownBuilder class."""

        directory = ""
        data_directory = "_data"
        test_file = "program-business-with-computing-courses.json"
        test_file_path = str(Path(data_directory, test_file).absolute())
        courses_json = load_json_from_file(test_file_path).get("courses", [])
        program_name = "Business with Computing"

        for course in courses_json:
            if course.get("coursecategory") == N_TUTORR:
                continue

            self.__process_course(directory, data_directory, program_name, course)

    def __process_course(self, directory, data_directory, program_name, course):
        course_name: str = clean_course_name(course.get("fullname", ""))
        course_dir = course_directory(course)
        directory_path = str(Path(directory, course_dir).absolute())
        course_url: str = course.get("viewurl", "")

        course_markdown_builder = CourseMarkdownBuilder(
            program_name, course_name, course_url
        )

        course_file_name = course_contents_filename(course_name)
        course_contents_file = str(Path(data_directory, course_file_name).absolute())

        courses_contents = load_json_list_from_file(course_contents_file)
        course_markdown_builder.process_course_contents(courses_contents)
        course_markdown_builder.save_to_directory(directory_path)


if __name__ == "__main__":
    unittest.main()
