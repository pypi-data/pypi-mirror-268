"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Moodle data downloader Class
"""

import logging
from os import makedirs, utime
from pathlib import Path
from requests import get, RequestException
from .api import Api
from .course_markdown_builder import CourseMarkdownBuilder
from .data_utility import N_TUTORR, FileData, get_courses_favoured, is_file_a_copy
from .json_utility import load_json_from_file, load_json_list_from_file
from .moodle_json_downloader import MoodleJsonDownloader
from .program_markdown_builder import ProgramMarkdownBuilder
from .project_structure import clean_course_name, course_directory
from .version import __version__


class MoodleDataDownloader:
    """Moodle data downloader"""

    def __init__(
        self,
        program_name: str,
        server: str,
        token: str,
        data_dir: str = "",
        enable_enrollment_download: bool = False,
        timeout: float = 300.0,
        rest_format: str = "json",
    ):
        self.program_name = program_name
        """College program name"""
        self._api = Api(server, token, rest_format, timeout)
        """API for Moodle"""
        dir_p = f"{data_dir}/_data" if not data_dir else "_data"
        """Data directory path"""
        self._json_downloader = MoodleJsonDownloader(
            program_name, self._api, enable_enrollment_download, dir_p
        )
        """Enable enrollment download flag"""
        self.data_dir = data_dir
        """Data directory"""

    @property
    def api(self) -> Api:
        """API for Moodle

        Returns:Api
            Api: The API for Moodle
        """
        return self._api

    @property
    def json_downloader(self) -> MoodleJsonDownloader:
        """Moodle JSON downloader

        Returns:
            MoodleJsonDownloader: The Moodle JSON downloader
        """
        return self._json_downloader


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

    def build_markdown_files(self) -> None:
        """Build markdown files"""
        program = load_json_from_file(self._json_downloader.program_filepath)
        self.build_program_markdown_files(program.get("courses", []))

    def build_program_markdown_files(self, courses: list[dict]) -> None:
        """Build markdown files

        Args:
            courses (list): The courses
        """
        program_builder = ProgramMarkdownBuilder(self.program_name)
        program_builder.process_courses_json(courses)
        program_builder.save_to_directory(self.data_dir)

        for course in courses:
            if course.get("coursecategory") == N_TUTORR:
                continue

            course_name: str = clean_course_name(course.get("fullname", ""))
            directory_path: str = self.create_directory(course_directory(course))
            course_url: str = course.get("viewurl", "")

            course_markdown_builder = CourseMarkdownBuilder(
                self.program_name, course_name, course_url
            )
            path = self._json_downloader.get_course_content_filepath(course_name)

            course_contents = load_json_list_from_file(path)
            course_markdown_builder.process_course_contents(course_contents)
            course_markdown_builder.save_to_directory(directory_path)

    @staticmethod
    def display_version() -> None:
        """Display the version"""
        print(f"Using my_moodle Version: {__version__}")

    def download_my_json_data(self) -> list[dict]:
        """Download my JSON data

        Returns:
            dict: A list of JSON courses
        """
        return self._json_downloader.download_my_data().get("courses", [])

    def download_my_data(self) -> dict:
        """Download my data

        Returns:
            dict: The program JSON
        """
        program = self._json_downloader.download_my_data()
        self.build_program_markdown_files(program.get("courses", []))
        self.download_courses_contents(program.get("courses", []))
        return program

    def download_program_courses_contents(self, college_program: dict) -> None:
        """Download courses contents

        Args:
            college_program (dict): The college program
        """
        self.download_courses_contents(college_program.get("courses", []))

    def download_courses_contents(self, courses: list) -> None:
        """Download courses contents

        Args:
            courses (list): The courses
        """
        for course in courses:
            if course.get("coursecategory") == N_TUTORR:
                continue
            course_name: str = clean_course_name(course.get("fullname", ""))
            directory_path: str = self.create_directory(course_directory(course))

            self.download_course_contents(directory_path, course_name)

    def download_course_contents(self, directory_path: str, course_name: str) -> None:
        """Download all files from a course

        Args:
            course_id (str): The course id
            directory_path (str): The directory path
        """
        course_contents = load_json_list_from_file(
            self._json_downloader.get_course_content_filepath(course_name)
        )
        course_markdown_builder = CourseMarkdownBuilder(
            self.program_name, course_name, ""
        )
        files = course_markdown_builder.process_course_contents(course_contents)
        self.download_files(directory_path, files)

    def download_files(self, directory_path: str, files: list[FileData]) -> None:
        """Download files to a directory

        Args:
            directory_path (str): The directory path
            files (list): The files
        """
        for file in files:
            logging.info("Filename: %s , URL: %s", file.name, file.url)
            file_path = str(Path(directory_path, file.name).absolute())

            if is_file_a_copy(file, file_path):
                logging.info("File already exists: %s", file_path)
                continue

            file_url: str = file.get_download_url(self.api.token)
            self.download_file(
                file_url,
                file_path,
                file.date_created,
                file.date_modified,
                self.api.timeout,
            )

    @staticmethod
    def download_file(
        file_url: str,
        save_path: str,
        date_created: int,
        date_modified: int,
        timeout: float,
    ) -> None:
        """Download a file from Moodle"""
        try:
            response = get(file_url, stream=True, timeout=timeout)
            response.raise_for_status()

            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)

                MoodleDataDownloader.set_file_timestamps(
                    save_path, date_created, date_modified
                )
                logging.info("Saved to: %s", save_path)
            else:
                logging.warning("Download refused: %s", response.status_code)
        except RequestException as e:
            logging.error("Failed to download file: %s\n", str(e))

    @staticmethod
    def set_file_timestamps(save_path: str, date_created: int, date_modified: int):
        """Set the file timestamps

        Args:
            save_path (str): The file path
            date_created (int): The date created
            date_modified (int): The date modified
        """
        if date_modified:
            if date_created:
                utime(save_path, (date_created, date_modified))
            else:
                utime(save_path, (date_modified, date_modified))

    def download_favorite_courses_contents(self) -> None:
        """Download favorite courses

        Returns:
            list: The favorite courses data
        """
        program = load_json_from_file(self._json_downloader.program_filepath)
        favorite_courses_data: list = get_courses_favoured(program.get("courses", []))
        self.download_courses_contents(favorite_courses_data)
