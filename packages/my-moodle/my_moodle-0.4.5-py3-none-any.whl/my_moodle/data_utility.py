"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Moodle data utility Class
"""

from pathlib import Path
from time import time
from pandas import DataFrame
from IPython.core.display import HTML
from requests import get
from my_moodle.course_status import CourseStatus
from my_moodle.enrolled_users_fields import EnrolledUsersFields
from my_moodle.project_structure import content_course_filename

N_TUTORR = "N-TUTORR"


class FileData:
    """File Data"""

    def __init__(
        self,
        file_number: int,
        name: str,
        url: str,
        size,
        date_created: int = 0,
        date_modified: int = 0,
        folder="",
    ):
        self.file_number = file_number
        """Course file number"""
        self.name = name
        """Name"""
        self.url = url
        """URL"""
        self.size = size
        """File Size"""
        self.date_created = date_created
        """Date Created"""
        self.date_modified = date_modified
        """Date Modified"""
        self.folder = folder
        """Folder"""

    def get_file_name(self) -> str:
        """Get the file name

        Returns:
            str: The file name
        """
        return content_course_filename(self.file_number, self.name)

    def is_in_folder(self) -> bool:
        """Check if the file is in a folder

        Returns:
            bool: True if the file is in a folder, False otherwise
        """
        return bool(self.folder)

    def get_download_url(self, token: str) -> str:
        """Get the download URL for the file"""
        if self.url.find("?forcedownload=") == -1:
            return f"{self.url}&token={token}"

        return f"{self.url}?forcedownload=1&token={token}"


def is_file_a_copy(file: FileData, file_path: str) -> bool:
    """Check if the file is a copy

    Args:
        file (FileData): The file data
        file_path (str): The file path

    Returns:
        bool: True if the file is the same filename and size and date modified, False otherwise
    """
    try:
        if not Path(file_path).exists():
            return False

        stat = Path(file_path).stat()
        if stat.st_size != file.size:
            return False

        if file.date_modified is None:
            return False

        if stat.st_mtime != file.date_modified:
            return False

        return True

    except OSError:
        return False


def create_data_frame(
    courses: list,
    id_column: str = "id",
    fullname_column: str = "fullname",
    url_column: str = "viewurl",
) -> DataFrame:
    """Create a DataFrame from the courses list

    Args:
        courses (list): The list of courses
        id_column (str, optional): The column name for the course id. Defaults to "id".
        fullname_column (str, optional): The column name for the course fullname.
        Defaults to "fullname".
        url_column (str, optional): The column name for the course viewurl.
        Defaults to "viewurl".

    Returns:
        DataFrame: The DataFrame of courses
    """
    columns: list[str] = [id_column, fullname_column, url_column]
    courses_data_frame = DataFrame(courses, columns=columns)
    if courses == []:
        return courses_data_frame
    courses_data_frame = courses_data_frame[columns]
    return courses_data_frame


def create_data_frame_with_tiny_url(
    courses: list,
    id_column: str = "id",
    fullname_column: str = "fullname",
    url_column: str = "viewurl",
) -> DataFrame:
    """Create a DataFrame from the courses list with a tiny url column

    Args:
        courses (list): The list of courses
        id_column (str, optional): The column name for the course id. Defaults to "id".
        fullname_column (str, optional): The column name for the course fullname.
        Defaults to "fullname".
        url_column (str, optional): The column name for the course viewurl.
        Defaults to "viewurl".

    Returns:
        DataFrame: The DataFrame of courses
    """

    for course in courses:
        course["tiny-url"] = create_tiny_url(course[url_column])
    columns: list[str] = [id_column, fullname_column, "tiny-url"]

    courses_data_frame = DataFrame(courses, columns=columns)
    if courses == []:
        return courses_data_frame
    courses_data_frame = courses_data_frame[columns]
    return courses_data_frame


def create_tiny_url(url: str) -> str:
    """Shorten the URL using https://tinyurl.com

    Args:
        url (str): The URL to shorten

    Returns:
        str: The shortened URL
    """
    base_url = "http://tinyurl.com/api-create.php?url="
    response = get(base_url + url, timeout=5)
    short_url = response.text
    return short_url


def courses_json_to_html(courses: list) -> HTML:
    """Display the courses as an HTML table

    Args:
        courses (list): The list of courses

    Returns:
        HTML: The HTML table
    """
    return HTML(
        create_data_frame(courses).to_html(render_links=True, escape=False, index=False)
    )


def data_frame_to_html(courses_data_frame: DataFrame) -> HTML:
    """Display a DataFrame as an HTML table

    Args:
        courses_data_frame (DataFrame): The DataFrame of courses

    Returns:
        HTML: The HTML table
    """
    return HTML(
        courses_data_frame.to_html(render_links=True, escape=False, index=False)
    )


def get_courses_by_status(courses: list, status: CourseStatus) -> list:
    """Get courses by status.

    Args:
        courses (list): List of courses.
        status (CourseStatus): The status of the course to filter by.

    Returns:
        list: List of courses with the status.
    """
    return [course for course in courses if get_course_status(course) == status]


def get_courses_favoured(courses: list) -> list:
    """Get courses that are favoured.

    Args:
        courses (list): List of courses.

    Returns:
        list: List of favoured courses.
    """
    return [course for course in courses if course.get("isfavourite", False)]


def get_course_status(course: dict) -> CourseStatus:
    """Get the status of the course.

    Args:
        course (dict): Dictionary containing the course's details.

    Returns:
        str: The status of the course.
    """
    current_time = time()

    if current_time < course["startdate"]:
        return CourseStatus.UPCOMING
    elif course["startdate"] <= current_time <= course["enddate"]:
        return CourseStatus.ACTIVE

    return CourseStatus.PAST_FINISHED


def is_student(enrolled_user: dict) -> bool:
    """Check if the enrolled user is a student.

    Args:
        enrolled_user (dict): Dictionary containing the enrolled user's details.

    Returns:
        bool: True if the user is a student, False otherwise.
    """
    roles = enrolled_user.get(EnrolledUsersFields.ROLES, [])
    if roles:
        role_names = [role[EnrolledUsersFields.ROLE_SHORTNAME] for role in roles]
        return "student" in role_names
    return False


def preprocess_enrolled_users(enrolled_users: list) -> list:
    """Preprocess enrolled users data before saving to CSV.

    Args:
        enrolled_users (list): List of enrolled users' details.

    Returns:
        list: Preprocessed enrolled users data.
    """
    if not enrolled_users:
        return []

    preprocessed_users = []
    for user in enrolled_users:
        if is_student(user):

            # Remove unwanted fields
            preprocessed_user = {
                key: value
                for key, value in user.items()
                if key not in EnrolledUsersFields.get_unwanted_fields()
            }

            # Set profile image url to blank if it matches the specified value
            profile_image_url: str = str(
                preprocessed_user.get(EnrolledUsersFields.PROFILE_IMAGE_URL)
            )
            if profile_image_url.endswith(
                EnrolledUsersFields.DEFAULT_PROFILE_IMAGE_URL
            ):
                preprocessed_user[EnrolledUsersFields.PROFILE_IMAGE_URL] = ""

            preprocessed_users.append(preprocessed_user)

    return preprocessed_users


def process_courses(program: dict) -> dict:
    """process courses data.

    Args:
        courses (dict): Courses data.

    Returns:
        dict: Processed courses data.
    """
    if not program:
        return {}

    if "courses" in program:
        for course in program["courses"]:
            if course["courseimage"].startswith("data:image/"):
                course["courseimage"] = ""

    program["courses"] = sorted(
        program["courses"], key=lambda course: course["fullname"]
    )

    return program


def process_course_contents_to_file_list(
    course_contents: list,
) -> list[FileData]:  # #NOSONAR
    # TODO: Remove
    # function Cognitive Complexity from 22
    """process course contents to a list of files.

    Args:
        course_contents (list): List of course contents.

    Returns:
        list: List of course content files.
    """
    if not course_contents:
        return []

    files = []

    file_number = 0
    for course_content in course_contents:
        if "modules" in course_content:
            for module in course_content["modules"]:
                if "contents" in module:
                    for content in module["contents"]:
                        if "fileurl" in content:
                            file_number += 1
                            file_data = FileData(
                                file_number,
                                content["filename"],
                                content["fileurl"],
                                content["filesize"],
                                content["timemodified"],
                            )
                            files.append(file_data)
    return files


def group_courses_by_category(courses_json: list[dict]) -> dict:
    """Group courses by category.

    Args:
        courses_json (dict): Courses data.

    Returns:
        dict: Courses grouped by category.
    """
    courses_by_category = {}

    # Group courses by category
    for course in courses_json:
        course_category = course.get("coursecategory", "")
        if course_category:
            if course_category not in courses_by_category:
                courses_by_category[course_category] = []
            courses_by_category[course_category].append(course)

    return courses_by_category
