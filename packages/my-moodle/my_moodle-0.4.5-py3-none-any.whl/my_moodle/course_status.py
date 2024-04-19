"""
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
Course Status Enum
"""

from enum import Enum


class CourseStatus(Enum):
    """Course Status
    Args:
        Enum (str): The course status
    """

    ACTIVE = "Active"
    PAST_FINISHED = "Past/Finished"
    UPCOMING = "Upcoming"
