"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Entry point for the application.
"""

from .version import __version__


def main() -> None:
    """Entry point for the application."""
    print(f"my_moodle version {__version__}")

if __name__ == "__main__":
    main()
