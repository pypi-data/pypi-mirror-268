"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Test cases for the packages of the project
"""

import unittest
from importlib.metadata import Distribution, distribution, PackageNotFoundError


class TestPackage(unittest.TestCase):
    """
    Test case for the package.
    """

    @staticmethod
    def is_package_installed(package_name: str) -> bool:
        """Test if the package is installed and
        prints the files in the distribution if it is installed.

        Args:
            package_name (str): The name of the package.

        Returns:
            bool: True if the package is installed, False otherwise.
        """
        try:
            package_distribution: Distribution = distribution(package_name)
            print(f"\nFiles in the '{package_name}' distribution:\n")
            for package_path in package_distribution.files: # type: ignore
                print(package_path)
            return True
        except PackageNotFoundError:
            print(f"The '{package_name}' distribution is not installed.")
            return False

    def test_package(self) -> None:
        """
        Test if the my-moodle module exists.
        """
        package_name: str = "my-moodle"

        is_package_installed: bool = self.is_package_installed(package_name)

        self.assertTrue(is_package_installed)


if __name__ == "__main__":
    unittest.main()
