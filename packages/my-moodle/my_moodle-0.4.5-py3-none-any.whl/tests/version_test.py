"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Test cases for the project.
"""

import unittest
from my_moodle import __version__


class TestVersion(unittest.TestCase):
    """Test case for version"""

    def test_version(self) -> None:
        """Test the version of the package"""
        expected_version: str = "0.4.5"  # Update this value when the version changes
        self.assertEqual(
            __version__,
            expected_version,
            f"Expected version: {expected_version}, Actual version: {__version__}",
        )


if __name__ == "__main__":
    unittest.main()
