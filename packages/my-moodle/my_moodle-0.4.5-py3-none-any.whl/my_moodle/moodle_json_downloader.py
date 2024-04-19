"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Moodle data downloader Class
"""

import logging
from os import makedirs
from pathlib import Path
from .api import Api
from .csv_utility import save_json_fields_list_to_csv
from .data_utility import N_TUTORR, preprocess_enrolled_users, process_courses
from .enrolled_users_fields import EnrolledUsersFields
from .json_utility import save_json_to_file
from .project_structure import (
    clean_course_name,
    course_contents_filename,
    get_enrolled_filename,
    make_slug,
)


class MoodleJsonDownloader:
    """Moodle data downloader"""

    def __init__(
        self,
        program_name: str,
        api: Api,
        enable_enrollment_download: bool = False,
        data_dir: str = "_data",
    ):
        """Constructor

        Args:
            program_name (str): The program name
            api (Api): The API for Moodle
            data_dir (str, optional): The data directory. Defaults to "_data".
        """
        self._api: Api = api
        """API for Moodle"""
        self.data_dir = data_dir
        """Data directory"""
        self._program_name = program_name
        """College program name"""
        self.__enable_enrollment_download = enable_enrollment_download
        """Enable enrollment download flag"""

        makedirs(self.data_dir, exist_ok=True)

    @property
    def api(self) -> Api:
        """API for Moodle

        Returns:
            Api: The API for Moodle
        """
        return self._api

    @property
    def __is_enrollment_download_enabled(self) -> bool:
        """Is enrollment download enabled

        Returns:
            bool: True if enrollment download is enabled
        """
        return self.__enable_enrollment_download

    def create_directory(self, directory: str) -> str:
        """Create a directory

        Args:
            directory (str): The directory to create

        Returns:
            str: The directory path
        """
        directory_path = Path(self.data_dir, directory)
        makedirs(directory_path, exist_ok=True)
        return str(directory_path.absolute())

    def download_my_data(self) -> dict:
        """Download my data

        Returns:
            dict: The courses json
        """
        program = self.download_program()
        self.download_courses(program)
        return program

    def download_program(self) -> dict:
        """Download program

        Returns:
            dict: The program json of the courses
        """
        program: dict = self.api.get_program_courses()
        path = self.program_filepath
        program = process_courses(program)
        save_json_to_file(process_courses(program), path)
        return program

    def download_courses(self, courses_json: dict):
        """Download courses

        Args:
            courses_json (dict): The courses json
        """

        for course_json in courses_json.get("courses", []):
            if course_json.get("coursecategory") == N_TUTORR:
                continue

            self.download_course_contents(course_json)
            # self.download_json_course_private_files(course_json)
            if self.__is_enrollment_download_enabled:
                self.download_students_by_course(course_json)

    def download_course_contents(self, course_json: dict) -> None:
        """Download course contents json
        Args:
            course_json (dict): The course json
        """
        course_id = course_json.get("id", "")
        name = clean_course_name(course_json.get("fullname", ""))
        self.download_course_contents_by_id(course_id, name)

    def download_course_contents_by_id(
        self, course_id: str, course_name: str
    ) -> list[dict]:
        """Download course contents json

        Args:
            course_id (str): The course id
            course_name (str): The course name
        """
        course_contents = self.api.get_course_contents(course_id)
        path = self.get_course_content_filepath(course_name)
        save_json_to_file(course_contents, path)
        return course_contents

    def download_students_by_course(self, course_json: dict) -> None:
        """Download enrolled students

        Args:
            course_json (dict): The course json
        """
        course_id = course_json.get("id", "")
        name = clean_course_name(course_json.get("fullname", ""))
        self.download_students_by_course_id(course_id, name)

    def download_students_by_course_id(self, course_id: str, course_name: str) -> None:
        """Download enrolled students

        Args:
            course_id (str): The course id
            filename (str): The filename
        """
        enrolled_users: list = self.api.get_course_enrolled_users(course_id)
        path = str(Path(self.data_dir, get_enrolled_filename(course_name)).absolute())
        save_json_to_file(enrolled_users, path)

        self.save_students_to_csv(enrolled_users, course_name)

    def save_students_to_csv(self, enrolled_users: list, name: str) -> None:
        """Save students to CSV

        Args:
            name (str): The course name
        """
        path = str(Path(self.data_dir, get_enrolled_filename(name, "csv")).absolute())

        enrolled_users1: list = preprocess_enrolled_users(enrolled_users)

        if not enrolled_users1:
            logging.warning("No enrolled users found.")
            return

        save_json_fields_list_to_csv(
            enrolled_users1, EnrolledUsersFields.get_field_order(), path
        )
        logging.info("Enrolled users saved to %s", path)

    def get_course_content_filepath(self, course_name: str) -> str:
        """Get the course content json filepath

        Args:
            course_name (str): The course name

        Returns:
            str: The course content json filepath
        """
        path = Path(self.data_dir, course_contents_filename(course_name))
        return str(path.absolute())

    @property
    def program_filepath(self) -> str:
        """Get the program filepath

        Returns:
            str: The program filepath
        """
        filename = f"program-{make_slug(self._program_name)}-courses.json"
        return str(Path(self.data_dir, filename).absolute())
