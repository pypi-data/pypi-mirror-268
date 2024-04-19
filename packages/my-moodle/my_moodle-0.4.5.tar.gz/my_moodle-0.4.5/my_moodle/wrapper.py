"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Wrappers for JSON data from the Moodle API.
"""

from typing import Optional


class Course:
    """Course represents a course in Moodle."""

    def __init__(self, json_data: dict):
        """
        Initializes a Course object with the given JSON data.

        Args:
            json_data (dict): The JSON data representing the course.
        """
        self.__json_data = json_data

    @property
    def id(self) -> int:
        """
        Returns the ID of the course.

        Returns:
            int: The ID.
        """
        return self.__json_data["id"]

    @property
    def full_name(self) -> str:
        """
        Returns the full name of the course.

        Returns:
            str: The full name.
        """
        return self.__json_data["fullname"]

    @property
    def short_name(self) -> str:
        """
        Returns the short name of the course.

        Returns:
            str: The short name.
        """
        return self.__json_data["shortname"]

    @property
    def id_number(self) -> str:
        """
        Returns the ID number of the course.

        Returns:
            str: The ID number.
        """
        return self.__json_data["idnumber"]

    @property
    def summary(self) -> str:
        """
        Returns the summary of the course.

        Returns:
            str: The summary.
        """
        return self.__json_data["summary"]

    @property
    def summary_format(self) -> int:
        """
        Returns the summary format of the course.

        Returns:
            int: The summary format.
        """
        return self.__json_data["summaryformat"]

    @property
    def start_date(self) -> int:
        """
        Returns the start date of the course.

        Returns:
            int: The start date.
        """
        return self.__json_data["startdate"]

    @property
    def end_date(self) -> int:
        """
        Returns the end date of the course.

        Returns:
            int: The end date.
        """
        return self.__json_data["enddate"]

    @property
    def visible(self) -> bool:
        """
        Returns whether the course is visible or not.

        Returns:
            bool: True if the course is visible, False otherwise.
        """
        return self.__json_data["visible"]

    @property
    def show_activity_dates(self) -> bool:
        """
        Returns whether the course shows activity dates or not.

        Returns:
            bool: True if the course shows activity dates, False otherwise.
        """
        return self.__json_data["showactivitydates"]

    @property
    def show_completion_conditions(self) -> bool:
        """
        Returns whether the course shows completion conditions or not.

        Returns:
            bool: True if the course shows completion conditions, False otherwise.
        """
        return self.__json_data["showcompletionconditions"]

    @property
    def full_name_display(self) -> str:
        """
        Returns the full name display of the course.

        Returns:
            str: The full name display.
        """
        return self.__json_data["fullnamedisplay"]

    @property
    def view_url(self) -> str:
        """
        Returns the view URL of the course.

        Returns:
            str: The view URL.
        """
        return self.__json_data["viewurl"]

    @property
    def course_image(self) -> str:
        """
        Returns the course image of the course.

        Returns:
            str: The course image.
        """
        return self.__json_data["courseimage"]

    @property
    def progress(self) -> int:
        """
        Returns the progress of the course.

        Returns:
            int: The progress.
        """
        return self.__json_data["progress"]

    @property
    def has_progress(self) -> bool:
        """
        Returns whether the course has progress or not.

        Returns:
            bool: True if the course has progress, False otherwise.
        """
        return self.__json_data["hasprogress"]

    @property
    def is_favourite(self) -> bool:
        """
        Returns whether the course is a favourite or not.

        Returns:
            bool: True if the course is a favourite, False otherwise.
        """
        return self.__json_data["isfavourite"]

    @property
    def is_hidden(self) -> bool:
        """
        Returns whether the course is hidden or not.

        Returns:
            bool: True if the course is hidden, False otherwise.
        """
        return self.__json_data["hidden"]

    @property
    def show_short_name(self) -> bool:
        """
        Returns whether the course shows the short name or not.

        Returns:
            bool: True if the course shows the short name, False otherwise.
        """
        return self.__json_data["showshortname"]

    @property
    def course_category(self) -> str:
        """
        Returns the course category of the course.

        Returns:
            str: The course category.
        """
        return self.__json_data["coursecategory"]


class MoodleFile:
    """MoodleFile represents a file in Moodle."""

    def __init__(self, json_data: dict):
        """
        Initializes a MoodleFile object with the given JSON data.

        Args:
            json_data (dict): The JSON data representing the Moodle file.
        """
        self.__json_data = json_data

    @property
    def type(self) -> str:
        """
        Returns the type of the Moodle file.

        Returns:
            str: The filename.
        """
        return self.__json_data["type"]

    @property
    def file_name(self) -> str:
        """
        Returns the filename of the Moodle file.

        Returns:
            str: The filename.
        """
        return self.__json_data["filename"]

    @property
    def file_path(self) -> str:
        """
        Returns the filepath of the Moodle file.

        Returns:
            str: The filepath.
        """
        return self.__json_data["filepath"]

    @property
    def file_size(self) -> int:
        """
        Returns the filesize of the Moodle file.

        Returns:
            int: The filesize.
        """
        return self.__json_data["filesize"]

    @property
    def file_url(self) -> str:
        """
        Returns the file URL of the Moodle file.

        Returns:
            str: The file URL.
        """
        return self.__json_data["fileurl"]

    @property
    def time_created(self) -> int:
        """
        Returns the time created of the Moodle file.

        Returns:
            int: The time created.
        """
        return self.__json_data["timecreated"]

    @property
    def time_modified(self) -> int:
        """
        Returns the time modified of the Moodle file.

        Returns:
            int: The time modified.
        """
        return self.__json_data["timemodified"]

    @property
    def mime_type(self) -> str:
        """
        Returns the mimetype of the Moodle file.

        Returns:
            str: The mimetype.
        """
        return self.__json_data["mimetype"]

    @property
    def is_external_file(self) -> bool:
        """
        Returns whether the file is external or not.

        Returns:
            bool: True if the file is external, False otherwise.
        """
        return self.__json_data["isexternalfile"]

    @property
    def author(self) -> Optional[str]:
        """
        Returns the author of the Moodle file if available.

        Returns:
            Optional[str]: The author or None if not available.
        """
        return self.__json_data.get("author")

    @property
    def license(self) -> Optional[str]:
        """
        Returns the license of the Moodle file if available.

        Returns:
            Optional[str]: The license or None if not available.
        """
        return self.__json_data.get("license")

    def is_file(self) -> bool:
        """Is the Moodle file a file?

        Returns:
            bool: True if the Moodle file is a file, False otherwise.
        """
        return self.type == "file"

    def is_url(self) -> bool:
        """Is the Moodle file a URL?

        Returns:
            bool: True if the Moodle file is a URL, False otherwise.
        """
        return self.type == "url"

    def create_local_filename(self) -> str:
        """Create a local filename

        Returns:
            str: The local filename
        """
        return self.file_name
