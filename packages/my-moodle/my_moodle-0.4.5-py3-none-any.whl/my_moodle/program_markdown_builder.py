"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
ProgramMarkdownBuilder Class
"""

import logging
from os import makedirs
from pathlib import Path

from .resource_utility import PackageResources
from .data_utility import N_TUTORR, group_courses_by_category
from .markdown_document import MarkdownDocument
from .markdown_methods import MarkdownLink
from .project_structure import course_directory, clean_course_name


class ProgramMarkdownBuilder:
    """Program Markdown Builder"""

    def __init__(self, program_name: str, filename: str = "readme.md"):
        """Initialise the CourseMarkdownBuilder

        Args:
            program_name (str): The program name
            course_name (str): The course name
            course_url (str): The course URL
        """
        self._markdown_document = MarkdownDocument()
        """Markdown document"""
        self._filename = filename
        """Filename"""
        self._program_name = program_name
        """Program name"""

    def __str__(self) -> str:
        """Return the string representation of the CourseMarkdownBuilder

        Returns:
            str: The string representation of the CourseMarkdownBuilder
        """
        return str(self._markdown_document)

    def add_program(self, program_name: str) -> None:
        """Add a program

        Args:
            program_name (str): The program name
        """
        self._markdown_document.write_h1(program_name)

    def add_category(self, category_name: str) -> None:
        """Add a category

        Args:
            category_name (str): The category name
        """
        self._markdown_document.write_h2(category_name)

    def add_course(self, course_name: str, course_path: str) -> None:
        """Add a course

        Args:
            course_name (str): The course name
            course_path (str): The course path
        """
        self._markdown_document.write_bullet_link_line(
            MarkdownLink(course_name, f"{course_path}/readme.md", course_name)
        )

    def save_to_directory(self, directory_path: str, encoding: str = "utf-8") -> None:
        """Saves the markdown document to a directory

        Args:
            directory_path (str): The directory path
        """
        file_path = str(Path(directory_path, self._filename).absolute())
        if not Path(directory_path).exists():
            makedirs(directory_path, exist_ok=True)
        with open(file_path, "w", encoding=encoding) as file:
            file.write(str(self))

    def save_to_file(self, file_path: str, encoding: str = "utf-8") -> None:
        """Saves the markdown document to a file

        Args:
            file_path (str): The file path
        """
        with open(file_path, "w", encoding=encoding) as file:
            file.write(str(self))

    def add_template_notice(self) -> None:
        """Add the template notice"""

        package_recourses = PackageResources()

        link = "https://github.com/marcocrowe/my-moodle-template"
        instructions_link = "template-instructions.md"
        filled_message = package_recourses.template_message.format(
            link=link, instructions_link=instructions_link
        )

        self._markdown_document.write_paragraph(filled_message)
        self._markdown_document.write_hr()
        self._markdown_document.write_line()

    def process_courses_json(self, courses_json: list[dict]) -> None:
        """Process the courses json

        Args:
            courses_json (dict): The courses json.
        """

        self.add_program(self._program_name)
        self.add_template_notice()
        courses_by_category = group_courses_by_category(courses_json)
        for category, courses in courses_by_category.items():
            if category == N_TUTORR:
                logging.warning("Skipping category: %s", category)
                continue
            self.add_category(category)
            courses = sorted(courses, key=lambda x: x.get("fullname", ""))
            for course in courses:
                name = clean_course_name(course.get("fullname", ""))
                dir_path = course_directory(course)

                self.add_course(clean_course_name(name), dir_path)
            self._markdown_document.write_line()
        self._markdown_document.write_hr()
