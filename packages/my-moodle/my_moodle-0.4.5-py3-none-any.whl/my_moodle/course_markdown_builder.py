"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
CourseMarkdownBuilder Class
"""

from html import unescape
from os import makedirs
from pathlib import Path

from my_moodle.wrapper import MoodleFile

from .data_utility import FileData, content_course_filename
from .markdown_document import MarkdownDocument
from .markdown_methods import MarkdownLink

_MOODLE_LINK_TEXT = "`moodle`"


class CourseMarkdownBuilder:
    """Course Markdown Builder"""

    def __init__(
        self,
        program_name: str,
        course_name: str,
        course_url: str,
        filename: str = "readme.md",
    ):
        """Initialise the CourseMarkdownBuilder

        Args:
            program_name (str): The program name
            course_name (str): The course name
            course_url (str): The course URL
        """
        self._markdown_document = MarkdownDocument()
        """Markdown document"""
        self._course_name = course_name
        """Course name"""
        self._course_url = course_url
        """Course URL"""
        self._filename = filename
        """Filename"""
        self._program_name = program_name
        """Program name"""
        self._files = []

    def __add_file(self, file_data: FileData) -> None:
        """Add a file to the list of files

        Args:
            file_data (FileData): The file data
        """
        self._files.append(file_data)

    def __str__(self) -> str:
        """Return the string representation of the CourseMarkdownBuilder

        Returns:
            str: The string representation of the CourseMarkdownBuilder
        """
        return str(self._markdown_document)

    def save_to_directory(self, directory_path: str, encoding: str = "utf-8") -> None:
        """Saves the markdown document to a directory

        Args:
            directory_path (str): The directory path
        """
        file_path: str = str(Path(directory_path, self._filename).absolute())

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

    def process_course_contents(self, course_contents: list[dict]) -> list[FileData]:
        """Process course contents

        Args:
            course_contents (dict): The course contents JSON
        """

        self._markdown_document.write_h1(
            str(MarkdownLink(self._program_name, "../readme.md", self._program_name))
        )
        self._markdown_document.write_h2(self._course_name)
        self._markdown_document.write_paragraph(f"Course URL: <{self._course_url}>")

        course_file_number = 1
        for course_content in course_contents:
            # Write module heading
            module_name = course_content.get("name", "")
            self._markdown_document.write_h3(module_name)

            if course_content.get("visible", 1) == 0:
                self._markdown_document.write_paragraph("*Not available.*")
                continue

            modules = course_content.get("modules", [])
            if not modules or len(modules) == 0:
                self._markdown_document.write_paragraph("*No content.*")
            else:
                course_file_number = self.process_modules(modules, course_file_number)
        self._markdown_document.write_hr()
        return self._files

    def process_modules(self, modules: list, course_file_number: int) -> int:
        """Process modules

        Args:
            modules (list): The modules json
            course_file_number (int): The course file number

        Returns:
            int: The number of files processed
        """
        for module in modules:
            mod_name = module.get("modname", "")

            module_contents = module.get("contents", [])

            is_link = len(module_contents) == 0

            module_is_heading = module_contents and len(module_contents) > 1

            if mod_name == "label":
                description: str = module.get("description", "")
                description: str = unescape(description)  # Unescape HTML entities
                self._markdown_document.write_line()
                self._markdown_document.write_paragraph(description.strip())
                continue

            content_name = module.get("name", "")
            moodle_content_url = module.get("url", "")

            if module_is_heading:
                if len(module_contents) < 5:
                    self._markdown_document.write_bullet_line(f"**{content_name}**")
                    course_file_number = self.process_module_folder_contents(
                        module_contents, course_file_number
                    )
                else:
                    local_uri = (
                        content_course_filename(course_file_number, content_name) + "/"
                    )
                    local_link = MarkdownLink(content_name, local_uri, content_name)
                    moodle_link = MarkdownLink(
                        _MOODLE_LINK_TEXT, moodle_content_url, content_name
                    )
                    self._markdown_document.write_bullet_line(
                        f"**{local_link}**: original at {moodle_link}"
                    )
                    file_url, file_size, file_created, file_modified = (
                        self.get_file_data(module_contents)
                    )
                    self.__add_file(
                        FileData(
                            course_file_number,
                            local_uri,
                            file_url,
                            file_size,
                            file_created,
                            file_modified,
                        )
                    )
                    course_file_number += 1

            else:
                if is_link:
                    moodle_link = MarkdownLink(
                        f"`{content_name}`", moodle_content_url, content_name
                    )
                    self._markdown_document.write_bullet_link_line(moodle_link)
                elif mod_name == "url":
                    url = self.get_local_uri(course_file_number, module_contents)

                    moodle_link = MarkdownLink(f"`{content_name}`", url, content_name)
                    self._markdown_document.write_bullet_link_line(moodle_link)
                    # TODO: Check course_file_number += 1
                else:
                    local_uri = self.get_local_uri(course_file_number, module_contents)
                    local_link = MarkdownLink(content_name, local_uri, content_name)
                    moodle_link = MarkdownLink(
                        _MOODLE_LINK_TEXT, moodle_content_url, content_name
                    )
                    self._markdown_document.write_bullet_line(
                        f"**{local_link}**: original at {moodle_link}"
                    )
                    file_url, file_size, file_created, file_modified = (
                        self.get_file_data(module_contents)
                    )
                    self.__add_file(
                        FileData(
                            course_file_number,
                            local_uri,
                            file_url,
                            file_size,
                            file_created,
                            file_modified,
                        )
                    )
                    course_file_number += 1
            self._markdown_document.write_line()
        return course_file_number

    def get_file_url(self, module_contents: list) -> str:
        """Get the file URL

        Args:
            module_contents (list): The module contents

        Returns:
            str: The file URL
        """
        for module_content in module_contents:
            moodle_file = MoodleFile(module_content)
            if moodle_file.is_file() and "fileurl" in module_content:
                return moodle_file.file_url
        return ""

    def get_file_data(self, module_contents: list) -> tuple[str, int, int, int]:
        """Get the file URL

        Args:
            module_contents (list): The module contents

        Returns:
            str: The file URL
        """
        for module_content in module_contents:
            moodle_file = MoodleFile(module_content)
            if moodle_file.is_file() and "fileurl" in module_content:
                return (
                    moodle_file.file_url,
                    moodle_file.file_size,
                    moodle_file.time_created,
                    moodle_file.time_modified,
                )
        return "", 0, 0, 0

    def process_module_folder_contents(
        self, module_contents: list, course_file_number: int
    ) -> int:
        """_summary_

        Args:
            module_contents (list): _description_
            course_file_number (int): _description_

        Returns:
            int: The number of files processed
        """
        for module_content in module_contents:
            moodle_file = MoodleFile(module_content)
            moodle_content_url = moodle_file.file_url
            content_name = moodle_file.file_name
            if moodle_file.is_file() and "fileurl" in module_content:
                local_uri = content_course_filename(
                    course_file_number, moodle_file.file_name
                )
                local_link = MarkdownLink(content_name, local_uri, content_name)
                moodle_link = MarkdownLink(
                    _MOODLE_LINK_TEXT, moodle_content_url, content_name
                )
                self._markdown_document.write_bullet_line(
                    f"**{local_link}**: original at {moodle_link}", 1
                )
                file_url, file_size, file_created, file_modified = self.get_file_data(
                    module_contents
                )
                self.__add_file(
                    FileData(
                        course_file_number,
                        local_uri,
                        file_url,
                        file_size,
                        file_created,
                        file_modified,
                    )
                )
                course_file_number += 1
            elif moodle_file.is_url():
                moodle_link = MarkdownLink(
                    _MOODLE_LINK_TEXT, moodle_content_url, content_name
                )
                self._markdown_document.write_bullet_line(
                    f"**{local_link}**: original at {moodle_link}"
                )
                moodle_link = MarkdownLink(
                    content_name, moodle_content_url, content_name
                )
                self._markdown_document.write_bullet_link_line(moodle_link, 1)
        return course_file_number

    def get_local_uri(self, course_file_number: int, module_contents: list) -> str:
        """Get the local URI

        Args:
            course_file_number (int): The course file number
            module_contents (list): The module contents

        Returns:
            str: The local URI
        """
        local_uri = ""
        for module_content in module_contents:
            moodle_file = MoodleFile(module_content)
            if moodle_file.is_file() and "fileurl" in module_content:
                local_uri = content_course_filename(
                    course_file_number, moodle_file.file_name
                )
            elif moodle_file.is_url():
                local_uri = module_content["fileurl"]
        return local_uri
