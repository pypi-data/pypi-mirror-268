"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
API Controller Class
"""

from json import loads
from requests import post, Response
from .api_functions import (
    CORE_COURSE_GET_CONTENTS,
    CORE_COURSE_GET_ENROLLED_COURSES_BY_TIMELINE_CLASSIFICATION,
    CORE_ENROL_GET_ENROLLED_USERS,
    MOD_ASSIGN_GET_ASSIGNMENTS,
    MOD_ASSIGN_GET_SUBMISSIONS,
)


class Api:
    """This class is responsible for calling endpoints of the Moodle API."""

    WEB_SERVICE_PATH: str = "webservice/rest/server.php"

    def __init__(
        self, server: str, token: str, rest_format: str = "json", timeout: float = 300.0
    ):
        self._moodle_url: str = (
            f"{server}/{self.WEB_SERVICE_PATH}?wstoken={token}&moodlewsrestformat={rest_format}"
        )
        self._timeout: float = timeout
        self._token: str = token

    @property
    def moodle_url(self):
        """Moodle URL

        Returns:
            str: The Moodle URL
        """
        return self._moodle_url

    @property
    def timeout(self) -> float:
        """Timeout

        Returns:
            float: The timeout
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value: float) -> None:
        """Set the timeout

        Args:
            value (float): The timeout
        """
        self._timeout = value

    @property
    def token(self) -> str:
        """Token

        Returns:
            str: The token
        """
        return self._token

    def call_moodle_api(self, function_name: str, params: dict) -> list[dict] | dict:
        """Call a Moodle API function

        Args:
            function_name (str): The function name
            params (dict): The parameters

        Returns:
            dict: The result
        """
        url = f"{self.moodle_url}&wsfunction={function_name}"
        response: Response = post(url, params=params, timeout=self.timeout)
        return loads(response.content)

    def get_assignment_submissions(self, assignment_id: str) -> dict:
        """Get assignment submissions.

        Args:
            assignment_id (str): The assignment id.

        Returns:
            dict: A dictionaries containing submission information.
        """
        params = {"assignmentids[0]": assignment_id}
        json = self.call_moodle_api(MOD_ASSIGN_GET_SUBMISSIONS, params)
        return self.__get_dict(json)

    def get_course_assignments(self, course_id: str) -> dict:
        """Get assignments from a course

        Args:
            course_id (str): The course id

        Returns:
            list: A json list of assignments
        """
        params = {"courseids[0]": course_id}
        json = self.call_moodle_api(MOD_ASSIGN_GET_ASSIGNMENTS, params)
        return self.__get_dict(json)

    def get_course_contents(self, course_id: str) -> list[dict]:
        """Get contents from a course

        Args:
            course_id (str): The course id

        Returns:
            list: A json list of contents
        """
        params = {"courseid": course_id}
        json = self.call_moodle_api(CORE_COURSE_GET_CONTENTS, params)
        return self.__get_list(json)

    def get_course_enrolled_users(self, course_id: str) -> list[dict]:
        """Get enrolled users in a course

        Args:
            course_id (str): The course id

        Returns:
            list[dict] | dict: A json list of enrolled users
        """
        params = {"courseid": course_id}
        json = self.call_moodle_api(CORE_ENROL_GET_ENROLLED_USERS, params)
        return self.__get_list(json)

    def get_program_courses(self) -> dict:
        """Get the college program with the courses you have enrolled on

        Returns:
            dict: A json object with courses
        """
        params = {"classification": "inprogress"}

        json = self.call_moodle_api(
            CORE_COURSE_GET_ENROLLED_COURSES_BY_TIMELINE_CLASSIFICATION,
            params,
        )
        return self.__get_dict(json)

    def __get_dict(self, item: dict | list[dict]) -> dict:
        """Get a json object

        Args:
            value (dict | list[dict]): The item to check

        Raises:
            ValueError: If the item is not a json object

        Returns:
            dict: The json object
        """
        if isinstance(item, dict):
            return item

        raise ValueError(f"Expected a json object {item}")

    def __get_list(self, item: dict | list[dict]) -> list[dict]:
        """Get a json list

        Args:
            value (dict | list[dict]): The item to check

        Raises:
            ValueError: If the item is not a json list

        Returns:
            list[dict]: The json list
        """
        if isinstance(item, list):
            return item

        raise ValueError(f"Expected a json list {item}")
