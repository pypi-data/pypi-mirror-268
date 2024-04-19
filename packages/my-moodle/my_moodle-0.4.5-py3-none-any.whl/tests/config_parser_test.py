"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Test cases for the project.
"""

from configparser import ConfigParser
import os
import unittest

from pathlib import Path


class ConfigParserTest(unittest.TestCase):
    """Test case for Config Utility"""

    def test_create_config_file(self) -> None:
        """Test create_config_file method"""
        file_path: str = "tests/test-config.ini"

        config_parser = ConfigParser()
        config_parser["User"] = {
            "course": "Course Name",
            "server": "server.com",
            "token": "a9b775eeec1b4590b345976009c098b2",
        }

        path = Path(file_path)
        if not path.parent.exists():
            os.makedirs(path.parent)

        with open(file_path, "w", encoding="utf-8") as config_file:
            config_parser.write(config_file)

        # delete test file
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
