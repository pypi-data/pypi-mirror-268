"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Test cases for the project.
"""

import unittest
from my_moodle.project_structure import clean_course_slug


class MoodleDataUtilityTestSuite(unittest.TestCase):
    """Module for testing the MoodleDataUtility class."""

    def test_convert_to_slug(self) -> None:
        """Test the convert_to_slug function.

        This function reads test data from a CSV file, where each line contains a full name
        and its corresponding expected slug. It then compares the output of convert_to_slug
        with the expected slug for each full name.
        """

        test_file: str = "tests/slug-test-data.csv"

        full_names: list[str] = []
        expected: list[str] = []

        with open(test_file, encoding="utf-8") as file:
            for line in file:
                full_name, slug = line.split(",")
                full_names.append(full_name)
                expected.append(slug.strip())

        for index, full_name in enumerate(full_names):
            actual = clean_course_slug(full_name)
            self.assertEqual(actual, expected[index])


if __name__ == "__main__":
    unittest.main()
