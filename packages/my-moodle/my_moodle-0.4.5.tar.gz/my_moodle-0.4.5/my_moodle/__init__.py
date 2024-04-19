"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Moodle data downloader package.
"""

from . import api_functions as ApiFunctions
from . import config_utility as ConfigUtility
from . import csv_utility as CsvUtility
from . import data_utility as DataUtility
from . import json_utility as JsonUtility
from . import markdown_methods
from . import notebook_utility as NotebookUtility
from .api import Api
from .course_markdown_builder import CourseMarkdownBuilder
from .course_status import CourseStatus
from .enrolled_users_fields import EnrolledUsersFields
from .markdown_document import MarkdownDocument
from .moodle_data_downloader import MoodleDataDownloader
from .moodle_json_downloader import MoodleJsonDownloader
from .program_markdown_builder import ProgramMarkdownBuilder
from .update_utility import update_my_moodle_template
from .version import __version__
from .wrapper import Course, MoodleFile
from .__main__ import main

__all__ = [
    "Api",
    "ApiFunctions",
    "ConfigUtility",
    "Course",
    "CourseMarkdownBuilder",
    "CourseStatus",
    "CsvUtility",
    "DataUtility",
    "EnrolledUsersFields",
    "JsonUtility",
    "main",
    "markdown_methods",
    "MarkdownDocument",
    "MoodleDataDownloader",
    "MoodleFile",
    "MoodleJsonDownloader",
    "NotebookUtility",
    "ProgramMarkdownBuilder",
    "update_my_moodle_template",
    "__version__",
]
