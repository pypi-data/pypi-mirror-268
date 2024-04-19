"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Filename and directory utility functions for Project Structure.
"""

from html import unescape
from re import search, sub


def clean_course_name(course_fullname: str) -> str:
    """Clean the course name, by placing the year at the end of the string.

    Args:
        input_string (str): The input string

    Returns:
        str: The clean course name
    """
    fullname = unescape(course_fullname).replace("&", "and")
    clean_name, year = get_course_name_parts(fullname)
    return f"{clean_name}{year}"


def clean_course_slug(course_fullname: str) -> str:
    """Get the course directory

    Args:
        course (dict): The course

    Returns:
        str: The course directory
    """
    return make_slug(clean_course_name(course_fullname))


def content_course_filename(number: int, filename: str) -> str:
    """Generate a course filename.

    Args:
        number (int): The course file number
        filename (str): The filename

    Returns:
        str: The generated filename
    """
    return f"{number:02d}-{make_slug(filename)}"


def course_directory(course: dict) -> str:
    """Get the course directory

    Args:
        course (dict): The course

    Returns:
        str: The course directory
    """
    course_id = course.get("id", "")
    fullname = course.get("fullname", "")
    return course_directory_with(course_id, fullname)


def course_directory_with(course_id: str, fullname: str) -> str:
    """Parse the course name from the course details.

    Args:
        course_id (str): The course id.
        fullname (str): The course full name.

    Returns:
        str: The course name.
    """
    name = clean_course_name(fullname)
    return make_slug(f"{name}-id-{course_id}")


def course_contents_filename(course_name: str):
    """Create a course content JSON filename

    Args:
        course_name (str): The course name

    Returns:
        str: The filename
    """
    return f"course-{make_slug(clean_course_name(course_name))}-contents.json"


def get_course_name_parts(course_full_name: str) -> tuple[str, str]:
    """Get the course name parts.

    Args:
        course_full_name (str): The course full name

    Returns:
        tuple[str, str]: The course name and the year
    """
    # Extract year "(23-24)"
    match = search(r"\(\d+-\d+\)", course_full_name)
    if match:
        year = match.group(0)
        return course_full_name.replace(year, "").strip(), year

    return course_full_name, ""


def get_enrolled_filename(course_name: str, file_type: str = "json") -> str:
    """Create an enrolled filename

    Args:
        course_name (str): The course name

    Returns:
        str: The filename
    """
    return f"enrolled-users-{clean_course_slug(course_name)}.{file_type}"


def get_assignments_filename(course_name: str) -> str:
    """Create an assignments filename

    Args:
        course_name (str): The course name

    Returns:
        str: The filename
    """
    return f"{clean_course_slug(course_name)}-assignments.json"


def get_submissions_filename(course_name: str, assignment_name: str) -> str:
    """Create an submissions filename

    Args:
        course_name (str): The course name

    Returns:
        str: The filename
    """
    return f"{clean_course_slug(course_name)}-submission-{make_slug(assignment_name)}.json"


def make_slug(filename: str) -> str:
    """Generate a clean filename slug.
    Removes illegal characters and replaces spaces with dashes.
    Collapses multiple dashes into one.

    Args:
        filename (str): The filename

    Returns:
        str: The generated filename
    """
    # Define the pattern to match illegal characters
    illegal_chars_pattern = r'[/:*?"<>|%\\\x00-\x1f\x7f]'
    # Replace illegal characters with space
    slug = sub(illegal_chars_pattern, " ", filename)
    # Remove consecutive spaces
    slug = sub(r"\s+", " ", slug)
    # Replace spaces with dashes
    slug = slug.replace(" ", "-")
    # Replace parentheses with dashes
    slug = sub(r"[\(\)]", "-", slug)
    # Collapse multiple dashes into one
    slug = sub(r"-+", "-", slug)
    # Remove leading and trailing dashes and spaces
    return slug.strip("- ").replace("-.", ".").lower()
