"""
Test cases for the project.
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

import unittest
from pathlib import Path
from my_moodle.api import Api
from my_moodle.config_utility import check_and_read_config
from my_moodle.data_utility import N_TUTORR
from my_moodle.json_utility import load_json_from_file, save_json_to_file
from my_moodle.project_structure import (
    get_assignments_filename,
    get_submissions_filename,
)


class ApiTestSuite(unittest.TestCase):
    """Module for testing the MoodleDataDownloader class."""

    def test_get_course_assignments(self) -> None:
        """Test get_course_assignments."""

        return
        test_config_file = "tests/config-n-t.ini"
        _, server, token = check_and_read_config(test_config_file)
        api = Api(server, token)

        data_directory = "_data"
        test_file = "program-software-development-courses.json"
        test_file_path = str(Path(data_directory, test_file).absolute())
        courses_json = load_json_from_file(test_file_path).get("courses", [])

        for course in courses_json:
            if course.get("coursecategory") == N_TUTORR:
                continue

            assignment = api.get_course_assignments(course.get("id"))
            print(assignment)
            course_name = course.get("fullname")
            save_json_to_file(
                assignment, f"{data_directory}/{get_assignments_filename(course_name)}"
            )

    def test_get_assignment_submissions(self) -> None:
        """Test get_assignment_submissions."""

        test_config_file = "tests/config-n-t.ini"
        _, server, token = check_and_read_config(test_config_file)
        api = Api(server, token)

        data_directory = "_data"
        test_file = "program-software-development-courses.json"
        test_file_path = str(Path(data_directory, test_file).absolute())
        courses_json = load_json_from_file(test_file_path).get("courses", [])

        for course in courses_json:
            if course.get("coursecategory") == N_TUTORR:
                continue

            course_name = course.get("fullname")
            course_assignments = api.get_course_assignments(course.get("id"))
            assignments = course_assignments.get("courses", [])[0].get(
                "assignments", []
            )
            for assignment in assignments:
                assignment_id = str(assignment.get("id"))
                submissions = api.get_assignment_submissions(assignment_id)
                print(submissions)
                save_json_to_file(
                    submissions,
                    f"{data_directory}/{get_submissions_filename(course_name, assignment_id)}",
                )


if __name__ == "__main__":
    unittest.main()
